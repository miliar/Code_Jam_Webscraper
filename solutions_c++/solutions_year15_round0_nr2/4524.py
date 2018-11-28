/* HellGeek */
/* Shiva Bhalla */
/* iit2012077 */
 
#include<stdio.h>
#include<vector>
#include<map>
#include<utility>
#include<algorithm>
#include<set>
#include<string>
#include<string.h>
#include<time.h>
#include<iostream>
#include<queue>
#include<stack>
#include<math.h>

#define LL long long
#define FIT(i,t) for(i=0;i<t;i++)
#define FIN(i,n) for(i=0;i<n;i++)
#define FJT(j,t) for(j=0;j<t;j++)
#define FJN(j,n) for(j=0;j<n;j++)
#define MAX2(a,b) a>b?a:b
#define MIN2(a,b) a>b?b:a
#define REP(i,a,b) for(i=a;i<=b;i++)

using namespace std;

int main()
{
 LL i,j,k,l,n,m,t;
 
 freopen("output.txt","w",stdout);
 
 cin >> t;
 LL arr[10005];
 for(i=1;i<=t;i++) {
                   cin >> n;
                   m = 0;
                   for(j=0;j<n;j++) {
                                   cin >> arr[j];
                                   m = max(m,arr[j]);
                   }
                   LL res = 99999999;
                   for(j=1;j<=m;j++) {
                                     LL tr = 0;
                                     LL tot = 0;
                                     for(k=0;k<n;k++) {
                                                      if(arr[k] > j) {
                                                                tr = tr + arr[k]/j - 1;
                                                                if(arr[k]%j!=0)
                                                                tr++;
                                                                tot = max(tot, j);
                                                      }
                                                      else
                                                      tot = max(tot, arr[k]);
                                                      
                                     }
                                     tr = tr + tot;
                                     res = min(res,tr);
                   }
                   printf("Case #%lld: %lld\n",i,res);
 }
 
 return 0;
}
