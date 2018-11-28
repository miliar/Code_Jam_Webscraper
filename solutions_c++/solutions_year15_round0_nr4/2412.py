/*_______SHREY MANIK______*/
#include <iostream>
#include <string>
#include <climits>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <cstring>
#include <iomanip>
#define MOD 1000000007
#define LL long long
#define SET(a) memset(a,-1,sizeof(a))
#define CLEAR(a) memset(a,0,sizeof(a))
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
using namespace std;
template<class T>T gcd(T a,T b){return (b==0)?a:gcd(b,a%b);}
template<class T>T lcm(T a,T b){return (a*b)/gcd(a,b);}
LL t,x,r,c,ans;
LL k=0;
int main()
{
 scanf("%lld",&t);
 while(t--)
 {
 	++k;
 	scanf("%lld %lld %lld",&x,&r,&c);
 	ans=r*c;
 	if(x==1)
 	{
 	printf("Case #%lld: GABRIEL\n",k);
 	}
 	else if(x==2)
 	{
 	if(ans%2==0)
 	printf("Case #%lld: GABRIEL\n",k);
 	else printf("Case #%lld: RICHARD\n",k);
 	}
 	else if(x==3)
 	{
 	if(ans%3==0)
 	{
 	if(ans==6 || ans==9 || ans==12 || ans==15)
 	printf("Case #%lld: GABRIEL\n",k);
 	else printf("Case #%lld: RICHARD\n",k);
 	}
 	else printf("Case #%lld: RICHARD\n",k);
 	}
 	else if(x==4)
 	{
 	if(ans%4==0)
 	{
 	if(ans==12 || ans==16)
 	printf("Case #%lld: GABRIEL\n",k);
 	else printf("Case #%lld: RICHARD\n",k);
 	}
 	else printf("Case #%lld: RICHARD\n",k);
 	}
 }
 return 0;
}