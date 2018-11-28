#include<bits/stdc++.h>
#define ull unsigned long long
#define ll long long
#define pb push_back
#define mem(a,p) memset(a,p,sizeof(a))
#define fi first
#define se second
#define mp make_pair
#define bitcount __builtin_popcount
#define gcd __gcd
#define rep(i,a,b) for(int i=a;i<b;++i)
#define all(a) a.begin(),a.end()
#define sz(a) ((int)(a.size()))
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
#define debug(x,y) cerr<<x<<" "<<y<<" "<<endl;
#define ns ios_base::sync_with_stdio(false);cin.tie(0)
using namespace std;
#define VI vector<int>
#define PII pair<int,int>

int main() {
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-output1.in","w",stdout);
    int t,cs=1;
    cin>>t;
    int a[4][4],b[4][4],x,y;
    while(t--) {
        cin>>x;
        rep(i,0,4)
        rep(j,0,4)
        cin>>a[i][j];
        cin>>y;
        rep(i,0,4)
        rep(j,0,4)
        cin>>b[i][j];
        int cnt=0,res=-1;
        rep(i,0,4) {
            rep(j,0,4) {
                if(a[x-1][i]==b[y-1][j])
                    res=a[x-1][i],cnt++;
            }
        }
        if(cnt==1)
            cout<<"Case #"<<cs<<": "<<res<<"\n";
        else if(cnt>1)
            cout<<"Case #"<<cs<<": "<<"Bad magician!"<<"\n";
        else if(cnt==0)
             cout<<"Case #"<<cs<<": "<<"Volunteer cheated!"<<"\n";
        cs++;
    }
    return 0;
}
