#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int a[1005];
int n;
int main()
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int t,ca=0;
    char ch;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%d",&n);getchar();
        for(int i=0;i<=n;i++)
        {
                scanf("%c",&ch);
                a[i]=ch-'0';
        }
        int sum=a[0],ret=0;
        for(int i=1;i<=n;i++)
        {
            if(sum<i)
            {
                    ret+=i-sum;
                    sum=i+a[i];
            }
            else sum+=a[i];
        }
        printf("Case #%d: %d\n",++ca,ret);
    }
    return 0;
}
