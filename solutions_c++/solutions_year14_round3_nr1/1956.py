#include <iostream>
using namespace std;
#include<vector>
#include <string>
#include<stack>
#include<list>
#include <string>
#include <vector>
#include <bitset>
#include <sstream>
#include <algorithm>
#include<list>
#include<time.h>
#include <map>
#include <fstream>
#include <deque>
#include <hash_map>
#include <set>

class IntSetBST
{ 
private:
	int n, *v, vn;
	struct node
	{
		int val;
		node *left, *right;
		node(int i){ val = i; left = right = 0; }
	};
	node *root;
	IntSetBST(int maxelements, int maxv){ root = nullptr; }

};

class Shape
{

protected:
	double length;
	double area;
	void print_protected(){ cout<<"This is a protected function in Shape\n"; }
	
public:
	Shape(){}
	Shape(double x, double y){ area = x; length = y; }
	virtual double CalculateArea(){ return 0; }
	void print_public(){ cout<<"This is a public functionn in Shape\n"; }
	 ~Shape(){}
};

class Circle: public Shape
{
public:
	Circle(double x, double y)
	{
		area = x;
		length = y;
	}
	double CalculateArea(){ return 1; }
};

class Eclipse: public Circle
{
public:
	Eclipse(double x, double y):Circle(x,y){};
	double CalculateArea(){ return 2; }
};

class Base
{
public:
	static int n;
	static const int c = 1;
	Base(){}
	virtual ~Base(){}
};

int Base::n = 1;



class LinkList
{
	struct node
	{
	public:
		node *next;
		int val;
		node(int v){ val = v; next = nullptr; }
	};
public:
	node *first;
	node *last;
	LinkList()
	{
		first = nullptr;
		last = nullptr;
	}
	void Add(int v)
	{
		node *n = new node(v);
		if(first==nullptr)
			first = n;
		else
			last->next = n;
		last = n;
	}

	void deleteNode( int val)
	{
		node *p = first, *pre = first;
		while (p->val != val && p!=nullptr)
		{
			pre = p;
			p = p->next;
		}
		
		if(p->val==val)
		{
			
			if(p==first)
				first=p->next;
			else 
				pre->next = p->next;
			delete p;
		}
		
	}

	void insertNode( int k, int val)
	{
		node *p = first, *pre = first;
		while (p->val != k && p!=nullptr)
		{
			pre = p;
			p = p->next;
		}
		if(p==nullptr)
			return;
		node *t = new node(val);
		t->next = p->next;
		p->next = t;
		
	}

	void print()
	{
		node *p = first;
		int i=0;
		while (p!=nullptr)
		{
			cout<<p->val<<' ';
			p = p->next;
			if(++i%10==9)
				cout<<'\n';
		}
		cout<<'\n';
	}

	void Reverse()
	{
		node *pre = first;
		node *p  = first->next;
		node *post = first->next->next;

		first->next = nullptr;
		
		while (p!=nullptr)
		{
			post = p->next;
			p->next = pre;
			pre = p;
			p = post;
		}
		first = pre;
	}

	void Merge(LinkList ls1, LinkList ls2)
	{
		if(ls1.first==nullptr || ls2.first==nullptr)
			return;

		node *p = ls1.first, *q = ls2.first;
		node *head;
		if(p->val < q->val)
		{
			head = q;
			q = q->next;
		}
		else
		{
			head = p;
			p = p->next;
		}
		node *t = head;
		
		while (p!=nullptr && q!=nullptr)
		{
			if(p->val < q->val)
			{
					t->next = p;
					p = p->next;
			}
			else
			{
				t->next = q;
				q = q->next;
			}
			t = t->next;
		}
		if(p!=nullptr)
			t->next = p;
		if(q!=nullptr)
			t->next = q;
		first = head;
	}

	void InsertSort(LinkList ls)
	{

		node *head = ls.first;
		node *remaning;
		node *t;
		node *p;
		node *p1;

		remaning = head->next;
		head->next = nullptr;

		while (remaning != nullptr)
		{
			for(t = remaning, p = head, p1 = head; p!=nullptr&&p->val<t->val; p1 = p, p = p->next)
				;
			remaning = remaning->next;

			if(p==head)
				head = p;
			else
				p1->next = t;
			t->next = p;
		}
		ls.first = head;
	}
};

void print(int *arr, int l, int u)
{
	for(int i=l;i<=u;i++)
		cout<<arr[i]<<' ';
	cout<<'\n';
}

void InsertSort(int *arr, int l, int u)
{
	int i = l+1, j;
	for(; i<=u; i++)
	{
		int t = arr[i];
		for( j = i-1; j>=0;j-- )
		{
			if(arr[j] > t)
				arr[j+1] = arr[j];
			else
				break;
		}
		arr[j+1] = t;
	print(arr,0,i);
	}
}

void ShellSort(int *arr, int l, int u)
{
	for( int gap=(l+u)/2; gap>0;gap /= 2)
		for( int i=l+gap; i<=u; i++)
		{
			int t = arr[i];
			int j;
			for(j=i; j>0&&t < arr[j-gap]; j-=gap)
				arr[j] = arr[j-gap];
			arr[j] = t;
		}
}

int getAbsMin(int *arr,int N)
{
	if(N<=0)  throw "Invalid Arguments";
	int left=0;
	int right=N-1;
	if(arr[left]>=0) return arr[left];
	if(arr[right]<=0) return arr[right];
	int mid;
	while(true)
	{
		mid=(left+right)/2;
		if(arr[mid+1]<0) left=mid+1;  
		else if(arr[mid]>0) right=mid-1;  
		else if(arr[mid]+arr[mid+1]>=0) return arr[mid];  
		else return arr[mid+1];  
	}   
}

int StrAssign(const char * src, char *dst)
{
	if(src==nullptr || dst==nullptr)
		return -1;
	char *p = dst;
	while (*src!='\0')
	{
		*dst++ = *src++;
	}
	//*dst = '\0';
	return dst-p;
}

char * strcpy2(const char *src, char *dst)
{
	if(src==nullptr || dst==nullptr)
		throw "invalid arguments";
	char *p = dst;
	while(*p++=*src++)
		;
	return dst;
}

char *strcat2(char *dest, const char *src)
{
	if(dest==nullptr || src==nullptr)
		throw "invalid parameters";
	char *p = dest;
	while (*p++!='\0');
	p--;
	while (*p++=*src++);

	return dest;
}

int length2(char *str)
{
	if(str==nullptr)
		return 0;
	int n=0;
	while (str[++n]);
	return n;
}

void swapstar(char *c1, char *c2)
{
	char t = *c1;
	*c1 = *c2;
	*c2 = *c1;
}

void Reverse(char *str)
{
	if(str==nullptr)
		return;
	char *p = str;
	while(*p!='\0')
		p++;
	p--;
	while(str < p)
		swapstar(str++,p--);
}

void ReverseSentence(char *str)
{
	Reverse(str);
	char *p = str, *q = str;
	while (true)
	{
		if(*q==' ')
		{
			*q='\0';
			Reverse(p);
			*q=' ';
			p = q+1;
		}
		else if(*q == '\0')
		{
			Reverse(p);
			break;
		}
		q++;
		
	}
	while (str < q)
	{
		if(*str=='\0')
			*str = ' ';
		str++;
	}
}

