#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <fstream>
using namespace std;

const int N = 1E3+7;
int a[N],t,cas,n,now,ans;
char st[N];

int main()
{
    freopen("A-small-attempt1.in", "r", stdin);
	freopen("slyar1.out", "w", stdout);

	/* 中间按原样写代码，什么都不用修改 */


    memset(st,' ',sizeof(st));
    scanf("%d",&t);
    cas = 1;
    while ( cas <= t )
    {
        memset(a,0,sizeof(a));
        scanf("%d",&n);
        scanf("%s",st);
        for ( int i = 0 ; i <= n ; i++ )
        {
            a[i] =(int) (st[i]-'0');
//            cout<<"a[i]:"<<a[i]<<endl;
        }
        now = a[0];
        ans = 0;

        for ( int i  = 1 ; i <= n ; i++ )
        {

            if ( a[i]==0 ) continue;

        //    cout<<"i:"<<i<<"ans:"<<ans<<
         //         "now："<<now<<endl;
            if ( now>=i )
            {
                now = now + a[i];
            }
            else
            {
                ans = ans + ( i - now );
                now = now +( i-now );
                now = now + a[i];
            }

        }
        printf("Case #%d: %d\n",cas,ans);
        cas++;

    }
    fclose(stdin);
	fclose(stdout);
    return 0;
}
