//BISMILLAHIR RAHMANIR RAHIM
// OUM NAMA MA SWARASATI

#include<cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<fstream>
#include<string>
#include<vector>
#include<queue>
#include<map>
#include<set>
#include<sstream>
#include<stack>
#include<stdlib.h>
#include<iostream>
#include<algorithm>

#define AB push_back
#define MB pop_back
#define CL(vctr) vctr.clear()
#define MS(v,ar) memset(ar,v,sizeof(ar))
#define MP make_pair
#define F first
#define S second

#define MX(a,b) a>b?a:b
#define MN(a,b) a<b?a:b
#define ABS(x) x>0?x:-x

#define INF 1<<30
#define PI 2 * acos( 0 )
#define EPS 1E-9
#define SZ 100000+5
#define MOD 1000000000+7

using namespace std;
typedef long long int ll;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T,i,j,d,p[1005];
//    tm[1]=1;tm[2]=2;pm[1]=1;pm[2]=2;
//    for(i=3;i<1001;i++)
//    {
//        m1=i/2,m2=i-m1;h1=h2=1;
//        if(h1>)
//        for(j=1;ans<i;j++)
//        {
//
//        }
//    }
    scanf("%d",&t),T=t;
    while(t--)
    {
        scanf("%d",&d);
        int c,res=0;
        for(i=0;i<d;i++)
        {
            scanf("%d",p+i);
            res=max(res,p[i]);
        }
        for(i=1;i<1001;i++)
        {
            c=0;
            for(j=0;j<d;j++)
            {
                c+=p[j]/i;
                if(!(p[j]%i))c--;
            }
            c+=i;
            if(res>c)res=c;
        }
        printf("Case #%d: %d\n",T-t,res);
    }

    return 0;
}
