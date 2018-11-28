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

struct rectangle
{
	int x1, x2, y1, y2;
	rectangle(){}
	rectangle(int _x1, int _x2, int _y1, int _y2) : x1(_x1), x2(_x2), y1(_y1), y2(_y2) 
	{
		if(x1 > x2) swap(x1,x2);
		if(y1 > y2) swap(y1,y2);
	}
};

int dist(const rectangle &a, const rectangle &b)
{
	int x = Infinity;
	if(a.x1 <= b.x1 and b.x1 <= a.x2) x = 0;
	if(a.x1 <= b.x2 and b.x2 <= a.x2) x = 0;
	if(b.x1 <= a.x1 and a.x1 <= b.x2) x = 0;
	if(b.x1 <= a.x2 and a.x2 <= b.x2) x = 0;
	if(x != 0)
	{
		if(a.x1 >= b.x2) x = a.x1-b.x2;
		else x = b.x1-a.x2;
	}

	int y = Infinity;
	if(a.y1 <= b.y1 and b.y1 <= a.y2) y = 0;
	if(a.y1 <= b.y2 and b.y2 <= a.y2) y = 0;
	if(b.y1 <= a.y1 and a.y1 <= b.y2) y = 0;
	if(b.y1 <= a.y2 and a.y2 <= b.y2) y = 0;
	if(y != 0)
	{
		if(a.y1 >= b.y2) y = a.y1-b.y2;
		else y = b.y1-a.y2;
	}

	return max(0,max(x,y)-1);
}

const int MAXN = 1010;
int X, Y, N;
rectangle A[MAXN];
slong D[MAXN];
bool V[MAXN];

void read_data()
{
	scanf("%d %d %d", &X, &Y, &N);
	FOR(i,1,N) 
	{
		int x1, x2, y1, y2;
		scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
		A[i] = rectangle(x1,x2,y1,y2);
	}
}

void solve()
{
	CLEAR(V);
	A[N+1] = rectangle(-1,-1,0,Y-1);
	A[N+2] = rectangle(X,X,0,Y-1);
	FOR(i,1,N+2) D[i] = Infinity;
	D[N+1] = 0;
	FOR(i,1,N+2)
	{
		int t = -1;
		FOR(j,1,N+2) if(!V[j] and (t == -1 or D[j] < D[t])) t = j;
		V[t] = true;
		FOR(j,1,N+2) D[j] = min(D[j], D[t] + dist(A[t],A[j]));	
	//	cout << "T: " << t << endl;
	}
	//FOR(i,1,N+2) cout << A[i].x1 << " " << A[i].x2 << " " << A[i].y1 << " " << A[i].y2 << endl;
	//FOR(i,1,N+2) cout << i << " " << D[i] << endl;
//	FOR(i,1,N+2) FOR(j,1,N+2) cout << MP(i,j) << " " << dist(A[i],A[j]) << endl;
//	cout << "DEBUG: " << dist(A[2],A[1]) << endl;
	printf("%lld\n", D[N+2]);
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
