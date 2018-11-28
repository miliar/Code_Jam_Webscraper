                  /* Original Author: Akash Sinha(sinaka) 
                       Problem Code:
                       Language: c++
                    */
using namespace std;
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <bitset>
//#include<conio.h>

//DEFINITIONS

#define LL  long long int
#define ULL  unsigned long long int
#define DB double
#define LDB long double
#define PB push_back
#define MP make_pair
#define SL(a) scanf("%lld",&a)
#define S(a) scanf("%d",&a)
#define SC(a) scanf("%c",&ch)
#define SD(a) scanf("%lf",&a)
#define PL(a) printf("%lld",a)
#define P(a) printf("%d",a)
#define PC(a) printf("%c",a)
#define PD(a) printf("%lf",a)
#define max(a,b) (a>b?a:b)
#define min(a,b) (a<b?a:b)
#define NL printf("\n")
#define W(t) while(t--)
#define FOR(i,lo,hi) for(i=lo;i<hi;i++)
#define gc getchar_unlocked
#define MOD 1000000007
int main()
{
    freopen("C:\\Users\\suyash\\Desktop\\input.txt","r",stdin);
    freopen("C:\\Users\\suyash\\Desktop\\output.txt","w",stdout);
    int t,n,m,i,j,k,tc,cn,cm;
    int arr[105][105];
    bool flag;
    scanf("%d",&t);
    for(tc=1;tc<=t;tc++)
    {
       scanf("%d%d",&n,&m);
       flag=true;
       for(i=0;i<n;i++)
       for(j=0;j<m;j++)
       scanf("%d",&arr[i][j]);
       
       for(i=0;i<n;i++)
       {
          for(j=0;j<m;j++)
          if(arr[i][j]==1)
          {
             cn=0;cm=0;
             for(k=0;k<m;k++)
             if(arr[i][k]==1)
             cm++;
             for(k=0;k<n;k++)
             if(arr[k][j]==1)
             cn++;
             if((cn!=n)&&(cm!=m))
             {flag=false;break;}
          }
          if(!flag)
          break;
       }
       if(flag)
       printf("Case #%d: YES\n",tc);
       else
       printf("Case #%d: NO\n",tc);
    }
    //getch();
    return 0;
}
       
       
