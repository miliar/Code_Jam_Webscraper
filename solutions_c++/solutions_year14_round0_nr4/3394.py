// Deceitful War.cpp : �������̨Ӧ�ó������ڵ㡣
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

//ʵ�ֿ�������
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

//ʵ�ֶ��������
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

//�������˳���½ڵ�x�ĺ��
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

//�������˳���½ڵ�x��ǰ��
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

//���ĸ��ڵ���ܻ�ı�
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

//���ĸ��ڵ���ܻ�ı�
//zָ��Ľڵ��ֵ���ܻ��
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

	return y;//��ֹ�ڴ�й¶
}

//Ken's optimal strategy
//����ֵ��Kenѡ������block������
//���������������Զ϶���ʱKen�����ǿռ�
float Ken(tree* Ken, float Told_Naomi) {
	float r = -1.0;//����Ԥ�ȱ���Ҫɾ���ڵ��ֵ��������ɾ������ܻ�ȡ����

	//�Ƚ�Told_Naomi����Ken����
	node* t = (node*)malloc(sizeof(node));
	t->key = Told_Naomi;
	t->p = NULL;
	t->left = NULL;
	t->right = NULL;
	tree_insert(Ken, t);
	//����Told_Naomi��ֱ�Ӻ�̣�����Ϊ�վ��Ǵ���Told_Naomi����Сֵ
	node* y = tree_successor(t);
	t = tree_delete(Ken, t);//ɾ��Told_Naomi
	delete(t);//��ֹ�ڴ�й¶
	if(y != NULL) {		
		r = y->key;
	}
	//��Ϊ����Told_Naomi��Ken��block���أ�ѡһ�������block
	else {
		y = tree_minimum(Ken->root);
		r = y->key;
	}
	
	y = tree_delete(Ken, y);
	delete(y);//��ֹ�ڴ�й¶
	return r;
}

//Naomi's strategy when she is playing War!
//��������ѡ��block,�˴�����С��������
//k��ʾ��k�ν�����ȡ0��N-1��NΪ��ʼʱblock������
float Honest_Naomi(float Naomi[], int k) {
	return Naomi[k];
}

//Naomi's optimal strategy when she is playing Deceitful War!
//Naomi��block�Ѿ����ᵽ���ź���Ŀ�����þ��������blockƭKen���������ص�block
//��������Naomi���������blockҪ��Ken���������block��ʱ������һ�ε÷ֻ��ᣬӦ�ð�Told_Naomi���õı�Ken�������ص�block���أ�ƭ���������block
//ÿ�ζ�Ҫ�Ƚ�Naomi���������block��Ken���������block,��ȷ������
//k��ʾ��k�ν�����ȡ0��N-1��NΪ��ʼʱblock������
//����ֵ��һ��ָ��float�����ָ�룬�����������Ԫ�أ���һ����Told_Naomi,�ڶ�����Chosen_Naomi
float* Clever_Naomi(float Naomi[], tree* Ken, int k) {
	float* r = (float*)malloc(sizeof(float) * 2);
	node* y1 = tree_maximum(Ken->root);
	node* y2 = tree_predecessor(y1);
	node* y3 = tree_minimum(Ken->root);

	if(Naomi[k] > y3->key) { //���Ե÷�
		r[0] = (y1->key + 1) / 2; //��ƭ�Ĺؼ�һ����
		r[1] = Naomi[k];
	} else { //���ܵ÷֣�ƭ��Ken���ص�block
		if(y2 != NULL) {
			if(y2->key > Naomi[k]) {
				r[0] = (y1->key + y2->key) / 2; //��ƭ�Ĺؼ�һ����
			} else {
				r[0] = Naomi[k];
			}
			r[1] = Naomi[k];
		} else {
			//������ʣһ��block
			r[0] = Naomi[k];
			r[1] = Naomi[k];
		}
	}

	return r;
}

//Ken��blockֵ��Ҫ���ݣ���Ϊ��Ҫ��������
int* deceitful_war(int N, float Naomi[], tree* Ken1, tree* Ken2) {
	int* points = (int*)malloc(sizeof(int) * 2);
	points[0] = 0;//Clever Naomi�ĵ÷�
	points[1] = 0;//Honest Noami�ĵ÷�
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

//��������������
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream in("d:\\Code jam\\Deceitful War\\D-large.in");
	ofstream out("d:\\Code jam\\Deceitful War\\D-large.out");
	int T = 0;

	in >> T;
	for(int t=1;t<=T;t++) {
		int N = 0;
		in >> N;//blocks������
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