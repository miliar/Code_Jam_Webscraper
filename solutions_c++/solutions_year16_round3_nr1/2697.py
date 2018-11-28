#include<stdio.h>
#include<string.h>
#include<algorithm>

using namespace std;

int a[30];

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.txt","w",stdout);
    int i,j,m,n,t,max,cnt,flag,co=1;
    int sum;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);
        sum=0;
        for(i=0;i<n;i++)
        {
            scanf("%d",&a[i]);
            sum+=a[i];
        }
        flag=m=0;
        printf("Case #%d:",co++);
        while(1)
        {
            max=0;
            for(i=0;i<n;i++)
                if(a[i]>max)
                    max=a[i];
            if(!max)
                break;
            cnt=0;
            for(i=0;i<n;i++)
            {
                if(a[i]==max)
                {
                    if(!cnt)
                        printf(" %c",i+65);
                    else
                        printf("%c",i+65);
                    cnt++;
                    a[i]--;
                    m++;
                    if(sum-m==2)
                    break;
                }
                if(cnt==2)
                    break;
            }
        }
        printf("\n");
    }
    return 0;
}
