// Deceitful War.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"

using namespace std;

void exchange(float A[], int i, int j) {
	float t;
	t = A[i];
	A[i] = A[j];
	A[j] = t;

	return;
}

//实现快速排序
int partition(float A[], int p, int r) {
	float x = A[r];
	int i = p - 1;
	for(int j=p;j<=r-1;j++) {
		if(A[j] <= x) {
			i = i + 1;
			exchange(A, i, j);
		}
	}
	exchange(A, i + 1, r);
	return i + 1;
}

void quicksort(float A[], int p, int r) {
	int pivot = -1;
	if(p < r) {
		pivot = partition(A, p, r);
		quicksort(A, p, pivot - 1);
		quicksort(A, pivot + 1, r);
	}
}

//实现二叉查找树
typedef struct node{
	float key;
	struct node* left;
	struct node* right;
	struct node* p;
}node;

typedef struct tree{
	node* root;
}tree;

node* tree_minimum(node* x) {
	while(x->left != NULL) {
		x = x->left;
	}
	return x;
}

node* tree_maximum(node* x) {
	while(x->right != NULL) {
		x = x->right;
	}
	return x;
}

//中序遍历顺序下节点x的后继
node* tree_successor(node* x){
	if(x->right != NULL) {
		return tree_minimum(x->right);
	}

	node* y = x->p;
	while(y != NULL && x == y->right) {
		x = y;
		y = y->p;
	}
	return y;
}

//中序遍历顺序下节点x的前趋
node* tree_predecessor(node* x){
	if(x->left != NULL) {
		return tree_maximum(x->left);
	}

	node* y = x->p;
	while(y != NULL && x == y->left) {
		x = y;
		y = y->p;
	}
	return y;
}

//树的根节点可能会改变
void tree_insert(tree* T, node* z) {
	node* y = NULL;
	node* x = T->root;
	
	while(x != NULL) {
		y = x;
		if(z->key < x->key) {
			x = x->left;
		} else {
			x = x->right;
		}
	}
	z->p = y;
	if(y == NULL) {
		T->root = z;
	} else {
		if(z->key < y->key) {
			y->left = z;
		} else {
			y->right = z;
		}
	}

	return;
}

//树的根节点可能会改变
//z指向的节点的值可能会变
node* tree_delete(tree* T, node* z) {
	node* y = NULL;
	if(z->left == NULL || z->right == NULL) {
		y = z;
	} else {
		y = tree_successor(z);
	}

	node* x = NULL;
	if(y->left != NULL) {
		x = y->left;
	} else {
		x = y->right; 
	}

	if(x != NULL) {
		x->p = y->p;
	}

	if(y->p == NULL) {
		T->root = x;
	} else {
		if(y == y->p->left) {
			y->p->left = x;
		}
		else {
			y->p->right = x;
		}
	}

	if(y != z) {
		z->key = y->key;
	}

	return y;//防止内存泄露
}

//Ken's optimal strategy
//返回值是Ken选出来的block的重量
//根据问题描述可以断定此时Ken不会是空集
float Ken(tree* Ken, float Told_Naomi) {
	float r = -1.0;//用于预先保存要删除节点的值，否则在删除后可能会取不到

	//先将Told_Naomi插入Ken树中
	node* t = (node*)malloc(sizeof(node));
	t->key = Told_Naomi;
	t->p = NULL;
	t->left = NULL;
	t->right = NULL;
	tree_insert(Ken, t);
	//再找Told_Naomi的直接后继，若不为空就是大于Told_Naomi的最小值
	node* y = tree_successor(t);
	t = tree_delete(Ken, t);//删除Told_Naomi
	delete(t);//防止内存泄露
	if(y != NULL) {		
		r = y->key;
	}
	//若为空则Told_Naomi比Ken的block都重，选一个最轻的block
	else {
		y = tree_minimum(Ken->root);
		r = y->key;
	}
	
	y = tree_delete(Ken, y);
	delete(y);//防止内存泄露
	return r;
}

