#include<bits/stdc++.h>
#define ALL(X)       X.begin(),X.end()
#define FOR(I,A,B)   for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)  for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)  for(int (I) = (A); (I) >= (B); (I)--)
#define CLEAR(X)     memset(X,0,sizeof(X))
#define SIZE(X)      int(X.size())
#define CONTAIN(A,X) (A.find(X) != A.end())
#define PB           push_back
#define MP           make_pair
#define X            first
#define Y            second
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong Infinity = 1000000100;
const ldouble Epsilon = 1e-9;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T,U>&p) { return os << "(" << p.X << "," << p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& V) { os << "["; FORW(i,0,SIZE(V)) os << V[i] << ((i==SIZE(V)-1) ? "" : ","); return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& S) {os << "("; for(T i: S) os << i << (i==*S.rbegin()?"":","); return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& M){os << "{"; for(pair<T,U> i: M) os << i << (i.X==M.rbegin()->X?"":","); return os << "}"; }
template<typename T, typename F> T lbound(T p, T q, F f) { while(p < q) { T r = p+(q-p)/2; if(f(r)) q = r; else p = r+1; } return p; }
template<typename T, typename F> T lboundl(T p, T q, F f) { FOR(i,1,70) { T r = (p+q)/2; if(f(r)) q = r; else p = r; } return p; }

const int MAXN = 1010;
int N;
int A[MAXN];

void read_data()
{
	scanf("%d", &N);
	FOR(i,1,N) scanf("%d", A+i);
}

bool Q[MAXN];

void solve()
{
	CLEAR(Q);
	vector<pair<int,int>> V;
	FOR(i,1,N) V.PB(MP(A[i],i));
	sort(ALL(V));
	int result = 0;
	for(auto v: V)
	{
		int id = v.Y;
		int l = id-1;
		FOR(i,1,id-1) if(Q[i]) --l;
		int r = N-id;
		FOR(i,id+1,N) if(Q[i]) --r;
		result += min(l,r);
		Q[id] = true;
	}
	printf("%d\n", result);
}

int main() 
{
	int z;
	scanf("%d", &z);
	FOR(_,1,z)
	{
		printf("Case #%d: ", _);
		read_data();
		solve();
	}
	return 0;
}
