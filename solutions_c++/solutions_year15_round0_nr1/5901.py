# include<cstdio>
# include<iostream>
# include<fstream>
# include<algorithm>
# include<functional>
# include<cstring>
# include<string>
# include<cstdlib>
# include<iomanip>
# include<numeric>
# include<cctype>
# include<cmath>
# include<ctime>
# include<queue>
# include<stack>
# include<list>
# include<set>
# include<map>

using namespace std;

const double PI=4.0*atan(1.0);

typedef long long LL;
typedef unsigned long long ULL;

# define inf 999999999
# define MAX 1234

char s[MAX];
int a[MAX];

int main(void)
{
   freopen("A-large.in","r",stdin);
    freopen("aaalarge.out","w",stdout);

    int icase = 1;
    int t;cin>>t;
    while ( t-- )
    {
        memset(s,0,sizeof(s));
        memset(a,0,sizeof(a));
        int n;cin>>n;
        scanf("%s",s);
        for ( int i = 0;i <= n;i++ )
        {
            a[i] = s[i]-'0';
        }
        int sum = 0, tot = 0;
        for ( int i = 0;i <= n;i++ )
        {
            if ( sum < i && a[i]!=0 )
            {
                tot+=i-sum;
                sum+=i-sum;
            }
            sum+=a[i];
        }
        printf("Case #%d: %d\n",icase++,tot);
    }



	return 0;
}