class A
{
		friend class B;
private:
	void F(){}

};

class B
{
public:
	void F()
	{
		A a = A();
		a.F();
	}
};

void PrintIt(string &str)
{
	cout<<str<<' ';
}

void test(void func(string &str), string &sr)
{
	func(sr);
}

const string ToothbrushCode("0003");

class IsAToothbrush
{
public:
	IsAToothbrush(string &In):toothbrush(In){}
	bool operator() ( string& SalesRecord )
	{
		return toothbrush==SalesRecord;
	}
private:
	string toothbrush;
};

class EventIsIn1997
{
public:
	
	bool operator () (string& EventRecord)
	{
		// year field is at position 12 for 4 characters in EventRecord
		return EventRecord.substr(0,1)=="1997";
	}

};

template <typename T>
void PrintAny(T &t)
{
	cout<<t<<' ';
}

template <typename T>
int partition3(T* arr, int l, int u)
{
	int i = l, j = u+1;
	int t = arr[l];

	while (true)
	{
		do 
		{
			i++;
		} while (arr[i]<t&&i<=u);
		do 
		{
			j--;
		} while (arr[j]>t);
		if(i>j)
			break;
		swap(arr[i], arr[j]);
	}
	swap(arr[l], arr[j]);
	return j;
}

template <typename T>
void Qsort(T* arr, int l, int u)
{
	if(l>=u)
		return;
	int m = partition3(arr, l ,u);
	Qsort(arr, l, m-1);
	Qsort(arr, m+1, u);
}

int partition4(int *s, int l, int r)
{
	int i = l, j = r, x = s[l];
	while (i < j)
	{
		while(i < j && s[j] >= x) // 从右向左找第一个小于x的数
			j--;  
		if(i < j) 
			s[i++] = s[j];

		while(i < j && s[i] < x) // 从左向右找第一个大于等于x的数
			i++;  
		if(i < j) 
			s[j--] = s[i];
	}
	s[i] = x;
	return i;
}

#include <time.h>

class Top
{
public:
	int a;
	//virtual ~Top(){}
};

class Left: virtual public Top
{
public: 
	int b;
};

class Right: virtual public Top
{
public:
	int c;
};

class Bottom: public Left,  public Right
{
public: 
	int d;
	
};

class CA
{
	//int k; //如果基类没有数据成员，则在这里多重继承编译不会出现二义性
	int k;
	int i;
	int j;
public:
	void f() {cout << "CA::f" << endl;}
};

class CB : public CA
{
};

class CC : public CA
{
};

class CD : public CB, public CC
{
};


class Solution {
public:
	void reverseWords(string &s) 
	{
		string temp = "";
		reverse(s);
		int i=0, j = 0;
		int n = s.length();
		bool isFirst = true;
		while( j<n )
		{
			while( s[i]==' ' && i<n )
				i++;
			if(i==n)
				break;
			else
				j = i;

			while((s[j]!=' '&& s[j]!='\0')&&j<n)
				j++;
			string t = s.substr(i,j-i);
			reverse(t);
			if(!isFirst)
				temp += ' ';
			temp += t ;
			isFirst = false;
			i = j+1;
		}
		s = temp;
	}

	void reverse(string &s)
	{
		int n = s.length();
		int i=0, j=n-1;
		while(i<j)
		{
			swap(s[i],s[j]);
			i++;
			j--;
		}
	}

	int evalRPN(vector<string> &tokens) {
		stack<int> s;
		int i1, i2;
		
		vector<string>::iterator it = tokens.begin();
		for(; it!=tokens.end(); it++)
		{
			string t = *it;
			if(t=="+")
			{
				i1 = s.top();
				s.pop();
				i2 = s.top();
				s.pop();
				s.push(i1+i2);
			}
			else if(t=="-")
			{
				i1 = s.top();
				s.pop();
				i2 = s.top();
				s.pop();
				s.push(i2-i1);
			}
			else if(t=="*")
			{
				i1 = s.top();
				s.pop();
				i2 = s.top();
				s.pop();
				s.push(i1*i2);
			}
			else if(t=="/")
			{
				i1 = s.top();
				s.pop();
				i2 = s.top();
				s.pop();
				s.push(i2/i1);
			}
			else
			{
				s.push(str2int(*it));
			}
		}
		return s.top();
	}

	int str2int( const string &s)
	{
		stringstream ss;
		ss<<s;
		int n;
		ss>>n;
		return n;
	}
};

#define MaxNode 26
struct TrieNode 
{
	bool isWord;
	TrieNode *next[MaxNode];
	TrieNode()
	{
		isWord = false;
		for(int i=0;i<MaxNode;i++)
			next[i] = nullptr;
	}
};
void insert(TrieNode *root, string s)
{
	if(root==nullptr)
		return;
	unsigned int i = 0;
	TrieNode *p = root;
	while (i<s.length())
	{
		if(p->next[s[i]-'a'] == nullptr)
		{
			TrieNode *temp=new TrieNode();
			p->next[s[i]-'a'] = temp;
			p = p->next[s[i]-'a'];
		}
		else
		{
			p = p->next[s[i]-'a'];
		}
		i++;
	}
	p->isWord = true;

}
bool search(TrieNode *root, const string &str)
{
	TrieNode *p = root;
	string::const_iterator it = str.begin();
	while (p!=nullptr && it!=str.end())
	{
		p = p->next[*it++-'a'];
	}
	return (p!=nullptr && p->isWord==true);
}
void del(TrieNode *root)
{
	int i;
	for( i=0; i<MaxNode; i++)
	{
		if(root->next[i] != nullptr)
			del(root->next[i]);
	}
	free(root);
}
void printPrime(int &n)
{
	bool *p = new bool[n+1];
	for(int i=0;i<=n;i+=2)
	{
			p[i] = false;
			p[i+1] = true;
	}

	for(int i=3;i<=n;i+=2)
		if(p[i]==true)
			for(int j=2;j*i<=n;j++)
				p[j*i] = false;
	p[1] = false;
	p[2] = true;
	for(int i=2;i<=n;i++)
		if(p[i]==true)
			cout<<i<<' ';
}


int payTime(int pre, int n, int k)
{
	if(k==1)
		return 1;

	int c=0;
	int t = n/k;
	for(int i=pre;i<=t;i++)
		c += payTime(i,n-i,k-1);
	 
	return c;
}

int GetNum(int n, int k)
{
	int c=0;
	for(int i=1;i<=k;i++)
		c += payTime(1,n,i);
	return c;
}

#define RED true
#define BLK false

struct RB_Node 
{
	int key;
	int data;
	bool color;
	RB_Node *right;
	RB_Node *left;
	RB_Node *parent;
};

class RB_Tree
{
	RB_Node *root;

	bool leftRotate(RB_Node *node)
	{
		return true;
	}
	
	void RB_InsertFixUp( RB_Node *node)
	{

	}

