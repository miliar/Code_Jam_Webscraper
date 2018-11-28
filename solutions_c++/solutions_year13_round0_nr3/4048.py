#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
#include <cmath>
#include <stack>
#include <map>
#include <string>
#define LL long long
#define DB double
using namespace std;
int a[109];
int hui(LL k)
{
    int i,j;
    for(i=0;k>0;i++)
    {
        a[i] = k%10;
        k/=10;
    }
    for(j=0,i--;j<i;j++,i--)
    if(a[i]!=a[j]) return false;
    return true;
}
LL mp[]=
{0,
1,
2,
3,
11,
22,
101,
111,
121,
202,
212,
1001,
1111,
2002,
10001,
10101,
10201,
11011,
11111,
11211,
20002,
20102,
100001,
101101,
110011,
111111,
200002,
1000001,
1001001,
1002001,
1010101,
1011101,
1012101,
1100011,
1101011,
1102011,
1110111,
1111111,
2000002,
2001002
};
int main()
{
    //#ifndef ONLINE_JUDGE
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w+",stdout);
    //#endif
    int cas,T = 1;
    LL a,b;
    scanf("%d",&cas);
    while(cas--)
    {
        cin>>a>>b;
        int ans =0 ;
        for(int i=0;i<40;i++)
        if(a<=mp[i]*mp[i]&&mp[i]*mp[i]<=b)
        {
            ans++;
        }
        printf("Case #%d: %d\n",T++,ans);
    }
    return 0;
}
