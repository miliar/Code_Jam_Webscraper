#include <string>
#include <vector>
#include <algorithm>
#include <numeric>
#include <set>
#include <map>
#include <queue>
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstring>
#include <cctype>
#include <cassert>
#include <limits>
#include <functional>

#include <thread>
#include <mutex>

#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
#if defined(_MSC_VER) || __cplusplus > 199711L
#define aut(r,v) auto r = (v)
#else
#define aut(r,v) __typeof(v) r = (v)
#endif
#define each(it,o) for(aut(it, (o).begin()); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define pb(x) push_back(x)
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f
#define INFL 0x3f3f3f3f3f3f3f3fLL
using namespace std;
typedef vector<int> vi; typedef pair<int,int> pii; typedef vector<pair<int,int> > vpii; typedef long long ll;
template<typename T, typename U> inline void amin(T &x, U y) { if(y < x) x = y; }
template<typename T, typename U> inline void amax(T &x, U y) { if(x < y) x = y; }


#ifdef WIN32
extern "C" int __stdcall QueryPerformanceFrequency(long long*);
extern "C" int __stdcall QueryPerformanceCounter(long long*);
double getTime() {
	long long c, freq;
	QueryPerformanceCounter(&c);
	QueryPerformanceFrequency(&freq);
	return c * 1. / freq;
}
#else
#include <sys/time.h>
double getTime() {
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec / 1e6;
}
#endif

struct TimeIt {
	double c1;
	const char *msg;

	TimeIt(const char *msg_): msg(msg_) {
		c1 = getTime();
	}
	~TimeIt() {
		double c2 = getTime();
		fprintf(stderr, "%s: %.6f sec.\n", msg, c2 - c1);
	}

	operator bool() { return false; }	//if(TimeIt _ = "msg");else で宣言する用
};
#define TIMEIT(s) if(TimeIt timeit_##__LINE__ = s); else

struct Xor128 {
	unsigned x, y, z, w;
	Xor128(): x(123456789), y(362436069), z(521288629), w(88675123) { }
	unsigned next() {
		unsigned t = x ^ (x << 11);
		x = y; y = z; z = w;
		return w = w ^ (w >> 19) ^ (t ^ (t >> 8));
	}
	//手抜き
	inline unsigned next(unsigned n) { return next() % n; }
};
 
template<typename Node>
struct BottomupTreap {
	Xor128 rng;
	typedef Node *Ref;
	static int size(Ref t) { return !t ? 0 : t->size; }
 
	unsigned nextRand() { return rng.next(); }
private:
	bool choiceRandomly(Ref l, Ref r) {
		return l->priority < r->priority;
	}
public:
 
	Ref join(Ref l, Ref r) {
		if(!l) return r;
		if(!r) return l;
 
		Ref t = NULL;
		unsigned long long dirs = 0;
		int h;
		for(h = 0; ; ++ h) {
			if(h >= sizeof(dirs)*8 - 2) {
				//dirsのオーバーフローを防ぐために再帰する。
				//あくまでセーフティガードなのでバランスは多少崩れるかもしれない
				t = join(l->right, r->left);
				dirs = dirs << 2 | 1;
				h ++;
				break;
			}
			dirs <<= 1;
			if(choiceRandomly(l, r)) {
				Ref c = l->right;
				if(!c) {
					t = r;
					r = r->parent;
					break;
				}
				l = c;
			}else {
				dirs |= 1;
				Ref c = r->left;
				if(!c) {
					t = l;
					l = l->parent;
					break;
				}
				r = c;
			}
		}
		for(; h >= 0; -- h) {
			if(!(dirs & 1)) {
				Ref p = l->parent;
				t = l->linkr(t);
				l = p;
			}else {
				Ref p = r->parent;
				t = r->linkl(t);
				r = p;
			}
			dirs >>= 1;
		}
		return t;
	}
 
	typedef std::pair<Ref,Ref> RefPair;
 