	bool RB_Insert(int key, int data)
	{
		RB_Node *p = root;
		RB_Node *insert_p = nullptr;

		while ( p!= nullptr )
		{
			insert_p = p;
			if(key < p->key ) p = p->left;
			else if(key > p->key) p = p->right;
			else return false;
		}

		RB_Node *insert_node = new RB_Node();
		insert_node->key = key;
		insert_node->data = data;
		insert_node->color = RED;
		insert_node->left = nullptr;
		insert_node->right = nullptr;

		if(insert_p == nullptr)
		{
			root = insert_node;
			root->parent = nullptr;
		}
		else
		{
			if( key < insert_p->key )
				insert_p->left = insert_node;
			else
				insert_p->right = insert_node;
		}

		RB_InsertFixUp(insert_node);
		return true;
}

};

#define  MAX_VERTEX_NUM 10
typedef int InfoType;
struct EdgeBox
{
	int tailvex, headvex;
	EdgeBox *hlink, *tlink;
	InfoType info;
};
typedef int VertexType;
struct VexBox
{
	VertexType data;
	EdgeBox *firstin, *firstout;
};

struct OLGraph
{
	VexBox vlist[MAX_VERTEX_NUM];
	int vexnum, edgenum;
};

bool createDG(OLGraph &G)
{
	cout<<"please enter the vernum and edgenum\n";
	cin>>G.vexnum>>G.edgenum;
	for(int i=0;i<G.vexnum;i++)
	{
		G.vlist[i].data = 0;
		G.vlist[i].firstin = nullptr;
		G.vlist[i].firstout = nullptr;
	}

	for(int k=0;k<G.edgenum;k++)
	{
		EdgeBox *e = new EdgeBox();
		int v1, v2;
		cout<<"please enter the v1 and v2\n";
		cin>>v1>>v2;
		e->headvex = v1;
		e->tailvex = v2;
		e->info = rand()%10;
		e->hlink = G.vlist[v2].firstin;
		e->tlink = G.vlist[v1].firstout;
		G.vlist[v2].firstin = e;
		G.vlist[v1].firstout = e;
	}

	return true;
}

void printDG( OLGraph &G )
{
	for(int i=0; i< G.vexnum; i++)
	{
		cout<<i<<"->";
		EdgeBox *e = G.vlist[i].firstout;
		while (e!=nullptr)
		{
			cout<<e->tailvex<<' ';
			e = e->tlink;
		}
		cout<<'\n';
	}
}
#include <queue>
struct TreeNode
{
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode *parent;
	int num;
	TreeNode(int v)
	{
		val = v;
		left = nullptr;
		right = nullptr;
		parent = nullptr;
		num = 1;
	}

	void print()
	{
		queue<TreeNode*> node_queue;
		node_queue.push(this);
		TreeNode *current = nullptr;
		while ( !node_queue.empty() )
		{
			current = node_queue.front();
			cout<<current->val<<' ';

			node_queue.pop();
			if(current->left!=nullptr)
				node_queue.push(current->left);
			if(current->right!=nullptr)
				node_queue.push(current->right);
		}
	}
	int TreeDepth(TreeNode *root)
	{
		if(root==nullptr)
			return 0;
		return 1 + max(TreeDepth(root->left), TreeDepth(root->right));
	}
	bool isBalanced(TreeNode * t)
	{
		if(t==nullptr)
			return true;
		int d = TreeDepth(t->left) - TreeDepth(t->right);
		if(abs(d) > 1) return false;
		else return isBalanced(t->left) && isBalanced(t->right);
	}
	bool isComplete(TreeNode *root)
	{
		queue<TreeNode*> q;
		q.push(root);
		TreeNode *p = q.front();
		q.pop();
		while (p!=nullptr)
		{
				q.push(p->left);
				q.push(p->right);
				p = q.front(); q.pop();
		}
		while (!q.empty())
		{
			if(q.front()!=nullptr)
				return false;
			q.pop();
		}

		return true;

	}

};

void BinaryInsert(TreeNode *root, int i)
{
	
	TreeNode *p = root;
	TreeNode *pre = p;

	while (p!=nullptr)
	{
		pre = p;

		if( i < p->val )
			p = p->left;
		else if(i > p->val)
			p = p->right;
		else
		{
			p->num ++;
			return;
		}
	}

	TreeNode *t = new TreeNode(i);
	t->val = i;
	t->left = nullptr;
	t->right = nullptr;
	t->num = 1;
	t->parent = pre;

	if(i>pre->val) pre->right = t;
	else pre->left = t;
	
}

TreeNode* FindMax(TreeNode *root)
{
	if(root==nullptr)
		return nullptr;

	TreeNode *p = root;
	while (p->right!=nullptr)
		p = p->right;

	return p;
}

TreeNode* FindMin(TreeNode *root)
{
	if(root==nullptr)
		return nullptr;

	TreeNode *p = root;
	while (p->left!=nullptr)
		p = p->left;

	return p;
}

TreeNode* FindPost(TreeNode *p)
{
	if(p==nullptr)
		return nullptr;
	if(p->right != nullptr)
		return FindMin(p->right);

	TreeNode *t = p->parent;
	while (t!=nullptr && p!=t->left)
	{
		p = t;
		t = t->parent;
	}

	return t;
}

TreeNode *FindPre(TreeNode *p)
{
	if(p==nullptr)
		return nullptr;
	if(p->left != nullptr)
		return FindMax(p->left);

	TreeNode *t = p->parent;
	while (t!=nullptr && p!=t->right)
	{
		p = t;
		t = t->parent;
	}

	return t;
}

int BSTFindKth(int *arr, int n, int k)
{
	TreeNode *root = new TreeNode(arr[0]);
	for(int i=1;i<n;i++)
		BinaryInsert(root, arr[i]);
	
	TreeNode *min_node = root;
	while(min_node->left!=nullptr) min_node = min_node->left;

	for(int i=1;i<k;i++)
	{
		if(min_node==nullptr)
			break;
		min_node = FindPost(min_node);
	}
	if(min_node==nullptr)
		return -1;
	else
		return min_node->val;
}

inline int GetNum2(int n)
{
	//N+1-i
	int i, j, k;
	int sum=0;
	for(i=1;i<=n;i++)
		for(j=1;j<=n;j++)
			for(k=1;k<=n;k++)
			if(j!=i&&k!=j&&k!=i)
			{sum += (n+1-i)*(n+1-j)*(n+1-k);
				cout<<i<<' '<<j<<' '<<k<<'\n';
	}

	//for(i=1;i<=n;i++)
		//sum += (n+1-i)*(n+1-i)*(n+1-i);
	cout<<sum<<' ';
	return sum;
}

#define BITSPERWORD 32  
#define SHIFT 5  
#define MASK 0x1F  
#define NN 10000000  

int a[1 + NN/BITSPERWORD];//申请内存的大小  

//set 设置所在的bit位为1  
void set(int i) {          
	a[i>>SHIFT] |=  (1<<(i & MASK));   
}  
//clr 初始化所有的bit位为0  
void clr(int i) {          
	a[i>>SHIFT] &= ~(1<<(i & MASK));   
}  
//test 测试所在的bit为是否为1  
int  test(int i){   
	return a[i>>SHIFT] &   (1<<(i & MASK));   
}  



