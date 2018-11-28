#include<stdio.h>
using namespace std;
int main()
{
    freopen("C:\\Users\\Aditya\\Downloads\\A-large.in","r",stdin);
    freopen("C:\\Users\\Aditya\\Documents\\out.txt","w",stdout);
    int t,sum,count,tc=0,n,i,x;
    char st[1002];
    scanf("%d",&t);
    while(t--)
    {
        tc++;
        sum =0;
        count =0;
        scanf("%d %s",&n,st);
        for(i=0;i<=n;i++)
        {
            if(i-sum>0)
            {
                count+=i-sum;
                sum+=i-sum;
            }
            x=st[i]-'0';
            sum+=x;
        }
        printf("Case #%d: %d\n",tc,count);
    }
    return 0;
}
