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
    //freopen("input.txt","r",stdin);
    //freopen("output.txt","w",stdout);
    string s;
    cin >> t;
    
    for(j=1;j<=t;j++) {
               cin >> n >> s;
               l = 0;
               k = 0;
               for(i=0;i<s.size();i++) {
                                l = l + (int)(s[i]-48);
                                if(l<=i) {
                                        l++;
                                        k++;
                                }
               }
               
               printf("Case #%lld: %lld\n",j,k);
    }
    
     
    return 0;
}