template<typename T>
void print(T &t)
{
	cout<<t<<' ';
}
#define  MAX_INT (2147483647)
int atoi2(char *str) // begin with digit or -\+
{
	if(str==nullptr)
		return 0;
	int result=0;
	int signflag=1;

	char t = str[0];
	if(t=='-')
	{	signflag = -1;str++;}
	else if(t=='+')
	{signflag = 1;str++;}

	
	int temp = MAX_INT/10;
	int modnum = MAX_INT %10;
	while ('0'<=*str&&'9'>=*str)
	{
		if(result<temp)
			result = result *10 + *str++-'0';
		else if(result==temp&&(*str-'0')<=modnum)
			result = result *10 + *str++-'0';
		else
			break;
	}
	return result*signflag;
}

void partition123(int *arr, int l, int u, int &p, int&q)
{
	int t = arr[l];
	int i = l+1, lt = l, gt = u;

	while (i<=gt)
	{
		if(arr[i]<t)
		{
			swap(arr[lt++], arr[i++]);
		}
		else if(arr[i]>t)
			swap(arr[i],arr[gt--]);
		else
			i++;
	}
	p = lt;
	q = gt;
}

void quicksort(int *arr, int l, int u)
{
	if(arr==nullptr)
		return;
	if(l>=u)
		return;

	int i, j;
	partition123(arr,l ,u, i ,j);
	quicksort(arr,l,i-1);
	quicksort(arr,j+1, u);
}

void Merge(int *arr, int low, int mid, int high)
{
	vector<int> ivec(arr+low, arr+high+1);
	int i=0, j=mid-low+1;
	int t = low;
	while (i<=mid-low&&j<=high-low)
	{
		if(ivec[i]<=ivec[j])
			arr[t++] = ivec[i++];
		else
			arr[t++] = ivec[j++];
	}
	for(;i<=mid-low;i++)
		arr[t++] = ivec[i];
	for(;j<=high-low;j++)
		arr[t++] = ivec[j];
}

void MergeSort(int *arr, int l, int u)
{
	if(l>=u)
		return;
	int mid = (l+u)/2;
	MergeSort(arr, l, mid);
	MergeSort(arr, mid+1, u);
	Merge(arr, l,mid, u);
}

struct  node
{
	int val;
	node *next;
	node(int v = 0){val = v; next = nullptr;}
	node *add(int v)
	{
		node *t = new node;
		t->val = v;
		t->next = nullptr;
		next = t;
		return t;
	}
	void print()
	{
		node *p = this;
		while (p!=nullptr)
		{
			cout<<p->val<<' ';
			p = p->next;
		}
		cout<<endl;
	}
	friend bool operator==(node &a, node &b)
	{
//		cout<<&a<<' '<<&b<<endl;
		return (&a==&b)? true:false;
	}
};

node *Reverse(node *root)
{
	node *pre = root;
	node *now = root->next;
	node *post = root->next->next;

	root->next = nullptr;
	while (now!=nullptr)
	{
		now->next = pre;
		pre = now;
		now = post;
		if(post!=nullptr)
			post = post->next;
	}
	return pre;
}

void FindNext(char *p, int *next)
{
	next[0] = 0;
	int n = strlen(p);

	for(int i=1;i<n;i++)
	{
		int k = next[i-1];
		while (p[k]!=p[i] && k>0)
			k = next[k-1];
		if(p[k]==p[i])
			next[i] = k + 1;
		else
			next[i] = 0;
	}
}

int KMP(char *pat, char *str)
{
	const int n1 = strlen(str);
	const int n2 = strlen(pat);

	int *next = new int[n1];
	FindNext(pat,  next);

	int i=0, j=0;
	for(; i< n1; i++)
	{
		while (str[i]!=pat[j] && j>0)
			j = next[j-1];
		if(str[i]==pat[j])
			j++;
		if(j==n2)
			return i-n2+1;
	}
	return -1;
}

string LCStr(const string str1, const string str2)
{
	int n1 = str1.length(), n2 = str2.length();
	int *len = new int[n2+1];
	for(int i=0;i<n2+1;i++)
		len[i] = 0;

	int max_len = 0, last_pos = 0;
	for(int i=0;i<n1;i++)
		for(int j=n2;j>0;j--)
		{
			if(str1[i]==str2[j-1])
				len[j] = len[j-1] + 1;
			else
				len[j] = 0;
			if(len[j] > max_len)
			{
				max_len = len[j];
				last_pos = j - 1;
			}
		}
	
	const char *end_pos = str2.c_str() + last_pos + 1;
	const char *start_pos = str2.c_str() + last_pos - max_len +1;
	string s(start_pos, end_pos);
	return s;
}

int max2(int v1, int v2, int v3)
{
	v1 = (v1 > v2)? v1:v2;
	v1 = (v1 > v3)? v1:v3;
	return v1;
}

int FindMaxSubSeq(int *arr, int l, int u)
{
	if(l > u)
		return 0;
	if(l==u)
		return arr[l];

	int m = (l + u) /2;
	int lmax = 0, sum = 0;
	//Find max crossing the left
	for(int i=m;i>=l;i--)
	{
		sum += arr[i];
		lmax = (sum > lmax)? sum:lmax;
	}
	int rmax = 0;
	sum=0;
	for(int i=m+1;i<=u;i++)
	{
		sum += arr[i];
		rmax = (sum > rmax)? sum:rmax;
	}
	return max2(lmax+rmax, FindMaxSubSeq(arr,l,m),FindMaxSubSeq(arr,m+1,u));
}

int FindMax(int *arr, int l, int u)
{
	if(arr==nullptr || l>u)
		return 0;

	int max_so_far = 0, max_ending_here = 0, sum=0;

	for(int i=l;i<=u;i++)
	{
		max_ending_here = max(max_ending_here+arr[i], 0);
		max_so_far = max(max_ending_here, max_so_far);
	}
	return max_so_far;
}

class MinHeap
{
public:
	static void MinHeapFixUp(int *arr, int n, int i)
	{
		int j = (i - 1)/2;
		int t = arr[i];

		while (j>=0&&i!=0)
		{
			if(arr[j] <= t)
				break;
			swap(arr[i], arr[j]);
			arr[j] = arr[i];
			i = j;
			j = (j - 1)/2;
		}
		arr[i] = t;
	}

	static void MinHeapFixDown(int *arr, int n, int i)
	{
		int j = i*2 + 1;
		int t = arr[j];

		while (j<n)
		{
			if(arr[j] >= t )
				break;
			swap(arr[i], arr[j]);
			i = j;
			j = j*2 +1;
		}
		arr[i] = t;
	}

	static void MinHeap_Add(int *arr, int n,int m, int val)
	{
		arr[m] = val;
		MinHeapFixUp(arr,n,m);
	}

	static void Make_MinHeap(int *arr, int n)
	{
		for(int i=0; i<n;i++)
			MinHeap_Add(arr, n, i, arr[i]);
	}
	
};

