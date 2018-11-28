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


bool flag[NN];

void sieve()
{
    for(int i=4; i<NN; i+=2) flag[i]=1;

    for(int i=3; i*i<NN; i+=2)
    {
        if(flag[i]==0)
        {
            for(int j=i*i; j<NN; j+=2*i) flag[j]=1;
        }
    }
}

LL conv(string s,LL b)
{
    LL i,sum=0,k=1;

    for(i=s.size()-1; i>=0; i--)
    {
        sum+=(s[i]-'0')*k;
        k*=b;
    }

    return sum;
}

LL div(LL n)
{
    LL sq=1+sqrt(n*1.0);

    for(int i=2; i<=sq; i++)
    {
        if(n%i==0) return i;
    }

    return 0;
}

int main()
{

#ifdef One_1
    freopen("C-small-attempt1.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif // One_1

    sieve();

    LL i,ii,j,k,n,t=1,tc;
    bitset<16> bin;
    string s;

    read(tc);

    while(tc--)
    {
        read(n);
        read(j);

        printf("Case #%lld:\n",t++);

        LL x=(1<<(n-1));
        LL y=(1<<(n-2));

        for(i=0; i<y && j; i++)
        {
            k=(i*2)+x+1;

            if(flag[k])
            {
                bin = k;
                s=bin.to_string();

                LL ans[15];

                ans[2]=div(k);

                if(ans[2]==0) continue;

                for(ii=3; ii<=10; ii++)
                {
                    ans[ii]=div(conv(s,ii));
                    if(ans[ii]==0) goto xxx;
                }

                printf("%s",s.c_str());

                for(ii=2;ii<=10;ii++) printf(" %lld",ans[ii]);

                puts("");

                j--;

xxx:
                continue;

            }
        }
    }

    return 0;
}
