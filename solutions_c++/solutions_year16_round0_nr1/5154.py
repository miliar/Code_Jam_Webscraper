#include<bits/stdc++.h>
using namespace std;
#define pii pair<int,int>
#define fs first
#define sc second
typedef long long ll;
bool upd(int v,bool* pt){
    bool rt = 1;
    while(v!=0){
        pt[v%10]=1;
        v/=10;
    }
    for(int i = 0 ;i<10 ;i++)
        rt&=pt[i];

}

int main(){
    ios_base::sync_with_stdio(false);cin.tie(0);
    freopen ("file.out","w",stdout);
    freopen ("file.in","r",stdin);
    int t , n ,sol;
    cin>>t;
    for(int p = 1 ; p<=t;p++){
        cin>>n;
        if(!n){
            cout<<"Case #"<<p<<": INSOMNIA"<<'\n';
            continue;
        }
        bool dg[10];
        memset(dg,0 , sizeof dg);
        int res = n;
        bool ans =  upd(res,dg);
        for(int i  = 2 ;i<100;i++){
            if(ans)break;
            res = n*i;
            ans =  upd(res,dg);

        }
        cout<<"Case #"<<p<<": "<<res<<'\n';

    }


    return 0;

}

