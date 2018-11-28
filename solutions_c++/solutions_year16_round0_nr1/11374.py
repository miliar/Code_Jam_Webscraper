#include<cstdio>
#include<cstdlib>
#include<set>

using namespace std;

set<int> z;

int main()
{
    int n,t;
    scanf("%d",&t);
    int ret=t;
    while(t--)
    {
        scanf("%d",&n);
        int f=n;
        if(n==0)
        {
            printf("Case #%d: INSOMNIA\n",ret-t);
        }
        else
        {
            int mul=1,i;
            z.clear();
            while(z.size() < 10)
            {
                int m=n;
                for(i=1;i<=m;i*=10)
                {

                }
                i/=10;
                //printf("%d %d\n",m,i);
                for(;m > 0;i/=10)
                {
                    z.insert(m%10);
                    m=m/10;
                }
                n+=f;
                //printf("%d ",n*mul-1);
            }
            printf("Case #%d: %d\n",ret-t,n-f);
        }
    }
    return 0;
}
