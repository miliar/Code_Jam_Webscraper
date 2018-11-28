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
int main()
{
    freopen("D-small-attempt1.in","r",stdin);
    freopen("D-small-attempt1.out","w",stdout);
    int t;
    int kas = 0;
    scanf("%d",&t);
    while(t--)
    {
        int x,r,c;
        scanf("%d %d %d",&x,&r,&c);
        if(r > c)
            swap(r,c);
        string ans = "";
        if(x == 1)
        {
            ans = "GABRIEL";
        }
        else if(x == 2)
        {
            if((r*c)&1)
            {
                ans = "RICHARD";
            }
            else
            {
                ans = "GABRIEL";
            }
        }
        else if(x == 3)
        {
            if((r == 2 && c == 3) || (r == 3 && c == 4) || (r==3 && c==3))
            {
                ans = "GABRIEL";
            }
            else
            {
                ans = "RICHARD";
            }
        }
        else
        {
            if(r*c >= 12)
            {
                ans = "GABRIEL";
            }
            else
            {
                ans = "RICHARD";
            }
        }
        kas++;
        printf("Case #%d: %s\n",kas,ans.c_str());
    }
return 0;
}