	//l＜t≦rの(l,r)に分割する
	RefPair split2(Ref t) {
		Ref p, l = t->left, r = t;
		Node::cut(l); t->linkl(NULL);
		while(p = t->parent) {
			t->parent = NULL;
			if(p->left == t)
				r = p->linkl(r);
			else
				l = p->linkr(l);
			t = p;
		}
		return RefPair(l, r);
	}
	//l＜t＜rの(l,t,r)に分割する。(l,r)を返す
	RefPair split3(Ref t) {
		Ref p, l = t->left, r = t->right;
		Node::cut(l), Node::cut(r);
		t->linklr(NULL, NULL);
		while(p = t->parent) {
			t->parent = NULL;
			if(p->left == t)
				r = p->linkl(r);
			else
				l = p->linkr(l);
			t = p;
		}
		return RefPair(l, r);
	}
	Ref cons(Ref h, Ref t) {
		assert(size(h) == 1);
		if(!t) return h;
		Ref u = NULL;
		while(true) {
			if(choiceRandomly(h, t)) {
				Ref p = t->parent;
				u = h->linkr(t);
				t = p;
				break;
			}
			Ref l = t->left;
			if(!l) {
				u = h;
				break;
			}
			t = l;
		}
		while(t) {
			u = t->linkl(u);
			t = t->parent;
		}
		return u;
	}
};
 
class EulerTourTreeWithMarks {
	struct Node {
		typedef BottomupTreap<Node> BST;
 
		Node *left, *right, *parent;
		int size;
		unsigned priority;
		int val, sum;
 
		Node(): left(NULL), right(NULL), parent(NULL),
			size(1), priority(0), val(0), sum(0) { }
 
		inline Node *update() {
			int size_t = 1; int sum_t = val;
			if(left) {
				size_t += left->size;
				sum_t += left->sum;
			}
			if(right) {
				size_t += right->size;
				sum_t += right->sum;
			}
			size = size_t, sum = sum_t;
			return this;
		}
 
		inline Node *linkl(Node *c) {
			if(left = c) c->parent = this;
			return update();
		}
		inline Node *linkr(Node *c) {
			if(right = c) c->parent = this;
			return update();
		}
		inline Node *linklr(Node *l, Node *r) {
			if(left = l) l->parent = this;
			if(right = r) r->parent = this;
			return update();
		}
		static Node *cut(Node *t) {
			if(t) t->parent = NULL;
			return t;
		}
 
		static const Node *findRoot(const Node *t) {
			while(t->parent) t = t->parent;
			return t;
		}
		static std::pair<Node*,int> getPosition(Node *t) {
			int k = BST::size(t->left);
			Node *p;
			while(p = t->parent) {
				if(p->right == t)
					k += BST::size(p->left) + 1;
				t = p;
			}
			return std::make_pair(t, k);
		}
		static const Node *findHead(const Node *t) {
			while(t->left) t = t->left;
			return t;
		}
		static void updatePath(Node *t) {
			while(t) {
				t->update();
				t = t->parent;
			}
		}
	};
 
	typedef Node::BST BST;
	BST bst;
 
	std::vector<Node> nodes;
	//各頂点に対してその頂点から出ているarcを1つだけ代表として持つ(無い場合は-1)
	//逆にarcに対して対応する頂点はたかだか1つである
	std::vector<int> firstArc;
	//辺・頂点に対する属性
	std::vector<int> vertexVal;
 
	inline int getArcIndex(const Node *a) const { return a - &nodes[0]; }
 
	inline int arc1(int ei) const { return ei; }
	inline int arc2(int ei) const { return ei + (numVertices() - 1); }
 
public:
	inline int numVertices() const { return firstArc.size(); }
	inline int numEdges() const { return numVertices() - 1; }
 
	inline int getVertexVal(int v) const {
		return vertexVal[v];
	}
private:
 
	void updateSums(int a, int v) {
		Node *t = &nodes[a];
		t->val = v == -1 ? 0 : getVertexVal(v);
		Node::updatePath(t);
	}
 
