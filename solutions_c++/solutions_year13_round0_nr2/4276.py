#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <math.h>
using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int,int> ii;
typedef vector<ii> vii;
#define sz(a) int((a).size())
#define all(c) (c).begin(),(c).end()
#define loop(i,n) for(int i=0; i<(n); i++)
#define tr(it,c) for(it=(c).begin(); it!=(c).end(); it++)
#define tr2(it1,c,it2,d) for(it1=(c).begin(),it2=(d).begin(); it1!=(c).end(); it1++,it2++)

template <class T>
class BSTNode
{
private:
	static const size_t UNIT=1024;
	static BSTNode<T>* FREELIST;
	static BSTNode<T>* MEMLIST;
	BSTNode<T> *left, *right, *parent;
	size_t size;
	T value;
	static BSTNode<T>* BSTAllocate();
public:
	void* operator new(size_t size);
	void operator delete(void* p);
	static void Init();
	static void Release();
	static BSTNode<T>* ConstructBST(size_t s);
	BSTNode(){}
	BSTNode(BSTNode<T>* l, BSTNode<T>* r, BSTNode<T>* p, size_t s, T v)
		:left(l), right(r), parent(p), size(s), value(v){}
	inline void SetParent(BSTNode<T>* p=NULL){parent = p;}
	void DeleteAll();
	BSTNode<T>* GetIndex(size_t pos);
	T& GetValueAt(size_t pos);
	void insert(size_t pos, T value);
	void erase(BSTNode<T>*& root, size_t pos);
};

template <class T>
BSTNode<T>* BSTNode<T>::FREELIST=NULL;
template <class T>
BSTNode<T>* BSTNode<T>::MEMLIST=NULL;

template <class T>
BSTNode<T>* BSTNode<T>::BSTAllocate()
{
	BSTNode<T>* q = (BSTNode<T>*)malloc(sizeof(BSTNode<T>));
	BSTNode<T>* p = (BSTNode<T>*)malloc(UNIT*sizeof(BSTNode<T>));
	for(size_t i=0; i<UNIT-1; i++)
		(p+i)->left = p+i+1;
	(p+UNIT-1)->left = NULL;
	q->left = MEMLIST;
	q->right = p;
	MEMLIST = q;
	return p;
}

template <class T>
void BSTNode<T>::Init()
{
	FREELIST = BSTAllocate();
}

template <class T>
void BSTNode<T>::Release()
{
	BSTNode<T> *p, *q;
	q = MEMLIST;
	while(q)
	{
		p = q->left;
		free(q->right);
		free(q);
		q = p;
	}
	FREELIST = NULL;
	MEMLIST = NULL;
}

template <class T>
void* BSTNode<T>::operator new(size_t size)
{
	if(FREELIST == NULL)
		FREELIST = BSTAllocate();
	BSTNode<T>* p = FREELIST;
	FREELIST = FREELIST->left;
	return p;
}

template <class T>
void BSTNode<T>::operator delete(void* p)
{
	((BSTNode<T>*)p)->left = FREELIST;
	FREELIST = (BSTNode<T>*)p;
}

template <class T>
BSTNode<T>* BSTNode<T>::ConstructBST(size_t s)
{
	if(s == 0)
		return NULL;
	BSTNode<T>* p = new BSTNode<T>;
	p->size = s;
	BSTNode<T>* q;
	if(s >= 2)
		q = ConstructBST(s/2);
	else
		q = NULL;
	p->left = q;
	if(q) q->parent = p;
	if(s >= 3)
		q = ConstructBST((s-1)/2);
	else
		q = NULL;
	p->right = q;
	if(q) q->parent = p;
	return p;
}

template <class T>
void BSTNode<T>::DeleteAll()
{
	if(left)
		left->DeleteAll();
	if(right)
		right->DeleteAll();
	delete this;
}

template <class T>
BSTNode<T>* BSTNode<T>::GetIndex(size_t pos)
{
	if(pos >= size)
		throw("Out of Dynamic Array Index Bound");
	BSTNode<T>* p = this;
	while(1)
	{
		size_t base = (p->left) ? p->left->size : 0;
		if(pos > base)
		{
			p = p->right;
			pos -= (base+1);
		}
		else if(pos < base)
			p = p->left;
		else
			break;
	}
	return p;
}

template <class T>
T& BSTNode<T>::GetValueAt(size_t pos)
{return GetIndex(pos)->value;}

template <class T>
void BSTNode<T>::insert(size_t pos, T value)
{
	BSTNode<T>* p;
	if(pos == size)
	{
		p = this;
		while(p->right)
			p = p->right;
		p->right = new BSTNode<T>(NULL, NULL, p, 1, value);
	}
	else
	{
		p = GetIndex(pos);
		if(p->left == NULL)
			p->left = new BSTNode<T>(NULL, NULL, p, 1, value);
		else
		{
			p = p->left;
			while(p->right)
				p = p->right;
			p->right = new BSTNode<T>(NULL, NULL, p, 1, value);
		}
	}
	while(p)
	{
		p->size++;
		p = p->parent;
	}
}

template <class T>
void BSTNode<T>::erase(BSTNode<T>*& root, size_t pos)
{
	BSTNode<T> *p = GetIndex(pos);
	BSTNode<T> *q, *r;
	if(p->left==NULL && p->right==NULL)
	{
		q = p->parent;
		if(q->left==p)
			q->left = NULL;
		else
			q->right = NULL;
	}
	else if(p->left==NULL || p->right==NULL)
	{
		q = p->parent;
		r = (p->left==NULL) ? p->right : p->left;
		if(q == NULL)
			root = r;
		else if(q->left==p)
			q->left = r;
		else
			q->right = r;
		r->parent = q;
	}
	else
	{
		BSTNode<T>* t;
		if(p->right->size > p->left->size)
		{
			r = p->right;
			while(r->left)
				r = r->left;
			t = r->right;
		}
		else
		{
			r = p->left;
			while(r->right)
				r = r->right;
			t = r->left;
		}
		p->value = r->value;
		q = r->parent;
		if(r == q->right)
			q->right = t;
		else
			q->left = t;
		if(t)
			t->parent = q;
		p = r;
	}
	delete p;
	while(q)
	{
		q->size--;
		q = q->parent;
	}
}

