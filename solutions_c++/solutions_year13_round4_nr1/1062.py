
#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<map>
#include<queue>
#include<algorithm>
#include<stack>
#include<iomanip>
#define PR(X) cout << (X) << endl
const long long module = 1000002013;
using namespace std;
ifstream in("1.in");
ofstream out("1.out");
long long  n , m;
long long ans1, ans2, ans;
const int maxn = 10005;
long long e[maxn], o[maxn], p[maxn];

struct Event{
	long long pos;
	long long people;
	int flag; // 1 in 0 out
	Event& operator = (const Event& x){
		pos = x.pos;
		people = x.people;
		flag = x.flag;
	}
	//event(long long  p,long long peo, int f):pos(p),people(peo),flag(f){}
};
Event eve[maxn];

///养成updata的好习惯。但凡修改num，均需要Updata。

class Splay{
	protected:


	public:
		class Node{
			public:
				int data;
				Node* left, *right, *parent;
				int num;//the number of data
				int size;
				Node(){}
				Node(int parData, int parNum, Node* parParent = NULL)
					{
//						PR(132);
						data = parData;
						parent = parParent;
						num = parNum;
						size = parNum;
						left = NULL;
						right = NULL;
					}
				bool leftRotate(){//This Node is the left child of its parent
					parent->left = right;
					if (right != NULL) right->parent = parent;
					if (parent->parent != NULL)
						if (parent->parent->right == parent)///这里还错了半天，原来等号右边写的是parent->parent
							parent->parent->right = this;
						else
							parent->parent->left = this;///这个比较容易写错。我第一次没写，第二次写成了针对left\right
					right = parent;
					parent = parent->parent;
					right->parent = this;

					Splay::updata(right);
					Splay::updata(this);
				}
				bool rightRotate(){
					parent->right = left;
					if (left != NULL) left->parent = parent;
					if (parent->parent != NULL)
						if (parent->parent->right == parent)
							parent->parent->right = this;
						else
							parent->parent->left = this;
					left = parent;
					parent = parent->parent;
					left->parent = this;

					Splay::updata(left);
					Splay::updata(this);
				}
				bool rotate(){
					if (parent == NULL) return false;
					else if (parent->left == this) leftRotate();
						 else rightRotate();
				}
		};
		Node* head;
		Splay(){
			head = NULL;
		}

		bool rotate(Node* parNode){//parNode为儿子。自动判断左旋还是右旋。
			if (parNode->parent == NULL) return false;
			if (parNode->parent == head) head = parNode;//在这里维护全局标记
			else
				if (parNode->parent->left == parNode) parNode->leftRotate();
				else parNode->rightRotate();

		}

		static void updata(Node* now){
			if (now == NULL) return;
			now->size = now->num;
			if (now->left != NULL){
				now->size += now->left->size;
			}
			if (now->right != NULL){
				now->size += now->right->size;
			}
		}
		void lift(Node* parNode, Node* target = NULL){
			if (parNode == NULL) return;
			while (parNode ->parent != target){
				if (parNode ->parent->parent == target) rotate(parNode);
				else{
					if ((parNode->parent->left == parNode) ^//亦或关系
						(parNode->parent->parent->left == parNode->parent)){
						rotate (parNode);
						rotate (parNode);
					}
					else{
						rotate(parNode->parent);
						rotate(parNode);
					}
				}
			}
			//p.s.关于head的处理在旋转中处理过了，所以无需更改。
		}
		int getSize(Node* now){
			if (now == NULL) return 0;
			else return now->size;
		}

		Node* findKth (int rank){
			return findKth(rank, head);
		}
		Node* findKth (int rank, Node* start){///如果rank大于head返回NULL
			if ((start == NULL) || (rank > start->size) || (rank <= 0)) return NULL;

			Node* now = start;
			while (true){
				int leftSize = ((now->left == NULL)?0:now->left->size);
				if (rank <= leftSize) now = now->left;
				else if (rank > leftSize + now->num) {
						rank = rank - leftSize - now->num;
						now = now->right;
					 }
					 else break;
			}
			lift(now);///ADD
			return now;
		}
		Node* findMinKth (int rank){return findKth(rank, head);}
		Node* findMinKth (int rank, Node* start){return findKth(rank, start);}
		Node* findMaxKth (int rank){
			return findMaxKth(rank, head);
//another choice:		return findKth(head->size + 1 -rank, head);
		}
		Node* findMaxKth (int rank, Node* start){///如果rank大于总大小返回NULL
			if ((start == NULL) || (rank > start->size) || (rank <= 0)) return NULL;
//another choice:		return findKth(start->size + 1 - rank, start);删除下面所有
			Node* now = start;
			while (true){
				int rightSize = ((now->right == NULL)?0:now->right->size);
				if (rank <= rightSize) now = now->right;
				else if (rank > rightSize + now->num) {
						rank = rank - rightSize - now->num;
						now = now->left;
					 }
					 else break;
			}
			lift(now);///ADD
			return now;
		}

		Node* find (int parData){///if FAILED,return the last visited Node.null means no head
			Node* now = head;
			while (now != NULL){
				if (parData < now->data){
					if (now->left == NULL) break;
					else now = now->left;
				}
				else if (parData > now->data){
					if (now->right == NULL) break;
					else now = now->right;
				}
				else break;///设TreeData的比较满足三岐率，固非大于，非小于，则等于。
			}
			lift(now);
			return now;
		}
		///发现insert的时候不能lift，lift就挂了。必须添加在leaf上
		Node* findLeaf (int parData){//if FAILED,return the last visited Node.null means no head
			Node* now = head;
			while (now != NULL){
				if (parData < now->data){
					if (now->left == NULL) break;
					else now = now->left;
				}
				else if (parData > now->data){
					if (now->right == NULL) break;
					else now = now->right;
				}
				else break;///设TreeData的比较满足三岐率，固非大于，非小于，则等于。
			}
			return now;
		}

