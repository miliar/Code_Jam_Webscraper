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

char s[500];

int main()
{

#ifdef One_1
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
#endif // One_1


    LL i,j,k,n,t=1,tc;

    read(tc);

    while(tc--)
    {
        scanf("%s",s);

        for(i=strlen(s)-1; i>=0; i--)
        {
            if(s[i]!='+') break;
        }

        if(i<0)
        {
            printf("Case #%lld: 0\n",t++);
            continue;
        }

        k=1;

        for(j=1;j<=i;j++)
        {
            if(s[j]!=s[j-1]) k++;
        }

        printf("Case #%lld: %lld\n",t++,k);
    }

    return 0;
}
