#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(0);cin.tie(0);

using namespace std;

inline int toInt(string s) {int i;stringstream (s)>>i;return i;}
inline string toString(int i) {string s;stringstream ss;ss<<i;ss>>s;return s;}

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
#define MOD 1000000009

int main(){_
    #ifndef ONLINE_JUDGE
        freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);
    #endif
    int t;
    cin>>t;
    double c,f,x,ans,r,t1,t2;
    FORE(tt,1,t){
        cin>>c>>f>>x;r=2.0;
        ans=0;
        while(1){
            t1=c/r;
            t2=x/(r+f);
            if((t1+t2)*r<x){
                r+=f;
                ans+=t1;
            }
            else{
                ans+=x/r;
                break;
            }
        }
        cout<<"Case #"<<tt<<": "<<setprecision(7)<<fixed<<ans<<endl;
    }
return 0;
}
