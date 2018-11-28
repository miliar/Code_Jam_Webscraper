#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstring>
using namespace std;

int s[35];
long long c,j;
int d[11];

int main(){
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    int T,tc,n,m,i,t,k,b,ok;
    scanf("%d",&T);
    for(tc=1;tc<=T;++tc){
        printf("Case #%d:\n",tc);
        scanf("%d%d",&n,&k);
        for(m=0; m < (1<<(n-2)); ++m){
            s[0]=s[n-1]=1;
            t=m;
            for(i=1;i<n-1;++i){
                if(t&1) s[i]=1;
                else s[i]=0;
                t>>=1;
            }

            //for(i=n-1;i>=0;--i) printf("%d",s[i]); printf("---\n");
            ok=1;
            for(b=2;b<=10;++b){
                j=1;
                c=0;
                for(i=0;i<n;++i){
                    c+=s[i]*j;
                    j*=b;
                }
                //printf("b=%d, c=%d\n",b,c);
                d[b] = -1;
                for(i=3;1ll*i*i<=c;i+=2){
                    if(c%i==0){
                        d[b] = i;
                        break;
                    }
                }
                if(d[b] == -1){
                    ok=0;
                    break;
                }
            }
            if(ok){
                for(i=n-1;i>=0;--i) printf("%d",s[i]);
                for(i=2;i<=10;++i) printf(" %d",d[i]);
                printf("\n");
                k--;
                if(k==0) break;
            }
        }
    }
    return 0;
}
