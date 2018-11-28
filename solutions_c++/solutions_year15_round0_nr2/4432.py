#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <sstream>
#include <cstring>
#include <stack>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <climits>

#define ll long long
#define MAX(x,y) (((x)>(y))?(x):(y))
#define MIN(x,y) (((x)<(y))?(x):(y))
#define FOR(i,j,k) for(int i=j;i<=(k);i++)
#define REP(i,n)  for(int i=0;i<(n);i++)
#define mst(x,y) memset(x,y,sizeof(x))
#define eps 1e-5
#define INF 0x3f3f3f3f

using namespace std;

int arr[1500] ;
int T,cnt=0,n;

int main() {
    //freopen("B-small-attempt0.in","r",stdin) ;
    //freopen("out.out","w",stdout) ;
    scanf("%d", &T) ;
    for(int cnt = 1;cnt<=T;cnt++)
    {
        int maxmax,minmin,sum ;
        scanf("%d",&n) ;
        for(int i=0;i<n;i++) {
            scanf("%d",&arr[i]) ;
            maxmax = (maxmax>arr[i]?maxmax:arr[i]) ;
        }
        minmin = maxmax ;
        for(int i=1;i<=maxmax;i++) {
            sum = i;
            for(int j=0;j<n;j++) {
                if(arr[j]>i) {
                    if(arr[j]%i == 0)
                        sum += (arr[j]/i-1) ;
                    else
                        sum += (arr[j]/i) ;
                }
            }
            minmin = min(minmin,sum) ;
        }
        printf("Case #%d: %d\n",cnt, minmin) ;
    }
    return 0 ;
}

