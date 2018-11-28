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
string s;
int n;
int a[205],b[205];
int f1(int l,int r);
int f2(int l,int r){
    bool done=1;
    bool fine=1;
    for(int i=l;i<=r;++i){
        if(b[i]==0)done=0;
        if(b[i]==1)fine=0;
    }
    if(done)return 0;
    if(fine)return 1;
    if(b[r]==1)return f2(l,r-1);
    int re=r;
    while(b[re]==0)--re;
    return f1(l,re)+1;

}
int f1(int l,int r){
    bool done=1;
    bool fine=1;
    for(int i=l;i<=r;++i){
        if(a[i]==0)done=0;
        if(a[i]==1)fine=0;
    }
    if(done)return 0;
    if(fine)return 1;
    if(a[r]==1)return f1(l,r-1);
    int re=r;
    while(a[re]==0)--re;
    return f2(l,re)+1;
}
main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    int inter=0;
    cin>>t;
    for(;t;--t){
    cin>>s;
    for(int i=0;i<s.size();++i){
        if(s[i]=='+')a[i+1]=1;
        else a[i+1]=0;
        b[i+1]=1-a[i+1];
    }
    ++inter;
    n=s.size();
   // for(int i=1;i<=n;++i)cout<<a[i];cout<<"\n";
    cout<<"Case #"<<inter<<": "<<f1(1,n)<<"\n";
    }



}

