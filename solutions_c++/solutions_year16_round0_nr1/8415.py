#include <stdio.h>
#include <stdlib.h>

int t,n,nn,i,j,k,ii,ok,visited[20];

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&t);
    for (ii=1; ii<=t; ii++) {
        scanf("%d",&n);
        if (n==0) {
            printf("Case #%d: INSOMNIA\n",ii);
            continue;
        }
        
        nn=n;
        k=n;
        while (k>0) {
            visited[k%10]=ii;
            k/=10;
        }
        
        ok=1;
        for (i=0; i<=9; i++)
            if (visited[i]!=ii) {
                ok=0;
                break;
            }
        
        while (ok==0) {
            n+=nn;
            k=n;
            while (k>0) {
                visited[k%10]=ii;
                k/=10;
            }
            
            ok=1;
            for (i=0; i<=9; i++)
                if (visited[i]!=ii) {
                    ok=0;
                    break;
                }
        }
        
        printf("Case #%d: %d\n",ii,n);
    }
}