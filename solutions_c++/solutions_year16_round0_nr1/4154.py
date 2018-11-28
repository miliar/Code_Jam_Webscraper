/**
 *    @author     : Dipta Das
 *    @University : CUET CSE 11
 *    @Codeforces : diptadas
 *    @Topcoder   : dipta670
 *    @link       : www.fb.com/dipta.das
 */

#include <bits/stdc++.h>
using namespace std;

#define LL         long long
#define pll        pair<LL,LL>
#define mp         make_pair
#define fr         first
#define sc         second
#define pb         push_back

#define read(n)    scanf("%lld",&n)
#define mset(a,s)  memset(a,s,sizeof(a))
#define all(a)     a.begin(),a.end()

#define PI         acos(-1.0)
#define EPS        1e-9
#define MOD        1000000007
#define INF        1e9
#define NN         1000009

int main()
{

#ifdef One_1
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif // One_1


    LL i,j,k,n,t=1,tc;

    read(tc);

    while(tc--)
    {
        read(n);

        //n=tc;

        if(n==0)
        {
            printf("Case #%lld: INSOMNIA\n",t++);
            continue;
        }

        bool a[10]= {0};

        LL sum=0;

        for(i=0; i<1001; i++)
        {
            sum+=n;

            k=sum;

            while(k)
            {
                a[k%10]=1;
                k/=10;
            }

            for(j=0; j<10; j++) if(!a[j]) break;

            if(j==10) break;
        }

        if(i<1001)
            printf("Case #%lld: %lld\n",t++,sum);
        else
            printf("Case #%lld: INSOMNIA\n",t++);
    }

    return 0;
}
