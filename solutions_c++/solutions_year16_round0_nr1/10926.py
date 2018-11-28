#include<bits/stdc++.h>
using namespace std;
bool num[12];
int main()
{
    long long int n, t, i,j,a;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    scanf("%lld",&t);

    for(a=1; a<=t; a++)
    {
        memset(num, 0, sizeof num);
        scanf("%d",&n);
        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",a);
            continue;
        }
            long long int sum = 1;
            long long int x;
            long long int cnt = 1;
            for(i=1;cnt<=10;i++)
            {
                sum = i * n;
                j = sum;
                while(sum!=0)
                {
                    x = sum%10;
                    sum = sum/10;

                    if(num[x]==0)
                    {
                        num[x] = 1;
                        cnt++;
                    }
                }
            }
            printf("Case #%lld: %d\n",a,j);
        }
        return 0;
}
