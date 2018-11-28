#include<stdio.h>
#include<algorithm>
using namespace std;
int n;
int p[30];
main()
{
    int time,i,j,k,c,cnt,acnt;
    int sum;
    int num = 1;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("senate.txt","w",stdout);
    scanf("%d",&time);
    while(time--)
    {
        scanf("%d",&n);
        sum = 0;
        for(i=0;i<n;i++) scanf("%d",&p[i]),sum+=p[i];
        printf("Case #%d: ",num++);
        while(sum>0)
        {
            for(i=0;i<n+1;i++)
            {
                for(j=0;j<n+1;j++)
                {
                    p[i]--; p[j]--;
                    c = cnt = acnt = 0;
                    if(i!=n) c++;
                    if(j!=n) c++;
                    for(k=0;k<n;k++) cnt+=p[k],acnt=max(acnt,p[k]);
                    if(cnt<acnt*2||c>sum)
                    {
                        p[i]++;
                        p[j]++;
                    }
                    else
                    {
                        if(i!=n) printf("%c",i+'A'),sum--;
                        if(j!=n) printf("%c",j+'A'),sum--;
                        printf(" ");
                        i = j = n;
                        break;
                    }
                }
            }
        }
        printf("\n");
    }
}
