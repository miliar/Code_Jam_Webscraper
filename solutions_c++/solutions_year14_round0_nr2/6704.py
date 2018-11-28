#include<bits/stdc++.h>
#define ALL(X) X.begin(),X.end()
#define SIZE(X) ((int)X.size())
#define FOR(I,A,B) for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B) for(int (I) = (A); (I) < (B); (I)++)
#define FORD(I,A,B) for(int (I) = (A); (I) >= (B); (I)--)
#define FOREACH(a,b) for(__typeof(b.begin()) a = b.begin(); a != b.end(); ++a)
#define LBOUND(P,R,PRED) ({__typeof(P) X=P,RRR=(R), PPP = P; while(PPP<RRR) {X = (PPP+(RRR-PPP)/2); if(PRED) RRR = X; else PPP = X+1;} PPP;})
#define CONTAIN(C,X) (C.find(X) != C.end())
#define CLEAR(X) memset(X, 0, sizeof(X))
#define PB push_back
#define MP make_pair
#define X first
#define Y second

using namespace std;
typedef signed long long slong;
const slong Infinity = 1000000100;

typedef long double ldouble;
const ldouble Epsilon = 1e-9;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T,U>&p) {return os << "(" << p.first << "," << p.second << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& V) {os << "["; FOREACH(i, V) os << *i << (i-V.begin()+1==SIZE(V)?"":","); os << "]\n"; return os; }
template<typename T> ostream& operator << (ostream &os, const set<T>& S) {os << "("; FOREACH(i, S) os << *i << (*i==*S.rbegin()?"":","); os << ")\n"; return os; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& M){os << "{"; FOREACH(i, M) os << *i << (i->first==M.rbegin()->first?"":","); os << "}\n"; return os; }

ldouble C, F, X;

void read_data()
{
	scanf("%Lf %Lf %Lf", &C, &F, &X);
}

void solve()
{
	ldouble result = X/2;
	ldouble t = 0;
	ldouble w = 2;
	FOR(i,1,X)
	{
		t += C/w;
		w += F;
		result = min(result, t+X/w);
	}
	printf("%.10Lf\n", result);
}

int main()
{
	int z;
	scanf("%d", &z);
	FOR(_,1,z)
	{
		read_data();
		printf("Case #%d: ", _);
		solve();
	}
	return 0;
}
