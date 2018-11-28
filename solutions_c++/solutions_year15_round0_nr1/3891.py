#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
#define M 1009
char s[M];
int sum[M];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("large.out", "w", stdout);
    int t;
    scanf("%d",&t);
    int k = 1;
    while(t--)
    {
        memset(s,'\0',sizeof(s));
        memset(sum,0,sizeof(sum));
        int n;
        scanf("%d",&n);
        scanf("%s",s);
        int ans = 0;
        sum[0] = s[0]-'0';
        for(int i = 1;i <= n;i++)
        {
            if(sum[i-1]-i<0 && s[i]!='0')
            {
                ans = ans +(i-sum[i-1]);
                sum[i] = sum[i-1]+s[i]-'0'+(i-sum[i-1]);
            }
            else
            sum[i] = sum[i-1]+s[i]-'0';
        }
        printf("Case #%d: %d\n",k++,ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
