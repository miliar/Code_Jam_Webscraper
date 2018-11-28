#include <stdio.h>
using namespace std;
#define ull unsigned long long  int
int main() 
{
    int t,iter;
    scanf("%d",&t);
    for(iter=0;iter<t;iter++)
    {
        ull k,c,s;
        scanf("%llu%llu%llu",&k,&c,&s);
        ull a[k];
        int i;
        for(i=1;i<=k;i++)
        {
            a[i]=i;
        }
        ull p=1,sum=0;;
        for(i=1;i<c;i++)
        {
            p*=k;
            sum=p;
            for(int j=2;j<=k;j++)
            {
                //p*=c;
                a[j]+=(j-1)*sum;
                //printf("%d\n",a[i]);
     //           printf("%d\n",sum);
            //    sum+=p;
            }
        }
        printf("Case #%d: ",iter+1);
        for(p=1;p<=k;p++)
        {
            printf("%llu ",a[p]);
        }
        printf("\n");
    }
	return 0;
}

