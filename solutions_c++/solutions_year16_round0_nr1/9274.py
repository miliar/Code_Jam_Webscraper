#include <bits/stdc++.h>
using namespace std;

int main()
{
    //freopen("A-large.in","r",stdin); freopen("A-large.out","w",stdout);
    int t,n; cin >> t;
    for(int alwfkbn = 0; alwfkbn < t; alwfkbn++)
    {
        scanf("%d",&n);
        bool success=false;
        int a[10]={0,1,2,3,4,5,6,7,8,9},sn=-1,cur=10;
        for(long i = 1; i < 5001; i++)
        {
            bool loop = true;
            long long ni=n*i;
            if(i>1&&ni==n*i-1)
                break;
            while(loop)
            {
                if(ni>9)
                {
                    if(binary_search(a,a+cur,(ni%10)))
                    {
                        remove(a,a+cur,ni%10);
                        cur--;
                    }
                    ni/=10;
                }
                else
                {
                    if(binary_search(a,a+cur,ni))
                    {
                        remove(a,a+cur,ni);
                        cur--;
                    }
                    loop=false;
                }
            }
            if(!cur)
            {
                sn=i*n ;
                success=true;
                break;
            }
        }
        if(success)
            printf("Case #%d: %d\n",alwfkbn+1,sn);
        else printf("Case #%d: INSOMNIA\n",alwfkbn+1);
    }
}
