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

int d[50][50];
int d2[50][50];

int check(int mw, int mm, int N)
{
    if(mw == (1<<N)-1) return 1;
    FOR(i,0,N-1)
    {
        if(mw & (1<<i)) continue;
        int ops = 0;
        FOR(j,0,N-1)
        {
            if(!d2[i][j] || (mm & (1<<j))) continue;
            ops++;
            if(!check(mw|(1<<i), mm|(1<<j),N)) return 0;
        }
        if(!ops) return 0;
    }
    return 1;
}

void solve(int num)
{
    int N;
    cin >> N;
    FOR(i,0,N-1)
    {
        string s;
        cin >> s;
        FOR(j,0,N-1)
        {
            if(s[j] == '0') d[i][j] = 0;
            else d[i][j] = 1;
        }
    }

    int ans = N*N;
    int M = N*N;

    for(int mask = 1; mask < (1<<M); mask++) // !@@#$@#%#$%#%#$%#$%#$%
    {
        int cur = 0;
        FOR(i,0,N-1)
        {
            FOR(j,0,N-1)
            {
                int k = i*N + j;
                if(mask & (1<<k))
                {
                    d2[i][j] = 1;
                    if(!d[i][j]) cur++;
                }
                else d2[i][j] = d[i][j];
            }
        }
        int kk = 1;
        vector<int> wiersz(N,0), kol(N,0);
        FOR(i,0,N-1)
        {
            FOR(j,0,N-1)
            {
                if(d2[i][j])
                {
                    wiersz[i] = 1;
                    kol[j] = 1;
                }
            }
            int wspolni = 0, fail = 0;
            FOR(j,i+1,N-1)
            {
                FOR(k,0,N-1)
                {
                    if(d2[i][k] && d2[j][k]) wspolni++;
                    if(d2[i][k] ^ d2[j][k]) fail++;
                }
            }
            if(wspolni && fail) kk = 0;
        }
        FOR(i,0,N-1)
        {
            if(!wiersz[i] || !kol[i]) kk = 0;
        }

        //cout << ">>> " << wspolni << " " << fail << "\n";
        /*cout << "maska z kosztem " << cur << " kk? : " << kk << endl;
        FOR(i,0,N-1)
        {
            FOR(j,0,N-1)
            {
                cout << d2[i][j];
            }
            cout << "\n";
        }
        cout << "wychodzi " << check(0,0,N) << "\n";*/

        if(check(0,0,N)) ans = min(ans, cur);
    }

    cout<<"Case #"<<num<<": "<<ans<<"\n";

}

int main()
{
    ios_base::sync_with_stdio(0);
    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        solve(i);
    }
}
