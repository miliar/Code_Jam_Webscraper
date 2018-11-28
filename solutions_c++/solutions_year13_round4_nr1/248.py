#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;
const long long mod = 1000002013;
struct vvv{
  long long st,b,p;      
}pp[5555];
long long n,m,t,tot1,tot2,k,a[11111],b[11111],sk,tmp,ppx;

bool cmp(const vvv &a,const vvv &b){
  if (a.st==b.st)
     return a.b<b.b;
  return a.st<b.st;   
}

int main(){
    freopen("a.in","r",stdin);
    freopen("b.out","w",stdout);
    cin>>t;
    for (int i=1;i<=t;i++){
        cin>>n>>m;
        tot1=tot2=0;
        for (int j=0;j<m;j++){
            cin>>pp[j*2].st;
            pp[j*2].b=0;
            cin>>pp[j*2+1].st;
            pp[j*2+1].b=1;
            cin>>ppx;
            pp[j*2].p=pp[j*2+1].p=ppx;
            k=pp[j*2+1].st-pp[j*2].st;
            tmp = n*k-k*(k-1)/2;
            tmp = tmp%mod;
            tmp = tmp*ppx%mod;
            tot1=(tot1+tmp)%mod;  
        }    
        sk=0;
        sort(pp,pp+2*m,cmp);
       // cout<<pp[2].st<<" "<<pp[2].b<<endl;
        memset(b,0,sizeof(b));
        for (int j=0;j<2*m;j++){
            if (pp[j].b==1){
                ppx = pp[j].p;
                while (ppx){
                    if (sk&&ppx>b[sk-1]){
                       ppx -=b[sk-1];
                       k = pp[j].st-a[sk-1];
                       tmp = n*k-(k-1)*k/2;
                       tmp = tmp%mod;
                       tmp = tmp*b[sk-1]%mod;
                       tot2 = (tot2+tmp)%mod;
                       b[sk-1]=0;
                       sk--;                     
                    }
                    else{
                       k = pp[j].st-a[sk-1];
                       //cout<<k<<endl;
                       tmp = n*k-(k-1)*k/2;
                       tmp = tmp%mod;
                       tmp = tmp*ppx%mod;
                       tot2 = (tot2+tmp)%mod;
                       b[sk-1]-=ppx;
                       ppx = 0;   
                    }
                }     
                //cout<<tot2<<endl;
            }    
            else{
                if (sk&&a[sk-1]==pp[j].st){
                   b[sk-1]+=pp[j].p;
                } 
                else{
                    a[sk] = pp[j].st;
                    b[sk++]=pp[j].p;     
                }
            }
        }
        tot1-=tot2;
        tot1=(tot1+mod)%mod;
        cout<<"Case #"<<i<<": "<<tot1<<endl;
    }
    return 0;   
}
