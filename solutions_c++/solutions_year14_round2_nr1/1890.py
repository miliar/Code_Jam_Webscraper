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
    int t,n,ans,i,ii,j,t1,t2;
    cin>>t;
    vector<string>vs;
    char s;
    FORE(z,1,t){
        cin>>n;vs.resize(n);
        REP(i,n)cin>>vs[i];
        ans=0;i=0;j=0;
        while(1){
            if(i>=vs[0].size())break;
            s=vs[0][i];ii=i;
            while(vs[0][ii]==vs[0][i])ii++;
            t1=ii-i;
            i+=t1;
            if(vs[1][j]==s){
                ii=j;
                while(vs[1][ii]==s)ii++;
                t2=ii-j;
                j+=t2;
                ans+=abs(t1-t2);
                //cout<<ans<<endl;
            }
            else{
                ans=-1;
                break;
            }
        }
        if(j<vs[1].size())cout<<"Case #"<<z<<": Fegla Won"<<endl;
        else{
            if(ans>=0)cout<<"Case #"<<z<<": "<<ans<<endl;
            else cout<<"Case #"<<z<<": Fegla Won"<<endl;
        }
    }
return 0;
}
