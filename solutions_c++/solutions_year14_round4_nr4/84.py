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

const int MAXN = 10;
char buff[MAXN];
string S[MAXN];
int T[MAXN];
int N, K;

void read_data()
{
	scanf("%d %d", &N, &K);
	FOR(i,1,N) 
	{
		scanf("%s", buff);
		S[i] = string(buff);
	}
}

int result;
int poss;
set<string> Q[MAXN];

void rec(int n, int k)
{
	if(n == N+1 and k == K)
	{
//		cout << "T";
//FOR(i,1,N) cout << T[i] << endl;cout << endl;
		FORW(i,0,MAXN) Q[i].clear();
		FOR(i,1,N) FOR(j,0,SIZE(S[i])) Q[T[i]].insert(S[i].substr(0,j));
		int r = 0;
		FOR(i,1,K) r += SIZE(Q[i]);
//		if(r == 10)		{			cout << Q[1] << endl;			cout << Q[2] << endl;		}
		
		if(r > result)
		{
			result = r;
			poss = 1;
		}
		else if(r == result)
		{
			++poss;
		}
	}
	else if(n == N+1 or k >= K+1) return;
	else
	{
		T[n] = k+1;
		rec(n+1,k+1);
		FOR(i,1,k) 
		{
			T[n] = i;
			rec(n+1,k);
		}
	}
}

void solve()
{
	result = -1;
	poss = 0;
	rec(1,0);
	FOR(i,1,K) poss *= i;
	printf("%d %d\n", result, poss);
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