#include <utility>
int LCSeq(const string &str1, const string &str2)
{
	int n1 = str1.length(),  n2 = str2.length();
	int *len = new int[n2];

	 int **mat = new int *[n1];
	 for(int i=0;i<n1;i++)
		mat[i] = new int[n2];
	for(int i=0;i<n1;i++)
		for(int j=0;j<n2;j++)
			mat[i][j] = 0;

	for(int i=0;i<n2+1;len[i]=0,i++);
	for(int i=0;i<n1;i++)
		for(int j=0;j<n2;j++)
		{
			if(str1[i]==str2[j])
			{
				len[j+1] = len[j] +1;
				mat[i][j] = 1;
			}
			else	if(len[j+1] > len[j])
			{
				mat[i][j] = 2;
			}
			else
			{
				len[j+1] = len[j];
				mat[i][j] = 3;
			}
		}
		int i = n1-1, j = n2-1;
		stack<char> st;
		while (i>=0&&j>=0)
		{
			if(mat[i][j]==1)
			{
				st.push(str1[i]);
				i--;j--;
			}
			else if(mat[i][j]==2)
				i--;
			else
				j--;
		}
		while (!st.empty())
		{
			cout<<st.top();
			st.pop();
		}
		return len[n2];
}

//return index of biggest element that smaller than val
int BSearch(vector<int> arr, int l, int u, int val) 
{
	int i = l, j = u;
	while (i <= j)
	{
		int mid = (i + j)/2;
		if(arr[mid]<=val)
			i = mid + 1;
		else
			j = mid -1;
	}
	return i;
}

int LIS(vector<int> arr, int l, int u)
{
	vector<int> B(u-l+1);
	B.assign(u-l+1, 0);

	B[0] = arr[0];
	int len = 1;
	int i=l;
	for(; l<=u; l++)
	{
		if(arr[l] > B[len-1])
			B[len++] = arr[l];
		else
		{
			int pos = BSearch(arr, 0, len-1, arr[l]);
			B[pos] = arr[l];
		}
	}
	for(; i<=u;i++)
		if(arr[i]<B[len-1])
			cout<<arr[i]<<' ';
	cout<<arr[B[len-1]];
	return len;
}

int coins_num=3;
int coins[] = {1,  5,9};
int MinCoins(int total)
{
	vector<int> Min(total+1, MAX_INT);
	Min[0] = 0;

	for(int i=1; i<= total; i++)
		for(int j=0;j<coins_num;j++)
			if(coins[j] <= i && Min[i-coins[j]] +1 < Min[i])
				Min[i] = Min[i-coins[j]] +1;

	return Min[total];
}

#define  lowbit(x) (x & -x)
void modify(int *arr,int n, int idx, int delta)
{
	while (idx < n)
	{
		arr[idx] += delta;
		idx += lowbit(idx);
	}
}
int GetSum(int *arr, int n, int idx)
{
	int rs = 0;
	while (idx > 0)
	{
		rs += arr[idx];
		idx -= lowbit(idx);
	}
	return rs;
}

void Mirro(TreeNode *t)
{
	if(t==nullptr)
		return;

	swap(t->left, t->right);
	Mirro(t->left);
	Mirro(t->right);
}

int Fabonacci(int n)
{
	int *fab = new int[n+1]();
	fab[0] = 0;
	fab[1] = 1;
	int i = 2;
	while (i<=n)
	{
		fab[i] = fab[i-1] + fab[i-2];
		i++;
	}
	int t = fab[n];
	//cout<<&t<<fab+n;
	delete[] fab;
	return t;
}

int len = 7;
void printsolution(int *arr)
{
	for(int i=0;i<len;i++)
	{
		if(arr[i]!=0)
			cout<<i+1<<' ';
	}
	cout<<endl;
}
void SumCombination(int n, int m, int *flag)
{
	if(n<1 || m < 1)
		return;
	if(m < n)
		n = m;
	if(m==n)
	{
		flag[n-1] = 1;
		printsolution(flag);
		flag[n-1] = 0;
	}
	else
	{
		flag[n-1] = 1;
		SumCombination(n-1, m-n, flag);
		flag[n-1] = 0;
		SumCombination(n-1, m, flag);
	}
}

int LDS(char *str)
{
	if(str==nullptr)
		return -1;
	int max_so_far = 0, max_ending_here = 0;
	for(unsigned int i=0; i<strlen(str); i++)
	{
		if(str[i]>='0'&&str[i] <= '9')
			max_ending_here++;
		else
			max_ending_here = 0;
		max_so_far = max(max_ending_here, max_so_far);
	}
	return max_so_far;
}

void LeftShift(char *str, int n)
{
	int len = strlen(str);
	for(int i=0;i<len;i++)
		swap(str[i], str[len-i-1]);

	for(int i=0;i<len-n;i++)
		swap(str[i],str[len-n-i-1]);

	for(int i=len-n;i<len;i++)
		swap(str[i], str[len-1-(i-len+n)]);
	cout<<str;
}

int GetMaxDistance(TreeNode *t, int &max_left, int &max_right)
{
	if(t == nullptr)
	{
		max_left = 0;
		max_right = 0;
		return 0;
	}
	max_left = 0;
	max_right = 0;
	int maxLL=0, max_LR=0, max_RL=0, max_RR=0;
	int max_Distance_left=0, max_Distance_right=0;
	if(t->left!=nullptr)
	{
		max_Distance_left = GetMaxDistance(t->left, maxLL, max_LR);
		max_left = max(maxLL, max_LR) + 1;
	}

	if(t->right!=nullptr)
	{
		max_Distance_right = GetMaxDistance(t->right, max_RL, max_RR);
		max_right = max(max_RL, max_RR) + 1;
	}
	return max2(max_right + max_left, max_Distance_left, max_Distance_right);
}

bool GetPath(TreeNode *root, TreeNode *t, vector<TreeNode*> &v)
{
	if(root=nullptr)
		return false;
	v.push_back(root);
	if(root==t)
		return true;
	bool found = false;
	found = GetPath(root->left, t, v);
	if(!found)
		found = GetPath(root->right, t, v);
	if(!found)
		v.pop_back();
	return found;
}

void ConvertToList(TreeNode *root, TreeNode * &first, TreeNode * &last)
{
	if(root==nullptr)
	{
		first = nullptr;
		last = nullptr;
		return;
	}
	TreeNode *left_first, *left_last, *right_first, *right_last;
	if(root->left!=nullptr)
		first = root;
	else
	{
		ConvertToList(root->left, left_first, left_last);
		first = left_first;
		root->left = left_last;
		left_last->right = root;
	}
	if(root->right==nullptr)
		last = root;
	else
	{
		ConvertToList(root->right, right_first, right_last);
		root->right = right_first;
		last = right_last;
		right_first->left = root;
	}
	return;
}

TreeNode* GetLCA(TreeNode *r, TreeNode *t1, TreeNode *t2)
{
	if(r==nullptr||t1==nullptr||t2==nullptr)
		return nullptr;
	vector<TreeNode*> v1, v2;
	GetPath(r, t1, v1);
	GetPath(r, t2, v2);
	TreeNode *plast = nullptr;
	vector<TreeNode*>::iterator itor1 = v1.begin(), itor2 = v2.begin();
	while (itor1!=v1.end() && itor2!=v2.end())
	{
		if(*itor1==*itor2)
			plast = *itor1;
		itor1++;
		itor2++;
	}
	return plast;
}

