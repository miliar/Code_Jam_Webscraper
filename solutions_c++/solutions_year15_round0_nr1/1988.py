#include<iostream>
#include<stdio.h>
using namespace std;
const int maxn=1005;
char s[maxn];

void work()
{
    int sum=0,ans=0,n;
    scanf("%d",&n);
    scanf("%s",s);
   // cout<<n<<endl;
    //cout<<s<<endl;
    for (int i=0;i<=n;i++)
    {
        if (s[i]!='0' && sum<i)
        {
            ans+=i-sum;
            sum=i;
        }
        sum+=s[i]-'0';
    }
    printf("%d\n",ans);
}
int main()
{
    //freopen("A-large.in","r",stdin);
   // freopen("large.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while (T--)
    {
        cas++;
        printf("Case #%d: ",cas);
        work();
    }
}
