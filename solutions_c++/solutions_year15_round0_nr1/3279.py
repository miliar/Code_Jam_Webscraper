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
    int t,T,i,n;
    char s[1005];
    scanf("%d",&t),T=t;
    while(t--)
    {
        scanf("%d %s",&n,&s);
        int L=0,c=0,res=0;
        for(i=0;i<=n;i++)
        {
            if(s[i]>48)
            {
                if(c<L)res+=L-c,c=L;
            }
            c+=s[i]-48;L++;
        }
        printf("Case #%d: %d\n",T-t,res);
    }

    return 0;
}