char *MultiBigInt(char *str1, char *str2)
{
	int n1 = strlen(str1), n2 = strlen(str2);
	if(n1<n2)
	{
		swap(str1,str2);
		swap(n1,n2);
	}
	char *result = new char[n1+n2+1]();
	for(int i=0;i<n1+n2;i++)
		result[i] = '0';
	result[n1+n2] = '\0';
	int c = 0,i,j;
	for(i=n2-1;i>=0;i--)
	{
		c=0;
		for(j=n1-1;j>=0;j--)
		{
			int t = (str2[i]-'0')*(str1[j]-'0');
			int v1 = result[i+j+1] + t + c-'0';
			c = v1/10;
			result[i+j+1] = (v1 %10) + '0';
		}
		result[i+j+1] += c;
	}
	return result;
}

#include <stdarg.h>
void printVA(char *first, ...)
{
	va_list v;
	va_start(v, first);
	char * str = first;
	while (str!=nullptr)
	{
		cout<<str<<' ';
		str = va_arg(v, char *);
	}
	va_end(v);
	return;
}
void mystrcat(char *strDest, const char *strSrc)
{
	if(strDest==nullptr || strSrc==nullptr)
		return;

	char *p = strDest;
	while (*p)	p++;
	while (*p++=*strSrc++);
	return;
}

bool isCircle(node *head)
{
	if(head==nullptr)
		return false;
	node *pre = head, *post = head->next;
	while (pre!=nullptr && post!=nullptr)
	{
		if(pre==post)
			return true;
	}
	return false;
}

bool isIntersect(node *h1, node *h2)
{
	while(h1) h1= h1->next;
	while(h2) h2= h2->next;

	if(*h1==*h2)
		return true;
	else
		return false;
}

node * FindFirstNode(node *h1, node *h2)
{
	int c1 = 0, c2 = 0;
	node *p1= h1, *p2 = h2;
	while (h1!=nullptr)
	{
		c1++;
		h1 = h1->next;
	}
	while (h2!=nullptr)
	{
		c2++;
		h2 = h2->next;
	}
	while (c2>c1)
	{
		p2 = p2->next;
		c1++;
	}
	while (c1>c2)
	{
		p1 = p1->next;
		c2++;
	}
	while (p1!=nullptr&&p2!=nullptr)
	{
		if(*p1==*p2)
			return p1;
		p1 = p1->next;
		p2 = p2->next;
	}
	return nullptr;
}

node*  MergeList(node *p1, node *p2)
{
	if(p1==nullptr||p2==nullptr)
		return nullptr;
	node *ptr1 = p1, *ptr2 = p2;
	node *head = new node;
	node *p = head;
	while (ptr1!=nullptr && ptr2!=nullptr)
	{
		if(ptr1->val > ptr2->val)
		{
			p->next = new node(*ptr2);
			ptr2 = ptr2->next;
		}
		else
		{
			p->next = new node(*ptr1);
			ptr1 = ptr1->next;
		}
		p = p->next;
	}
	node *t;
	if(ptr1!=nullptr)
		t = ptr1;
	else
		t = ptr2;
	while (t!=nullptr)
	{
		p->next = new node(*t);
		t = t->next;
		p = p->next;
	}
	return head->next;
}

node *Reversee(node *p)
{
	if(p==nullptr)
		return nullptr;

	node *new_head = p, *old_head = p->next;
	p->next = nullptr;
	while (old_head!=nullptr)
	{
		node *temp = old_head->next;
		old_head->next = new_head;
		new_head = old_head;
		old_head = temp;
	}
	return new_head;
}

int mypartition(int *arr, int l, int u)
{
	int t = arr[l];
	int i=l, j = u+1;
	while (true)
	{
		do 
		{
			i++;
		} while (arr[i]<t&&i<=u);
		do 
		{
			j--;
		} while (arr[j]>t);
		if(i>=j)
			break;
		swap(arr[i], arr[j]);
	}
	swap(arr[l],arr[j]);
	return j;
}
void  myquicksort(int *arr, int l, int u)
{
	stack<int> st;
	st.push(u);
	st.push(l);
	while (!st.empty())
	{
		int i = st.top(); st.pop();
		int j = st.top(); st.pop();
		int mid = mypartition(arr, i, j);
		if(i<mid-1)
		{
			st.push(mid-1);
			st.push(i);
		}
		if(mid+1<j)
		{
			st.push(j);
			st.push(mid+1);
		}
	}
	return;
}

void PreTraverseNoRecurse(TreeNode *r)
{
	stack<TreeNode*> st;
	TreeNode *p=r;
	while ( p!=nullptr || !st.empty() )
	{
		if(p!=nullptr)
		{
			cout<<p->val<<' ';
			st.push(p);
			p = p->left;
		}
		else
		{
			p = st.top()->right;
			st.pop();
		}
	}
}

void PreTraverse2(TreeNode *root)
{
	stack<TreeNode*> st;
	st.push(root);
	while (!st.empty())
	{
		TreeNode *t = st.top();
		st.pop();
		cout<<t->val<<' ';
		if(t->right) st.push(t->right);
		if(t->left) st.push(t->left);
	}
}

void InTraverse(TreeNode *root)
{
	stack<TreeNode *> st;
	TreeNode *p=root;
	while(p!=nullptr || !st.empty())
	{
		if(p!=nullptr)
		{
			st.push(p);
			p = p->left;
		}
		else
		{
			p = st.top();
			st.pop();
			cout<<p->val<<' ';
			p = p->right;
		}
	}
}

void PostTraverse(TreeNode *root)
{
	stack< pair<TreeNode *,bool> > st;
	st.push(make_pair(root, false));
	TreeNode *p;
	while (!st.empty())
	{
		pair<TreeNode*,bool>	pr = st.top();
		p = pr.first;
		st.pop();
		if(!pr.second)
		{
			st.push(make_pair(p,true));
			if(p->right) st.push(make_pair(p->right,false));
			if(p->left) st.push(make_pair(p->left,false));
		}
		else
		{
			cout<<p->val<<' ';
		}
	}
}

void TraverseByLevel(TreeNode *root)
{
	TreeNode *p = root;
	queue<TreeNode*> q;
	q.push(p);
	while (!q.empty())
	{
		p = q.front();
		q.pop();
		cout<<p->val<<' ';
		if(p->left) q.push(p->left);
		if(p->right) q.push(p->right);
	}
}