//Naomi's strategy when she is playing War!
//可以随意选择block,此处按由小到大排序
//k表示第k次较量，取0至N-1，N为初始时block的数量
float Honest_Naomi(float Naomi[], int k) {
	return Naomi[k];
}

//Naomi's optimal strategy when she is playing Deceitful War!
//Naomi的block已经由轻到重排好序，目的是用尽可能轻的block骗Ken出尽可能重的block
//修正：当Naomi手里最轻的block要比Ken手里最轻的block重时，就有一次得分机会，应该把Told_Naomi设置的比Ken手里最重的block还重，骗他出最轻的block
//每次都要比较Naomi手里最轻的block与Ken手里最轻的block,以确定策略
//k表示第k次较量，取0至N-1，N为初始时block的数量
//返回值是一个指向float数组的指针，数组包含两个元素，第一个是Told_Naomi,第二个是Chosen_Naomi
float* Clever_Naomi(float Naomi[], tree* Ken, int k) {
	float* r = (float*)malloc(sizeof(float) * 2);
	node* y1 = tree_maximum(Ken->root);
	node* y2 = tree_predecessor(y1);
	node* y3 = tree_minimum(Ken->root);

	if(Naomi[k] > y3->key) { //可以得分
		r[0] = (y1->key + 1) / 2; //欺骗的关键一步！
		r[1] = Naomi[k];
	} else { //不能得分，骗掉Ken最重的block
		if(y2 != NULL) {
			if(y2->key > Naomi[k]) {
				r[0] = (y1->key + y2->key) / 2; //欺骗的关键一步！
			} else {
				r[0] = Naomi[k];
			}
			r[1] = Naomi[k];
		} else {
			//两方各剩一个block
			r[0] = Naomi[k];
			r[1] = Naomi[k];
		}
	}

	return r;
}

//Ken的block值需要两份，因为需要较量两次
int* deceitful_war(int N, float Naomi[], tree* Ken1, tree* Ken2) {
	int* points = (int*)malloc(sizeof(int) * 2);
	points[0] = 0;//Clever Naomi的得分
	points[1] = 0;//Honest Noami的得分
	for(int k=0;k<N;k++) {
		float* r_Clever_Naomi = Clever_Naomi(Naomi, Ken1, k);
		float r_Ken1 = Ken(Ken1, r_Clever_Naomi[0]);
		if(r_Clever_Naomi[1] > r_Ken1) {
			points[0] += 1;
		}

		float r_Honest_Naomi = Honest_Naomi(Naomi, k);
		float r_Ken2 = Ken(Ken2, r_Honest_Naomi);
		if(r_Honest_Naomi > r_Ken2) {
			points[1] += 1;
		}
	}

	return points;
}

//完成输入输出任务
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\Code jam\\Deceitful War\\D-large.in");
	ofstream out("d:\\Code jam\\Deceitful War\\D-large.out");
	int T = 0;

	in >> T;
	for(int t=1;t<=T;t++) {
		int N = 0;
		in >> N;//blocks的数量
		float* Naomi = (float*)malloc(sizeof(float) * N);
		tree Ken1 = { NULL };
		tree Ken2 = { NULL };
		for(int k=0;k<N;k++) {
			in >> Naomi[k];
		}
		for(int k=0;k<N;k++) {
			float w = 0;
			in >> w;
			node* k1 = (node*)malloc(sizeof(node));
			node* k2 = (node*)malloc(sizeof(node));
			k1->key = k2->key = w;
			k1->p = k2->p = NULL;
			k1->left = k2->left = NULL;
			k1->right = k2->right = NULL;
			tree_insert(&Ken1, k1);
			tree_insert(&Ken2, k2);
		}
		quicksort(Naomi, 0, N-1);
		int* points = deceitful_war(N, Naomi, &Ken1, &Ken2);
		out << "Case #" << t << ": " << points[0]  << " " << points[1] << endl;
	}
	return 0;
}