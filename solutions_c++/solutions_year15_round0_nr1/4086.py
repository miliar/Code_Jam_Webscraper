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
char S[1005];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int kas = 0;
    while(t--)
    {
        int k;
        scanf("%d %s",&k,S);
        int len = k+1;
        int ans = 1000000;
        for(int i=0;i<=1010;i++)
        {
            int cur = i;
            int flag = 1;
            for(int j=0;j<len;j++)
            {
                if(S[j] == '0')
                    continue;
                if(cur < j)
                {
                    flag = 0;
                    break;
                }
                cur += (S[j]-'0');
            }
            if(flag)
            {
                ans = i;
                break;
            }
        }
        kas++;
        printf("Case #%d: %d\n",kas,ans);
    }
return 0;
}
