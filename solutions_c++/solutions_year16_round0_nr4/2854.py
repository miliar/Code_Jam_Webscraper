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
int q[115];
int n;
bool ok(){
    for(int i=0;i<10;++i)
        if(!q[i])return 0;
    return 1;
}
void f(int x){
    if(x==0){
        q[0]=1;
        return;
    }
    for(;x;x/=10)
        q[x%10]=1;
}
main(){
    cin.tie(0);
    ios_base::sync_with_stdio(0);
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int tek;
    int q,w,e;
    int it=0;
    cin>>tek;
    for(;tek;--tek){
            ++it;
     cin>>q>>w>>e;
    cout<<"Case #"<<it<<": ";
    for(int i=1;i<=q;++i)
        cout<<i<<' ';
    cout<<"\n";
    }




}

