#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

inline int toInt(string s) {int i;stringstream (s)>>i;return i;}
inline string toString(long long i) {string s;stringstream ss;ss<<i;ss>>s;return s;}

typedef long long LL;
typedef unsigned long long ULL;
typedef pair<int,int> PII;
typedef pair<ULL,ULL> PUU;
typedef vector<int> VI;
typedef vector<long> VL;
typedef vector<string> VS;

#define FOR(i,a,b) for(int i=a;i<b;i++)
#define FORE(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define RALL(c) (c).rbegin(), (c).rend()
#define SORT(c) sort(ALL(c))
#define PB push_back
#define MP make_pair

#define INF (long)1e9
#define EPS 1e-9

int main(){_
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int t,n,ans,tmp,mx;cin>>t;
    FORE(z,1,t){
        cin>>n;
        VI v(n);
        REP(i,n)cin>>v[i];
        mx=*max_element(ALL(v));
        ans=mx;
        FORE(i,1,mx){
            tmp=i;
            REP(j,n){
                if(v[j]>i){
                    tmp+=v[j]/i-1;
                    if(v[j]%i)tmp++;
                }
            }
            ans=min(ans,tmp);
        }
        cout<<"Case #"<<z<<": "<<ans<<endl;
    }
return 0;
}
