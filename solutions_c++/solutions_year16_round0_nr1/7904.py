#include<bits/stdc++.h>

using namespace std;

#define LL long long
#define pb push_back
#define pLL pair<LL,LL>
#define ff first
#define ss second
#define rep(i,a,b) for(LL i=a;i<=b;++i)
#define ld double
#define mp make_pair
#define vLL vector<LL>
#define vpLL vector<pLL>
#define vld vector<ld>
#define pld pair<ld,ld>
#define vpld vector<pld>
#define SLL set<LL>
#define SpLL set<pLL>

LL n,t,cnt[10];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("ans.txt","w",stdout);
    cin>>t;
    rep(loop,1,t){
        rep(i,0,9) cnt[i]=0;
        cin>>n;
        cout<<"Case #"<<loop<<": ";
        if(n==0){
            cout<<"INSOMNIA\n";
            continue;
        }
        for(LL i=1;;i++){
            LL tmp=i*n;
            while(tmp>0){
                cnt[tmp%10]=1;
                tmp/=10;
            }
            bool chk=true;
            rep(j,0,9){
                if(cnt[j]==0) chk=false;
            }
            if(chk){
                cout<<i*n<<endl;
                break;
            }
        }
    }
}
