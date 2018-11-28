#include <stdio.h>
using namespace std;

int main() 
{
    int t;
    int iter;
    scanf("%d",&t);
       int a[2501]={0};
     
    for(iter=1;iter<=t;iter++)
    {
        
        int n;
        scanf("%d",&n);
        int i;
        for(i=1;i<2501;i++)
        {
            a[i]=0;
        }
        int j,k;
        for(i=1;i<2*n;i++)
        {
            for(j=1;j<=n;j++)
            {
                scanf("%d",&k);
          //      printf("%d ",k);
                a[k]++;
            }
            
        }
        printf("Case #%d: ",iter);
        for(i=1;i<2501;i++)
        {
        //    printf("%d %d\n",i,a[i]);
            if(a[i]%2!=0)printf("%d ",i);
        }
        printf("\n");
    }
	return 0;
}