#include <windows.h>
HANDLE hMutex;
int tickets = 100;
DWORD WINAPI Func1Proc(LPVOID lpParameter)
{
	while (true)
	{
		//ReleaseMutex(hMutex);
		WaitForSingleObject(hMutex, INFINITE);
		if(tickets > 0)
		{
			Sleep(1000);
			cout<<"thread1 sold ticket: "<<tickets--<<endl;
		}
		else
			break;
		ReleaseSemaphore(hMutex, 1, NULL );
	}
	return 0;
}
DWORD WINAPI Func2Proc(LPVOID lpParameter)
{
	while (true)
	{
		//ReleaseMutex(hMutex);
		WaitForSingleObject(hMutex, INFINITE);
		if(tickets > 0)
		{
			Sleep(1000);
			cout<<"thread2 sold ticket: "<<tickets--<<endl;
		}
		else
			break;
		ReleaseSemaphore(hMutex, 1, NULL);
	}
	return 0;
}
char mychar;
HANDLE MutexABC[3];
HANDLE not_read[3];
HANDLE write_yet;
DWORD WINAPI FuncA(LPVOID lpParameter)
{
	while (true)
	{
		WaitForMultipleObjects(3, MutexABC, true, INFINITE);
		mychar = 'a' + rand()%40;
		ReleaseSemaphore(not_read[0],1,NULL);
		ReleaseSemaphore(not_read[1], 1, NULL);
		ReleaseSemaphore(not_read[2], 1, NULL);
		//Sleep(1000);
	}
	return 0;
}
DWORD WINAPI FuncB(LPVOID lpPamameter)
{
	while(true)
	{
		WaitForSingleObject(not_read[0], INFINITE);
		cout<<mychar<<endl;
		Sleep(1000);
		ReleaseSemaphore(MutexABC[0], 1, NULL);
	}
	return 0;
}
DWORD WINAPI FuncC(LPVOID lpPamameter)
{
	while(true)
	{		
		WaitForSingleObject(not_read[1], INFINITE);
		cout<<mychar<<endl;

		ReleaseSemaphore(MutexABC[1], 1, NULL);
	}
	return 0;
}
DWORD WINAPI FuncD(LPVOID lpPamameter)
{
	while (true)
	{
		WaitForSingleObject(not_read[2], INFINITE);
		cout<<mychar<<endl;
		ReleaseSemaphore(MutexABC[2], 1, NULL);
	}
	return 0;
}
/*
hMutex = CreateMutex(NULL, false, "ticket");
hMutex = CreateSemaphore(NULL, 2,2,"abc");\
ReleaseMutex(hMutex);
WaitForMultipleObjects(4, h, true, INFINITE);*/
void MirroNoRecurse(TreeNode *root)
{
	TreeNode *p = root;
	stack<TreeNode *> st;
	st.push(p);
	while (!st.empty())
	{
		p = st.top();
		st.pop();
		TreeNode *t;
		t = p->right;
		p->right = p->left;
		p->left = t;
		if(p->left!=nullptr) st.push(p->left);
		if(p->right!=nullptr) st.push(p->right);
	}
}

void printAllCombination(char *str, int i, int n)
{
	if(i==n-1)
	{
		for_each(str, str + n, print<char>);
		cout<<endl;
		return;
	}
	else
	{
		for(int k=i;k<n;k++)
		{
			swap(str[k], str[i]);
			printAllCombination(str, i+1, n);
			swap(str[k], str[i]);
		}
	}
}

void GetNextCombia(char *str, int n)
{
	int j = n-2;
	while (str[j]>=str[j+1] && j>=0)
	{
		--j;
	}
	if(j<0)
		return;
	int i = n-1;
	while (str[j]>=str[i])
	{
		--i;
	}
	swap(str[i],str[j]);
	j++; i = n-1;
	while (j<i)
	{
		swap(str[j++], str[i--]);
	}
	cout<<str<<endl;
}

class base{
private: int i;
public: base(int x){i=x;}
operator char*(){}
};

TreeNode * ReConstructTree(int *inorder, int i, int *preorder, int j, int n)
{
	if(n==0)		return nullptr;
	TreeNode *pat = new TreeNode(preorder[j]);
	int in = i;
	while (inorder[in]!=preorder[j]) in++;
	int len = in - i;
	TreeNode *left = ReConstructTree(inorder, i,preorder,j+1,len);
	TreeNode *right = ReConstructTree(inorder, in+1,preorder,j+len+1, n-len-1);
	if(left!=nullptr)		pat->left = left;
	if(right!=nullptr)	pat->right = right;
	return pat;
}

bool isPalindomes(int val)
{
	int i = 0, j = val;
	while (j)
	{
		i =i*10 + j%10;
		j /= 10;
	}
	if(i==val)
		return true;
	return false;
}

class X
{
public:
	X& operator=(const X& rhs){cout<<"==\n"; return *this;}
	const X& operator+(const X& rhs) const{cout<<"F const\n"; return rhs;}
	const X& operator+(int m){cout<<"F\n";return *this;}
private:
	int n;
};

#define THE_MACRO(x)\
   (x=((0xaaaaaaaa&x)>>1)+(0x55555555&x),\
	x=((0xcccccccc&x)>>2)+(0x33333333&x),\
	x=((0xf0f0f0f0&x)>>4)+(0x0f0f0f0f&x),\
	x=((0xff00ff00&x)>>8)+(0x00ff00ff&x),\
	x=(x>>16)+(0x0000ffff&x))

class Base_J
{
	int x;
public:
	Base_J(int n=0):x(n){ cout<<n;}
	virtual void F(){cout<<"func in base\n";}
};

class Derived_J:public Base_J
{
	int y;
public:
	Derived_J(int m, int n):y(m), Base_J(n) {cout<<m;}
	Derived_J(int m):y(m){cout<<m;}
	void F(){cout<<"func in derived\n";}
};

bool isIllegal(int *arr, int n)
{
	int *p = arr;
	int t=MAX_INT;
	for (int i=0;i<n;i++)
		for(int j=i+1,t=arr[i];j<n;j++)
		{
			if(arr[j] < arr[i])
				if(arr[j] < t)
					t = arr[j];
				else
					return false;
		}
	return true;
}

void GetMaxAndMin(TreeNode *root, int &max_dep, int &min_dep)
{
	if(root==nullptr)
	{
		max_dep = 0;
		min_dep = 0;
		return;
	}
	int max_left, min_left, max_right, min_right;
	GetMaxAndMin(root->left, max_left, min_left);
	GetMaxAndMin(root->right, max_right, min_right);
	max_dep = max(max_left, max_right) +1;
	min_dep = min(min_left, min_right)+1;
	return;
}

int removeDuplicateValue(node *root)
{
	
	node *pre = root;
	node *p = root->next;

	std::set<int> hs;
	hs.insert(root->val);
	int c = 0;
	while (p!=nullptr)
	{
		if(hs.find(p->val)==hs.end())
		{ 
			hs.insert(p->val);
			pre = p;
			p = p->next;
		}
		else
		{
			pre->next = p->next;
			delete p;
			p = pre->next;
			c++;
		}
	}
	return c;
}

void Hanrio(int n, int start, int temp, int end)
{
	if(n==1)
		cout<<start<<"->"<<end<<endl;
	else
	{
		Hanrio(n-1, start, end, temp);
		Hanrio(1, start, temp, end);
		Hanrio(n-1, temp, start, end);
	}
}

void HanrioNoRec(int n)
{
	struct mystate
	{
		mystate(int v1,int v2, int v3, int v4)
		{n=v1;start=v2;temp=v3;end = v4;}
		mystate(){}
		int n, start, temp, end;
	};
	mystate current_s;
	stack<mystate> st;
	st.push(mystate(n,1,2,3));
	while (!st.empty())
	{
		current_s = st.top();
		st.pop();
		if(current_s.n==1)
			cout<<current_s.start<<"->"<<current_s.end<<endl;
		else
		{
			int v1=current_s.n, v2=current_s.start,v3=current_s.temp,v4=current_s.end;
			st.push(mystate(v1-1,v3,v2,v4));
			st.push(mystate(1,v2,v3,v4));
			st.push(mystate(v1-1,v2,v4,v3));
			
		}
	}
}

