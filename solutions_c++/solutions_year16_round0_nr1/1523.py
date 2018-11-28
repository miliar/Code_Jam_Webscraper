#include<cstdio>
#include<cstring>
using namespace std;
typedef long long ll;
int T,t,ret;
ll n,m;
bool num[15];
void solve(ll temp){
    int i,j,k;
    while(temp){
        k=temp%10;
        if(num[k]==0){
            num[k]=1;
            ret++;
        }
        temp/=10;
    }
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);

    int i,j,k;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%I64d",&n);
        memset(num,0,sizeof(num));
        if(n==0)
            printf("Case #%d: INSOMNIA\n",t);
        else{
            m=0;
            ret=0;
            while(ret<10){
                m+=n;
                solve(m);
            }
            printf("Case #%d: %I64d\n",t,m);
        }
    }
}