	//firstArcの変更に応じて更新する
	void firstArcChanged(int v, int a, int b) {
		if(a != -1) updateSums(a, -1);
		if(b != -1) updateSums(b, v);
	}
 
public:
	class TreeRef {
		friend class EulerTourTreeWithMarks;
		const Node *ref;
	public:
		TreeRef() { }
		TreeRef(const Node *ref_): ref(ref_) { }
		bool operator==(const TreeRef &that) const { return ref == that.ref; }
		bool operator!=(const TreeRef &that) const { return ref != that.ref; }
		bool isIsolatedVertex() const { return ref == NULL; }
	};
 
	void init(int N) {
		int M = N - 1;
		firstArc.assign(N, -1);
		nodes.assign(M * 2, Node());
		for(int i = 0; i < M * 2; i ++)
			nodes[i].priority = bst.nextRand();
		vertexVal.assign(N, 0);
	}
 
	TreeRef getTreeRef(int v) const {
		int a = firstArc[v];
		return TreeRef(a == -1 ? NULL : Node::findRoot(&nodes[a]));
	}
 
	int getTreeSum(int v) const {
		TreeRef t = getTreeRef(v);
		if(t.isIsolatedVertex())
			return vertexVal[v];
		else
			return t.ref->sum;
	}
	bool isConnected(int v, int w) const {
		if(v == w) return true;
		int a = firstArc[v], b = firstArc[w];
		if(a == -1 || b == -1) return false;
		return Node::findRoot(&nodes[a]) == Node::findRoot(&nodes[b]);
	}
 
	int getTreeFirstArc(TreeRef t) const {
		assert(!t.isIsolatedVertex());
		return getArcIndex(t.ref);
	}
 
	static int getSize(TreeRef t) {
		if(t.isIsolatedVertex()) return 1;
		else return t.ref->size / 2 + 1;
	}
 
	void link(int ti, int v, int w) {
		int a1 = arc1(ti), a2 = arc2(ti);
		//v→wがa1に対応するようにする
		if(v > w) std::swap(a1, a2);
 
		int va = firstArc[v], wa = firstArc[w];
 
		Node *l, *m, *r;
		if(va != -1) {
			//evert。順番を入れ替えるだけ
			std::pair<Node*,Node*> p = bst.split2(&nodes[va]);
			m = bst.join(p.second, p.first);
		}else {
			//vが孤立点の場合
			m = NULL;
			firstArc[v] = a1;
			firstArcChanged(v, -1, a1);
		}
		if(wa != -1) {
			std::pair<Node*,Node*> p = bst.split2(&nodes[wa]);
			l = p.first, r = p.second;
		}else {
			//wが孤立点の場合
			l = r = NULL;
			firstArc[w] = a2;
			firstArcChanged(w, -1, a2);
		}
		//w→vの辺をmの先頭＝lの末尾にinsert
		m = bst.cons(&nodes[a2], m);
		//v→wの辺をmの末尾＝rの先頭にinsert
		r = bst.cons(&nodes[a1], r);
 
		bst.join(bst.join(l, m), r);
	}
 
	void cut(int ti, int v, int w) {
		//v→wがa1に対応するようにする
		if(v > w) std::swap(v, w);
 
		int a1 = arc1(ti), a2 = arc2(ti);
		std::pair<Node*,Node*> p = bst.split3(&nodes[a1]);
		int prsize = BST::size(p.second);
		std::pair<Node*,Node*> q = bst.split3(&nodes[a2]);
		Node *l, *m, *r;
		//a1,a2の順番を判定する。a1＜a2ならp.secondが変わっているはず
		if(p.second == &nodes[a2] || BST::size(p.second) != prsize) {
			l = p.first, m = q.first, r = q.second;
		}else {
			//a2＜a1の順番である。v→wの辺がa1であって親→子であることにする
			std::swap(v, w);
			std::swap(a1, a2);
			l = q.first, m = q.second, r = p.second;
		}
 
		//firstArcを必要に応じて書き換える
		if(firstArc[v] == a1) {
			int b;
			if(r != NULL) {
				//vが根じゃないなら右側の最初の辺でよい
				b = getArcIndex(Node::findHead(r));
			}else {
				//vが根なら最初の辺でよい。孤立点になるなら-1
				b = !l ? -1 : getArcIndex(Node::findHead(l));
			}
			firstArc[v] = b;
			firstArcChanged(v, a1, b);
		}
		if(firstArc[w] == a2) {
			//wが根になるので最初の辺でよい。孤立点になるなら-1
			int b = !m ? -1 : getArcIndex(Node::findHead(m));
			firstArc[w] = b;
			firstArcChanged(w, a2, b);
		}
 
		bst.join(l, r);
	}
 
