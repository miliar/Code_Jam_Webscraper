/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <bitset>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
    for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define REP(i,a,n) for(int i=a;i<(int)n;i++)
#define pb push_back
#define mp make_pair
typedef long long ll;
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
int A[10005];
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    FOR(z,t)
    {
        int n,x;
        scanf("%d %d",&n,&x);
        FOR(i,n)
        {
            scanf("%d",&A[i]);
        }
        sort(A,A+n);
        int ans = 0;
        for(int i=0;i<n;i++)
        {
            if(A[i] == -1)
                continue;
            int flag = 0;
            for(int k=n-1;k>i;k--)
            {
                if(A[k] == -1)
                    continue;
                if(A[i] + A[k] <= x)
                {
                    flag = 1;
                    A[k] = -1;
                    ans++;
                   // cout << k << " " << ans << endl;
                    break;
                }
            }
            if(flag)
                continue;
            ans++;
        }
        printf("Case #%d: %d\n",z+1,ans);

    }
return 0;
}
