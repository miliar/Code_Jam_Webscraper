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

int N, X;
const int MAXN = 1000100;
char A[MAXN];

int I = 2;
int J = 3;
int K = 4;
vector<vector<int>> Q {
    {0, 0, 0, 0, 0},
    {0, 1, I ,J , K},
    {0, I, -1, K, -J},
    {0, J, -K, -1, I},
    {0, K, J, -I, -1} 
};

void read_data()
{
	scanf("%d %d", &N, &X);
    scanf("%s", A+1);
    FOR(i,1,N) {
        if(A[i] == '1') A[i] = 1;
        if(A[i] == 'i') A[i] = I;
        if(A[i] == 'j') A[i] = J;
        if(A[i] == 'k') A[i] = K;
    }
}

int T[MAXN];
int t;

bool solve()
{
    t = 0;
    FOR(_,1,X) FOR(i,1,N) T[++t] = A[i];
    int r = 1;
    int x = -1;
    FOR(i,1,t) {
        bool minus = r < 0;
        if(minus) r = -r;
        r = Q[r][T[i]];
        if(minus) r = -r;
        if(r == I) {
            x = i;
            break;
        }
    }

    int y = -1;
    r = 1;
    FORD(i,t,1) {
        bool minus = r < 0;
        if(minus) r = -r;
        r = Q[T[i]][r];
        if(minus) r = -r;
        if(r == K) {
            y = i;
            break;
        }
    }

    if(x == -1 or y == -1) return false;

    r = 1;
    FOR(i,x+1,y-1) {
        bool minus = r < 0;
        if(minus) r = -r;
        r = Q[r][T[i]];
        if(minus) r = -r;
       }

    return r == J;
}

int main() 
{
    int z;
    scanf("%d", &z);
    FOR(i,1,z) {
    	read_data();
    	bool result = solve();
        printf("CASE #%d: %s\n", i, result ? "YES" : "NO");
    }
	return 0;
}
