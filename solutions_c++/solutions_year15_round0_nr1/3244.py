#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int num[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,summ,now,n,m;
    char c;
    scanf("%d",&T);
    for(int L=1;L<=T;++L)
    {
        summ=0;
        now=0;
        scanf("%d",&n);
        getchar();
        for(int i=0;i<=n;++i)
        {
            c=getchar();
            m=c-'0';
            if(i==0)
            {
                now+=m;
            }
            else
            {
                if(now>=i)
                    now+=m;
                else
                {
                    summ+=i-now;
                    now=i+m;
                }
            }
        }
        printf("Case #%d: %d\n",L,summ);
    }
    return 0;
}
