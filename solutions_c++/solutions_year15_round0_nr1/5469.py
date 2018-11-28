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
int t;
int n;
int pst,ct,k=0;
char str[100005];
int main()
{
  scanf("%d",&t);
  while(t--)
  {
     scanf("%d",&n);
     scanf("%s",str);
     pst=0;
     ct=0;
     for(int i=0;i<n+1;i++)
     {
          if(i<=pst)
          pst+=str[i]-'0';
          else
          {
             ct+=i-pst;
             pst+=i-pst;
             pst+=str[i]-'0';
           }
     }
     ++k;
     printf("Case #%d: %d\n",k,ct);
     }
     return 0;
}