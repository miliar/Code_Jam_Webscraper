#include <bits/stdc++.h>
using namespace std;
char a[2000];
int main()
{

    int t,s;
    scanf("%d",&t);
    for(int test=1;test<=t;test++)
    {
        scanf("%d",&s);
        scanf("%s",a);
        int l=strlen(a);
        int ans=0;
        int sum=a[0]-'0';
        for(int i=1;i<l;i++)
        {
            if(i>sum&&a[i]!='0')
            {
                ans=ans+i-sum;
                sum=i+a[i]-'0';
            }
            else
            sum=sum+(a[i]-'0');
        }
        printf("Case #%d: %d\n",test,ans);
    }
    return 0;
}