	void changeVertexVal(int v, int b) {
		vertexVal[v] = b;
		int a = firstArc[v];
		if(a != -1) {
			Node *t = &nodes[a];
			t->val = b;
			Node::updatePath(t);
		}
	}
};

struct Solver {
	int ii;
	int N, D;
	vector<int> S, M;
	int ans;
	Solver() {
	}
	~Solver() {
	}
	void readInput() {
		scanf("%d%d", &N, &D);
//		N=1000000,D=rand()%1000000;
		S.resize(N), M.resize(N);
		{	int A, C, R;
			scanf("%d%d%d%d", &S[0], &A, &C, &R);
//		S[0]=rand(),A=rand(),C=rand(),R=rand()+1;
			reu(i, 1, N)
				S[i] = ((ll)S[i-1] * A + C) % R;
		}
		{	int A, C, R;
			scanf("%d%d%d%d", &M[0], &A, &C, &R);
//		S[0]=rand(),A=rand(),C=rand(),R=rand()+1;
			reu(i, 1, N)
				M[i] = ((ll)M[i-1] * A + C) % R;
		}
	}
	void outputAnswer() {
		printf("Case #%d: %d\n", ii+1, ans);
	}
	void solve();
};

void Solver::solve() {
	vi parent(N, -1);
	reu(i, 1, N)
		parent[i] = M[i] % i;
	vpii xs(N);
	rep(i, N)
		xs[i] = mp(S[i], i);
	sort(all(xs));
	ans = 1;
	EulerTourTreeWithMarks ett; ett.init(N * 2);
	rep(i, N) ett.changeVertexVal(N + i, 1);
	reu(i, 1, N) ett.link(i - 1, i, N + parent[i]);
	for(int i = 0, j = 0; i < N; ++ i) {
		for(; j < N && xs[i].first + D >= xs[j].first; ++ j) {
			int u = xs[j].second, p = parent[u];
			ett.link(N - 1 + u, u, N + u);
		}
		int size = ett.getTreeSum(0);
		amax(ans, size);
		int u = xs[i].second, p = parent[u];
		ett.cut(N - 1 + u, u, N + u);
	}
}

extern "C" void __stdcall Sleep(unsigned);

int main() {
	int T;
	scanf("%d", &T);
	vector<Solver> solvers(T);
	rep(i, T) {
		solvers[i].ii = i;
		solvers[i].readInput();
	}
	int NumThreads = thread::hardware_concurrency();
	vector<thread*> threads(NumThreads);
	vector<bool> done(NumThreads, false);
	int caseNumber = 0;
	mutex theMutex;
	rep(i, NumThreads) {
		threads[i] = new thread([T, &caseNumber, &theMutex, &solvers, &done](int i) {
			while(1) {
				int myNumber;

				theMutex.lock();
				myNumber = caseNumber;
				if(myNumber < T)
					++ caseNumber;
				theMutex.unlock();

				if(myNumber < T) {
					double startTime = getTime();
					theMutex.lock();
					cerr << "case " << myNumber << " start (therad " << i << ")" << endl;
					theMutex.unlock();
					solvers[myNumber].solve();
					theMutex.lock();
					cerr << "case " << myNumber << " done in " << (getTime() - startTime) << " sec." << endl;
					theMutex.unlock();
				}else {
					theMutex.lock();
					done[i] = true;
					theMutex.unlock();
					break;
				}
			}
		}, i);
	}
	while(1) {
		theMutex.lock();
		bool end = true;
		rep(i, NumThreads)
			end &= done[i];
		theMutex.unlock();
		if(end) break;
		::Sleep(1);
	}

	rep(i, T) {
		solvers[i].outputAnswer();
	}
	return 0;
}