int xx = 0;
int parti(int *arr, int l, int u)
{
	if(arr==nullptr|| l>=u)
		return l;
	int i=l, j = u+1, t = arr[l];
	while (true)
	{
		do 
		{
			i++;
		} while (arr[i]>t&&i<=u);
		do 
		{
			j--;
		} while (arr[j]<t);
		if(i>=j)
			break;
		swap(arr[i],arr[j]);
		xx++;
	}
	swap(arr[l], arr[j]);
	return j;
}
int yy=0;
void quicks(int *arr, int l, int u)
{
	if(arr==nullptr || l>=u)
		return;
	stack<int> st;
	st.push(l);
	st.push(u);
	while (!st.empty())
	{
		int j = st.top();st.pop();
		int i = st.top();st.pop();
		if(i>=j)
			continue;
		int mid = parti(arr, i, j);
		st.push(i);
		st.push(mid-1);
		st.push(mid+1);
		st.push(j);
	}
	/*int mid = parti(arr, l, u);
	quicks(arr, l, mid-1);
	quicks(arr, mid+1 ,u);*/
	yy++;
}

void ThreePartition(int *arr, int l, int u, int &lt, int &gt)
{
	if(arr==nullptr || l>=u)
		return;
	lt = l;
	gt = u;
	int i = l+1, t = arr[l];
	while (i<=gt)
	{
		if(arr[i]<t)
			swap(arr[lt++],arr[i++]);
		else if(arr[i]>t)
			swap(arr[gt--],arr[i]);
		else
			i++;
	}
}
void superquick(int *arr, int l, int u)
{
	if(arr==nullptr || l>=u)
		return;
	int lt, gt;
	ThreePartition(arr, l, u, lt, gt);
	superquick(arr,l,lt-1);
	superquick(arr,gt+1, u);
}

node * FindCircleNode1(node *r)
{
	std::set<node*> st;
	node *p = r;
	while (p!=nullptr)
	{
		if(st.find(p)!=st.end())
			return p;
		else
			st.insert(p);
		p = p->next;
	}
	return nullptr;
}

node *FindCircleNode2(node *r)
{
	node *slow = r, *fast = r->next, *pre = r;
	while (slow!=fast)
	{
		slow = slow->next;
		pre = fast->next;
		fast = fast->next->next;
	}
	pre->next = nullptr;
	node *newhead = slow;
	int c1=0, c2 = 0;
	node *h1=r, *h2 = newhead;
	while(h1!=nullptr)
	{
		c1++;
		h1=h1->next;
	}
	while(h2!=nullptr)
	{
		c2++;
		h2 = h2->next;
	}
	h1=r;
	h2 = newhead;
	while(c1>c2)
	{
		h1 = h1->next;
		c1--;
	}
	while(c1<c2)
	{
		h2 = h2->next;
		c2--;
	}
	while (h1!=h2)
	{
		h1=h1->next;
		h2=h2->next;
	}
	pre->next = slow;
	return h1;
}

#define LEN 8//败者树容量，多路归并数目
#define MIN -1//所有数据的可能最小值

int ls[LEN+1];//败者树,ls[0]存放胜者，其余存放败者
int buf[LEN+1];//存放多路归并的头元素值,多出来的一位放MIN

void adjust(int i, int *buf)//buf[i]
{
	int t = (i+LEN) / 2;
	while (t>0)
	{
		if(buf[i] > buf[ls[t]])
			swap(ls[t], i);
		t /= 2;
	}
	ls[0] = i;
}
void build(int *buf)
{
	buf[LEN] = MIN;
	for(int i=0;i<LEN+1;i++)
		ls[i] = LEN;
	for(int i=0;i<LEN;i++)
		adjust(i, buf);
}

void FindNext2(const char *pat, int *next)
{
	if(pat==nullptr)
		return;
	next[0] = 0;
	int k, n = strlen(pat);
	for(int i=1;i<n;i++)
	{
		k = next[i-1];
		while(pat[i]!=pat[k] && k>0)
			k = next[k-1];
		if(pat[i]==pat[k])
			next[i] = k+1;
		else
			next[i] = 0;
	}
}

int KMP2(char *pat, char *str)
{
	int len_pat = strlen(pat), len_str = strlen(str);
	int *next = new int[len_pat];
	FindNext2(pat, next);
	int i=0, j=0;
	for(;i<len_str;i++)
	{
		while(str[i]!=pat[j] && j>0)
			j = next[j-1];
		if(str[i]==pat[j])
			j++;
		if(j==len_pat)
			return i-len_pat+1;
	}
	return -1;
}

bool Reverse2(char *str, int l, int u)
{
	int len = strlen(str);
	if(str==nullptr || l>u || u>=len)
		return false;
	while(l<u)
		swap(str[l++], str[u--]);
	return true;
}
void ReverseWord2(char *str)
{
	char *p = str;
	int i=0,j=0;
	while (*p!='\0')
	{

	}
}

int gcd(int x,int y) 
{ 
	int m;
if(x<y)
	return gcd(y,x);
if(x%y!=0)
	return gcd(y,x%y);
else return y;
}

typedef long long bigint;

void addmy(bigint x1,bigint y1,bigint x2,bigint y2,bigint &x, bigint &y)
{
	y = y1*y2;
	x = x1*y2 + x2*y1;
	x1 = gcd(x,y);
	x /= x1;
	y /= x1;
}

void cacul(string &str, bigint &x, bigint &y)
{
	const char *p = str.c_str();
	x = 0;y=0;
	bool flag = false;
	while (*p!='\0')
	{
		if(*(p)=='/')
		{
			flag = true;
			p++;
			continue;
		}
		if(!flag)
			x = x*10 + *p-'0';
		else
			y = y*10 + *p-'0';
		p++;
	}
}


int main()
{

	ifstream iff("A-small-attempt0.in");
	ofstream off("b.txt");
	int n;
	iff>>n;
	string str;
	bigint x, y;
	for(int i=1;i<=n;i++)
	{
		iff>>str;
		cacul(str, x, y);
		if(x>y)
			off<<"Case #"<<i<<': '<<"impossible"<<endl;
			//off<<"Case #"<<i<<': ';
		bigint t = gcd(x,y);
		x/=t;
		y /= t;
	    std::bitset<64> mybt(y);
		int cc=0;
		for(int k=0;k<64;k++)
			if(mybt[k]==1)
				cc++;
		if(cc==1)
		{int c1=0;
		while (x<y&&c1<41)
		{
			x *= 2;
			c1++;
		}

		if(c1<41)
			off<<"Case #"<<i<<": "<<c1<<endl;
		else
			off<<"Case #"<<i<<": impossible"<<endl;
		}else
		{
			off<<"Case #"<<i<<": impossible"<<endl;
		}
	}
	//system("pause");

} 
