#include<bits/stdc++.h>

#define xx first
#define yy second
#define LL long long
#define inf 100000000
#define pb push_back
#define vsort(v) sort(v.begin(),v.end())
#define pi acos(-1)
#define clr(a,b) memset(a,b,sizeof a)
#define bclr(a) memset(a,false,sizeof a)
#define pii pair<int,int>
#define MOD 1000000007
#define MP make_pair
#define MX 1005

using namespace std;

int ar[20];
vector<string>V;
vector<int>vv;
vector<vector<int> >vvv;

LL getVal(int n,LL base){
    LL ret=0;
    LL now=1ll;
    for(int i=0;i<n;i++){
        if(ar[i]) ret+=now;
        now*=base;
    }
    return ret;
}

bool prime(LL x){
    for(LL i=2;i*i<=x;i++){
        if(x%i==0){
            vv.pb(i);
            return false;
        }
    }
    return true;
}

int ok(int n){
    vv.clear();
    if(ar[0]==0 || ar[n-1]==0) return 0;
    for(int i=2;i<=10;i++){
        LL val=getVal(n,i);
        if(prime(val)) return 0;
    }
    vvv.pb(vv);
    return 1;
}
//
//void print(int n){
//    for(int i=n-1;i>=0;i--) cout<<ar[i]<<" ";
//    cout<<endl;
//}

LL solve(int n){
    int res=0;
    for(int i=0;i<(1<<n);i++){
        for(int j=0;j<n;j++){
            ar[j]=(i&(1<<j))?1:0;
        }
        int f=ok(n);
        res+=f;
        if(f){
            string tmp="";
            for(int j=n-1;j>=0;j--){
                if(ar[j]==1) tmp+='1';
                else tmp+='0';
            }
            V.pb(tmp);
        }
        if(res==50) break;

    }
    return res;
}

int main(){
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int test; cin>>test;
    for(int kase=1;kase<=test;kase++){
        int n,k; cin>>n>>k;
        solve(n);
        cout<<"Case #"<<kase<<":\n";
        for(int i=0;i<k;i++){
            cout<<V[i];
            for(int j=0;j<9;j++) cout<<" "<<vvv[i][j];
            cout<<endl;
        }
        V.clear(); vvv.clear();
    }
    return 0;
}

