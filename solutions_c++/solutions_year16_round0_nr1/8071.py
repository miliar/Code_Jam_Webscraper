#include <iostream>
#include<cstdio>
#include<cstring>
using namespace std;
int t,f[20],n;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    for(int tid=1;tid<=t;tid++)
    {
        memset(f,0,sizeof(f));
        int left=10;
        scanf("%d",&n);
        long long k=0;
        while(k<1000000&&left>0)
        {
            k++;
            long long tmp=k*n;
            while(tmp)
            {
                int tt=tmp%10;
                tmp/=10;
                if(f[tt]==0)
                {
                    f[tt]=1;
                    left--;
                }
            }
        }
        if(left==0) printf("Case #%d: %I64d\n",tid,k*n);
        else printf("Case #%d: INSOMNIA\n",tid);
    }
    return 0;
}
