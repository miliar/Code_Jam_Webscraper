#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
const int maxn = 1000+10;
char buf[maxn];
int n;


int main()
{
    freopen("./A-large.in","r",stdin);
    freopen("./a.out","w",stdout);
    int kase;
    scanf("%d",&kase);
    for(int z = 1;z <= kase;++z)
    {
        scanf("%d",&n);
        scanf("%s",buf);
        int sum = 0;
        int cnt = 0;
        for(int i = 0;i <= n;++i)
        {
            sum += buf[i]-'0';
            if(buf[i] != '0')
            {
                if(cnt >= i)
                    cnt += buf[i]-'0';
                else
                    cnt = i+buf[i]-'0';
            }
        }

        printf("Case #%d: %d\n",z,cnt-sum);
    }
    return 0;
}
