#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
    freopen("c1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T;
    int num[1001];
    scanf("%d",&T);
    for(int i = 0;i < 1001; ++i)
    num[i] = 0;
    for(int i = 1;i <= 31; ++i)
    {
        if(i > 10 && ((i%10) !=(i/10) ))
        continue;
        int tmp = i * i;
        if(tmp >= 100)
        {
            if((tmp % 10) == (int)(tmp / 100))
            {
                num[tmp] = 1;
                //printf("%d\n",tmp);
            }
        }
        else
        {
            if(tmp >= 10)
            {
                if((tmp % 10) == (int)(tmp / 10))
                {
                    num[tmp] = 1;
                    //printf("%d\n",tmp);
                }
            }
            if(tmp < 10)
            {
                num[tmp] = 1;
                //printf("%d\n",tmp);
            }
        }
    }
    for(int k = 0;k < T; ++k)
    {
        int a,b;
        int ans = 0;
        scanf("%d%d",&a,&b);
        for(int i = a;i <= b; ++i)
        {
            if(num[i] == 1)
                ans++;
        }
        printf("Case #%d: %d\n",k+1,ans);
    }
    return 0;
}
