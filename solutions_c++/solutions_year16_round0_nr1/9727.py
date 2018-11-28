#include <iostream>
#include<string>
#include<cstring>
#include<vector>
#include<set>
#include<stack>
#include<queue>
#include<list>
#include<cmath>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<fstream>
#include<map>
#include<iomanip>
using namespace std;
#define whiel while
#define null NULL
#define eps 1e-8
#define INF 0x3f3f3f
#define lson l,m,rt<<1
#define rson m+1,r,rt<<1|1
#define read(x) scanf("%d",&x)
using namespace std;
int getnext(int now , int n )
{
    if(now == n)
    {
        return 1 ;
    }
    else
        return now+1 ;




}

int main()
{
#ifndef ONLINE_JUDGE
//   freopen("C:\\Users\\wyy\\Desktop\\input.txt","r",stdin);
#endif
    ios::sync_with_stdio(false);//无法用scanf和输入挂
    long long  n;
    while(cin>>n)
    {
        long long locpre=-1;
        long long locafter=-1 ;
        long long mi = 2000000000;
        long long tmp ;
        for(long long i= 1 ; i<= n ; i++)
        {
            cin>>tmp;
            if(tmp<=mi)
            {
                if(tmp<mi)
                {
                    locafter=locpre=i;
                    mi=tmp;

                }
                else
                {
                    if(locafter==-1)
                    {
                        locafter=locpre=i;

                    }
                    else
                    {
                        locafter=i;
                    }

                }
            }

        }
        cout<<n-locafter<<endl;
        cout<<mi*n<<endl;
        cout<<locpre<<endl;
        long long ans = (n-locafter)+mi*n+locpre;
        cout<<ans-1<<endl;





    }












    return 0;
}
