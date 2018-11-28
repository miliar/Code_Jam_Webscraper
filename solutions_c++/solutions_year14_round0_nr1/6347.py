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
    int t,n1,n2,n3,flag;
    cin>>t;
    int a[4][4],b[4][4],tmp[4];
    FORE(tt,1,t){
        cin>>n1;n1--;
        REP(i,4)
            REP(j,4)
                cin>>a[i][j];
        cin>>n2;n2--;
        REP(i,4)
            REP(j,4)
                cin>>b[i][j];
        flag=0;
        REP(i,4)
            tmp[i]=a[n1][i];
        REP(i,4)
            REP(j,4)
                if(b[n2][j]==tmp[i]){
                    flag++;
                    n3=tmp[i];
                }
        if(flag==1)
            cout<<"Case #"<<tt<<": "<<n3<<endl;
        else if(flag==0)
            cout<<"Case #"<<tt<<": Volunteer cheated!"<<endl;
        else
            cout<<"Case #"<<tt<<": Bad magician!"<<endl;
    }
return 0;
}
