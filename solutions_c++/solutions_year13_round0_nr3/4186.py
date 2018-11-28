#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<stdio.h>
#include<string.h>
#include<map>
#include<vector>
#include<math.h>
typedef __int64 i64;
using namespace std;
__int64 pra[40]={
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
2001002};
int main()
{
    int t;
    freopen("C-large-1.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d",&t);
    int casee,j,k;
    __int64 i;
    __int64 ll,rr;
    i64 a,b;
    int res;
    int index;
    for(casee=1;casee<=t;casee++)
    {
        scanf("%I64d%I64d",&ll,&rr);
        int cnt=0;
        a=sqrt(ll*1.0),b=sqrt(rr*1.0);
        if(a*a<ll) a++;
        
        for(index=0;index<39;index++)
        {
            if(pra[index]>=a&&pra[index]<=b) cnt++;
        }
        printf("Case #%d: %d\n",casee,cnt);
    }
    return 0;
}