template <class T>
class DynamicArray
{
private:
	static size_t DAINUSE;
	BSTNode<T> *root;
	size_t usize;
public:
	DynamicArray(size_t s=0);
	~DynamicArray();
	void insert(size_t pos, T value);
	void erase(size_t pos);
	T& operator[](size_t pos);
	void clear();
	inline size_t size()const{return usize;}
};

template <class T>
size_t DynamicArray<T>::DAINUSE=0;

template <class T>
DynamicArray<T>::DynamicArray(size_t s=0):usize(s)
{
	if(DAINUSE==0)
		BSTNode<T>::Init();
	DAINUSE++;
	root = BSTNode<T>::ConstructBST(s);
	if(root)
		root->SetParent(NULL);
}

template <class T>
DynamicArray<T>::~DynamicArray()
{
	DAINUSE--;
	if(root)
		root->DeleteAll();
	if(DAINUSE == 0)
		BSTNode<T>::Release();
}

template <class T>
void DynamicArray<T>::insert(size_t pos, T value)
{
	if(usize == 0)
	{
		root = BSTNode<T>::ConstructBST(1);
		root->GetValueAt(pos) = value;
	}
	else
		root->insert(pos, value);
	usize++;
}

template <class T>
void DynamicArray<T>::erase(size_t pos)
{
	if(usize == 1)
		clear();
	else
	{
		root->erase(root, pos);
		usize--;
	}
}

template <class T>
T& DynamicArray<T>::operator[](size_t pos)
{return root->GetValueAt(pos);}

template <class T>
void DynamicArray<T>::clear()
{
	root->DeleteAll();
	root = NULL;
	usize = 0;
}

class IntArray
{
private:
	DynamicArray<int> *da;
public:
	void init(size_t s) {da = new DynamicArray<int>(s);}
	void clear() {delete da;}
	int& operator[](size_t pos) {return da->operator [] (pos);}
	void insert(size_t pos, int value) {return da->insert(pos, value);}
	void erase(size_t pos) {return da->erase(pos);}
};

string solveHelper(IntArray *board, int r, int c, set<pair<int, ii> > &S, int *convr, int *convc)
{
	if(r == 1 || c == 1)
		return "YES";
	int minHeight = S.begin()->first;
	int minr = S.begin()->second.first;
	int minc = S.begin()->second.second;

	loop(i, r) if(convr[i] == minr) {
		minr = i;
		break;
	}
	loop(j, c) if(convc[j] == minc) {
		minc = j;
		break;
	}

	bool straightRow = true;
	loop(j, c) if(board[minr][j] != minHeight)
		straightRow = false;

	bool straightCol = true;
	loop(i, r) if(board[i][minc] != minHeight)
		straightCol = false;

	if(straightRow) {
		loop(j, c)
			S.erase(make_pair(minHeight, ii(convr[minr], convc[j])));
		for(int i=minr; i<r-1; i++) {
			board[i] = board[i+1];
			convr[i] = convr[i+1];
		}
		return solveHelper(board, r-1, c, S, convr, convc);
	} else if(straightCol) {
		loop(i, r) {
			S.erase(make_pair(minHeight, ii(convr[i], convc[minc])));
			board[i].erase(minc);
		}
		for(int j=minc; j<c-1; j++)
			convc[j] = convc[j+1];
		return solveHelper(board, r, c-1, S, convr, convc);
	} else
		return "NO";
}

string solve(IntArray *board, int r, int c)
{
	IntArray *boardHelper = new IntArray[r];
	loop (i, r)
		boardHelper[i] = board[i];

	set<pair<int, ii> > S;
	loop (i, r) loop (j, c)
		S.insert(make_pair(board[i][j], ii(i, j)));

	int *convr = new int[r];
	int *convc = new int[c];
	loop(i, r) convr[i] = i;
	loop(j, c) convc[j] = j;

	string answer = solveHelper(boardHelper, r, c, S, convr, convc);

	loop(i, r)
		board[i].clear();
	delete board;
	delete boardHelper;
	delete convr;
	delete convc;
	return answer;
}

void preprocess(){}

void readinput(IntArray * &board, int &r, int &c)
{
	cin>>r>>c;
	board = new IntArray[r];
	loop(i, r) {
		board[i].init(c);
		loop(j, c)
			cin>>board[i][j];
	}
}

vs getoutput()
{
	IntArray *board;
	int r, c;
	readinput(board, r, c);
	string answer = solve(board, r, c);
	return vs(1, answer);
}

void main()
{
//	freopen("in.txt", "r", stdin); freopen("out.txt", "w", stdout);
//	freopen("test\\B-small-attempt0.in", "r", stdin);freopen("test\\B-small-attempt0.out", "w", stdout);
	freopen("test\\B-large.in", "r", stdin);freopen("test\\B-large.out", "w", stdout);
	int testcase;
	cin>>testcase;
	preprocess();
	for(int i=1; i<=testcase; i++)
	{
		cout<<"Case #"<<i<<": ";
		vs answer = getoutput();
		loop(j, sz(answer))
			cout<<answer[j]<<endl;
	}
	fclose(stdin);
	fclose(stdout);
}