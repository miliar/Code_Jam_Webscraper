//RandomUsername(Nikola Jovanovic)
//Google CodeJam Round B1
//A

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#define MAXN 150
#define forr(i) for(int i=1;i<=r;i++)
#define forc(i) for(int i=1;i<=c;i++)

using namespace std;

int t,a,b,k;
long long sum;

int main()
{
   // freopen("in.in","r",stdin);
   // freopen("out.txt","w",stdout);
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++)
    {
        sum=0;
        scanf("%d %d %d",&a,&b,&k);
        //cout<<(0&0)<<endl;
        for(int i=0;i<a;i++)
          for(int j=0;j<b;j++)
           {
            //  cout<<(i&j<<" "<<k<<endl;
             if((i&j)<k) { sum++;}
           }
        printf("Case #%d: %lld\n",tt,sum);
    }
    return 0;
}
