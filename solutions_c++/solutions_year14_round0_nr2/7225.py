#include <cstdio>
#include <stdlib.h>
#include <cstring>
#include <iostream>
#include <stdlib.h>
#include <string>
#include <math.h>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <limits.h>
#define s(a) scanf("%d",&a)
#define sl(a) scanf("%lld",&a)
#define p(a) printf("%d ",a)
#define pl(a) printf("%lld\n",a)
#define SIZE 100000
#define M 1000000007
#define SWAP(a,b) a= a^b, b=a^b, a=a^b
#define Z(a) memset(a,0,sizeof(a))
using namespace std;
typedef long long int ll;

/*inline int fastread()		// this is little bit slow compared to above one
{
    int i=0;
    char c=0;
    while (c<33)
        c=getchar_unlocked();
    while (c>33)
    {
		i = i*10+c-'0';
		c=getchar_unlocked();
    }
    return i;
} */
double a[SIZE];
int main()
{
    freopen("B-large.in","r",stdin);
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j,k;
    double total_time,expected_time,c,f,x,rate,temp,ans;
    s(t);
    for(i=1;i<=t;i++)
    {
       cin>>c>>f>>x;
       rate=2;
       a[0]=x/rate;
       total_time=0;
       for(j=1;a[j-1]<=a[0];j++)
       {
           total_time+=(c/rate);
           rate+=f;
           a[j]=total_time+(x/rate);
           if(a[j]>a[j-1])
           {
               ans=a[j-1];
               break;
           }
       }
        printf("Case #%d: %0.7lf\n",i,ans);
    }
}