		Node* findMax(){return findMax(head);}
		Node* findMax(Node* start){
			if (start == NULL) return NULL;
			Node* now = start;
			while (now->right != NULL) now = now->right;
			lift(now);
			return now;
		}

		Node* findMin(){return findMin(head);}
		Node* findMin(Node* start){///如果start为null 返回NULL
			if (start == NULL) return NULL;
			Node* now = start;
			while (now->left != NULL) now = now->left;
			lift(now);
			return now;
		}

		Node* next(Node* now){///如果now为最大值 返回NULL
			if (now == NULL) return NULL;
			lift(now);
			return findMin(now->right);
		}

		Node* pre(Node* now){///如果now为最大值 返回NULL
			if (now == NULL) return NULL;
			lift(now);
			return findMax(now->left);
		}

		Node* insert(int parData, int parNum){
//			PR(parData);
//			PR(parNum);
//			PR(1232);
			if (head == NULL) {
//				PR(1232);
				head = new Node;
				head->data = parData;
				head->num = parNum;
				head->size = parNum;
				head->left = NULL;
				head->parent = NULL;
				head->right = NULL;
			}
			else{
//				PR(1232);
				Node* findNode = findLeaf(parData);
				if (findNode->data == parData) {
					findNode->num += parNum;
					updata(findNode);///ADD 有可能直接就是根节点
					lift(findNode);
				}
				else {
					Node* newNode = new Node(parData, parNum, findNode);
					if (parData < findNode->data)
						findNode->left = newNode;
					else findNode->right = newNode;
					updata(findNode); ///ADD
					lift(newNode);
				}
			}
//			PR(1232);
			return head;
		}

		int erase(int parData, int parNum, bool isAll = false){
			if (head == NULL) return 0;
			Node* findNode = find(parData);
			int remain = 0;
			if (head->data != parData) return 0;
			else {
//CALCULATE THE ANS

				if (head->num >= parNum) {
					head->num -= parNum;
				}
				else{
					remain = parNum - head->num;
					head->num = 0;

				}
				updata(head);///ADD

				if (head->num == 0){
					Node* nextNode = next(head);
					if (nextNode == NULL){///删除根节点
						head = head->left;
						if (head != NULL)
							head->parent = NULL;
						updata(head);
					}
					else {///删除根节点的左孩子
						head->left = head->left->left;
						if (head->left != NULL)
							head->left->parent = head;///此处和上面忘记修改父亲节点了。
						updata(head);
					}
					delete findNode;
				}
			}
			return remain;
		}
		void innerDfs1(Node* now){
			if (now == NULL) return;
			cout << now->data << ' ';
			innerDfs1(now->left);
			innerDfs1(now->right);
		}
		void innerDfs2(Node* now){
			if (now == NULL) return;
			innerDfs2(now->left);
			cout << now->data << ' ';
			innerDfs2(now->right);
		}
		void dfs(){
			innerDfs1(head);
			cout << endl;
			innerDfs2(head);
			cout << endl;
		}
		~Splay(){}
};
Splay *splay;


bool cmp1(const Event &x, const Event & y){
	if ((x.pos < y.pos) || ((x.pos == y.pos) && (x.flag > y.flag))){
		return true;
	}
	return false;
}
int main(){

	long long testsum;
	in >> testsum;
	for (int iTest = 1; iTest <= testsum; iTest++){
		splay = new Splay;
		out << "Case #" << iTest << ": ";
		in >> n >> m ;
		ans1 = 0;
		ans2 = 0;
		ans = 0;
		for (int i = 1; i<=m; i++){
			in >> e[i] >> o[i] >> p[i];
			long long  k = (o[i] - e[i]);
			ans1  = (ans1 + p[i] *
					((n*k - k*(k-1)/2) %module) % module) % module;
			eve[2*i-1].flag = 1;
			eve[2*i-1].pos = e[i];
			eve[2*i-1].people = p[i];
			eve[2*i].flag = 0;
			eve[2*i].pos = o[i];
			eve[2*i].people = p[i];
		}
//		for (int i = 1; i <= 2*m; i++){
//			PR(eve[i].flag);
//			PR(eve[i].pos);
//			PR(eve[i].people);
//		}
//		PR(endl);
		sort(eve+1, eve+2*m+1, cmp1);
//		for (int i = 1; i <= 2*m; i++){
//			cout <<eve[i].flag <<' '<< eve[i].pos<<' '<< eve[i].people<< endl;
//		}
//		PR(endl);

		for (int i = 1; i <= 2*m; i++){
//			PR(i);
			if (eve[i].flag == 1){
				splay->insert(eve[i].pos, eve[i].people);
			}
			if (eve[i].flag == 0){
				int remain = eve[i].people;
				while (remain != 0){
					long long max = splay->findMax()->data;
					long long delta = remain - splay->erase(max, remain);
					remain -= delta;
					long long k = eve[i].pos - max;
					cout << delta << ' ' << n << ' ' << k << endl;
					cout << n*k - k*(k-1)/2 << endl;
					ans = (ans + delta *
					((n*k - k*(k-1)/2) %module) % module) % module;
				}
			}
		}

		cout << "anso" << ans1 << endl;
		cout << "ans" << ans << endl;
		out << ((ans1 - ans) % module + module) %module;
		out << endl;
	}
}
