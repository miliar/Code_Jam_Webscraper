#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
using namespace std;
int T;
char s[1010];
int main()
{
    freopen("a.in","r",stdin);
    freopen("b.txt","w",stdout);
    int T,ca=0;
    scanf("%d",&T);
    while(T--)
    {
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int ans=0;
        int num=0;
        for(int i=0;i<=n;i++)
        {
            int x=s[i]-'0';
            if(num>=i)
            {
                num+=x;
            }
            else
            {
                ans+=(i-num);
                //num+=i-num;
                num=i+x;
            }
        }
        printf("Case #%d: %d\n",++ca,ans);
    }

    return 0;
}
