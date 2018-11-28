#include<bits/stdc++.h>
#define ALL(X)        X.begin(),X.end()
#define FOR(I,A,B)    for(int (I) = (A); (I) <= (B); (I)++)
#define FORW(I,A,B)   for(int (I) = (A); (I) < (B);  (I)++)
#define FORD(I,A,B)   for(int (I) = (A); (I) >= (B); (I)--)
#define FOREACH(I,A)  for(__typeof(A.begin()) I = A.begin(); I != A.end(); ++I)
#define CLEAR(X)      memset(X,0,sizeof(X))
#define SIZE(X)       int(X.size())
#define CONTAIN(A,X)  (A.find(X) != A.end())
#define PB            push_back
#define MP            make_pair
#define X             first
#define Y             second
#define LBOUND(P,R,Q) ({__typeof(P) X=P,RR=(R), PP = P; while(PP<RR) {X = (PP+(RR-PP)/2); if(Q) RR = X; else PP = X+1;} PP;})
using namespace std;
typedef signed long long slong;
typedef long double ldouble;
const slong Infinity = 1000000100;
const ldouble Epsilon = 1e-9;
template<typename T, typename U> ostream& operator << (ostream& os, const pair<T,U>&p) { return os << "(" << p.X << "," << p.Y << ")"; }
template<typename T> ostream& operator << (ostream &os, const vector<T>& V) { os << "["; FORW(i,0,SIZE(V)) os << V[i] << ((i==SIZE(V)-1) ? "" : ","); return os << "]"; }
template<typename T> ostream& operator << (ostream &os, const set<T>& S) {os << "("; FOREACH(i,S) os << *i << (*i==*S.rbegin()?"":","); return os << ")"; }
template<typename T, typename U> ostream& operator << (ostream &os, const map<T, U>& M){os << "{"; FOREACH(i,M) os << *i << (*i.X==M.rbegin()->X?"":","); return os << "}"; }

int N;
const int MAXN = 1000100;
int A[MAXN];

void read_data()
{
	scanf("%d", &N);
    FOR(i,1,N) scanf("%d", A+i);
}

int solve()
{
    int result = Infinity;
    FOR(t,1,1000) {
        int q = t;
        FOR(i,1,N) {
            q += (A[i]-1)/t;
        }
        result = min(result, q);
    }
    return result;
}

int main() 
{
    int z;
    scanf("%d", &z);
    FOR(i,1,z) {
    	read_data();
    	int result = solve();
        printf("CASE #%d: %d\n", i, result);
    }
	return 0;
}
