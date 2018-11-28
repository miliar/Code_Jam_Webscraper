#include<bits/stdc++.h>

#define pb push_back
#define mp make_pair
#define x first
#define y second
#define y0 qweasd
#define y1 qasdna
#define left leva
#define right prava
#define next sled
#define int long long
using namespace std;
const int N=503772;
const int inf=1e18+7;
vector<int> v,top,lev;
vector<vector<int> > bot,keke;
vector<vector<int> > kok;
int n,k,ans;
void finish(){
    cout<<"Case #1:\n";
    for(int i=0;i<k;++i){
        reverse(keke[i].begin(),keke[i].end());
        for(int j=0;j<keke[i].size();++j)
            cout<<keke[i][j];
        cout<<' ';
        for(int j=0;j<bot[i].size();++j)
            cout<<bot[i][j]<<' ';
        cout<<"\n";
    }
    exit(0);
}
int kek(int x){
    for(int i=2;i*i<=x;++i){
        if(x%i==0){
            return i;
        }
    }
    return 0;
}
int st[30][40];
bool prime(int x){
    for(int i=2;i*i<=x;++i)
    if(x%i==0)return 0;
    return 1;
}
void check(){
    top.clear();
    lev.clear();
    for(int i=2;i<=10;++i){
        int q=0;
        for(int j=0;j<v.size();++j)
            q+=v[j]*st[j][i];
        if(prime(q))return;
        lev.pb(q);
        int e=kek(q);
        if(e!=0)top.pb(e);
        else return;
       // cout<<i<<' '<<q<<"\n";
    }
    ++ans;
    bot.pb(top);
    kok.pb(lev);
    keke.pb(v);
    if(ans==k){
        finish();
    }
}
void f(int len){
    if(len+1==n){
        v.pb(1);
        check();
        v.pop_back();
        return;
    }
    v.pb(0);
    f(len+1);
    v.pop_back();
    v.pb(1);
    f(len+1);
    v.pop_back();
}
main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int lel;
    cin>>lel;
    cin>>n>>k;
    for(int i=2;i<=10;++i)
        st[0][i]=1;
    for(int i=2;i<=10;++i)
        for(int j=1;j<=15;++j)
            st[j][i]=st[j-1][i]*i;
    v.pb(1);
    f(1);


}

