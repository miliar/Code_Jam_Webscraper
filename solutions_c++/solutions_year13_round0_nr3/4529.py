#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<list>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<iterator>
#include<algorithm>
#include<stack>
#include<queue>
using namespace std;

int palindrom(int n)
{
    int sum=0,k=n;
    while(k>0)
    {
        sum=sum*10+k%10;
        k/=10;
    }
    if(sum==n)
        return 1;
    return 0;
}
int main()
{
    int t,cas=1,a,b;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d%d",&a,&b);
        printf("Case #%d: ",cas++);
        int ans=0;
        for(int i=a;i<=b;i++)
        {
            int k=sqrt(i*1.0);
            if((k*k==i)&&palindrom(i)&&palindrom(k))
                ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
