#include <cstdio>
#include <cstring>
using namespace std;
int TestCase,a[33],N,M;
char b[33];
int main(){
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&TestCase);
    for(int O=1; O<=TestCase; O++){
        scanf("%d", &N); M=N;
        memset(a,0,sizeof(a));
        for(int i=1; i<=N; i++)
            scanf("%d",&a[i]), b[i]=char(i+64);
        printf("Case #%d: ",O);
        while(1){
            if(M==2){
                int A=0; int B=0;
                for(int i=1; i<=N; i++){
                    if(a[i]==0)continue;
                    if(A) B=i; else A=i;
                }
                if(a[A]==a[B]){
                    for(int i=1; i<a[A]; i++)
                        printf("%c%c ",b[A],b[B]);
                    printf("%c%c\n",b[A],b[B]);
                    break;
                }
            }
            int MAX=1;
            for(int i=1; i<=N; i++)
                if(a[i]>a[MAX]) MAX=i;
            a[MAX]--; if(a[MAX]==0) M--;
            printf("%c ",b[MAX]);
        }
    }
}
