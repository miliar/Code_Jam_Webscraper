#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <stack>
#include <set>
#include <vector>

using namespace std;

typedef long long    LL;
typedef vector <int> VI;
typedef vector <LL>  VL;
typedef vector <VI>  VVI;
typedef vector <VL>  VVL;

// Input Macros
#define s(n)               scanf("%d",&n)
#define sl(n)              scanf("%lld",&n)
#define sc(n)              scanf("%c",&n)
#define sf(n)              scanf("%lf",&n)
#define ss(n)              scanf("%s",n)

// Output Macros
#define p(n)               printf("%d\n",n)
#define pl(n)              printf("%lld\n",n)

// Useful Hardware Instructions
#define bitcount           __builtin_popcount
#define gcd                __gcd

// Useful Container Manipulation / Traversal Macros
#define forall(i,a,b)      for(int i=a; i<b; i++)
#define foreach(itr, c)    for( typeof((c).begin()) itr = (c).begin();  itr != (c).end(); ++itr)
#define whole(a)           a.begin(), a.end()
#define in(a,b)            ((b).find(a) != (b).end())
#define pb                 push_back
#define pf 				   push_front
#define fill(a,v)          memset(a, v, sizeof a)
#define mp                 make_pair

// Some Useful Functions
#define maX(a,b)           ((a) > (b) ? (a) : (b))
#define miN(a,b)           ((a) < (b) ? (a) : (b))

// Useful Constants
#define MOD 			   1000000007
#define INF                (int)1e9
#define EPS                1e-9
#define MAX                100002

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    s(T);
    int testCase = 0;
    while(T--)
    {
        testCase++;
        int sm;
        s(sm);
        string s;
        cin>>s;
        int ans = 0;
        int now = 0;
        for(int i=0; i<s.size(); i++)
        {
            if(now >= i)
                now += (s[i]-'0');
            else
            {
                ans += (i-now);
                now += (s[i]-'0')+(i-now);
            }
        }
        printf("Case #%d: %d\n", testCase, ans);
    }
    return 0;
}
