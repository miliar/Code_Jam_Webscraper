#include<bits/stdc++.h>
using namespace std;
#define ll int
#define sc second
#define fr first
#define pb push_back
#define ARRS int(2e5+10)
#define INF int(2e8+10)


int main(){
    #ifdef KHOKHO
        freopen("in.in","r",stdin);
        freopen("out.out","w+",stdout);
    #endif
    ll m;
    cin>>m;
    for(int t=1; t<=m; t++){
        ll n;
        cin>>n;
        bool fx[10];
        for(int i=0; i<10; i++)
                fx[i]=0;
        bool e=1;
        for(int i=1; i<100000; i++){
            ll p=n*i;
            while(p){
                fx[p%10]=1;
                p/=10;
            }
            e=1;
            for(int i=0; i<10; i++)
                if(!fx[i])e=0;
            if(e){
                cout<<"Case #"<<t<<": "<<i*n<<endl;
                break;
            }
        }
        if(!e)cout<<"Case #"<<t<<": INSOMNIA"<<endl;
    }
    return 0;
}
