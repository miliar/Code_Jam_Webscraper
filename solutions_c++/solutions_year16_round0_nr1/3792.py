#include <stdio.h>
int chk;
int main (void)
{
    int i,j,k,n,t;
    FILE*out;

    freopen("input.txt","r",stdin);
    out=fopen("output.txt","w");
    scanf("%d",&t);

    for(i=0;i<t;i++){
        scanf("%d",&n);
        if(n==0){
            fprintf(out,"Case #%d: INSOMNIA\n",i+1);
            continue;
        }

        for(j=n;chk!=(1<<10)-1;j+=n){
            for(k=j;k>0;k/=10){
                chk|=1<<(k%10);
            }
        }
        fprintf(out,"Case #%d: %d\n",i+1,j-n);
        chk=0;
    }

    return 0;
}
