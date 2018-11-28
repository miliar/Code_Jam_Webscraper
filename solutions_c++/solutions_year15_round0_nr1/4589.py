
#include <stdio.h>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <cmath>
#include <string.h>
#include <string>
#include <algorithm>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <limits.h>
#include <time.h>
#include <bitset>
#include <list>
#include <cassert>

#define EPS 1e-11
#define PI acos(-1)
#define LL long long
#define INF 1000000009
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define SZ(a) ((int)a.size())
#define OPENR(a) freopen(a,"r",stdin)
#define OPENW(a) freopen(a,"w",stdout)
#define pii pair<int,int>

int x4[4] = { 0, 0,-1, 1};
int y4[4] = {-1, 1, 0, 0};
int x8[8] = {-1,-1,-1, 0, 0, 1, 1, 1};
int y8[8] = {-1, 0, 1,-1, 1,-1, 0, 1};
int xhorse[8] = {1,2,1,2,-1,-2,-1,-2};
int yhorse[8] = {2,1,-2,-1,2,1,-2,-1};

using namespace std;

int t;
int s;

char ar[1005];

int main()
{
    scanf("%d",&t);

    for (int tc=1;tc<=t;tc++) {
        printf("Case #%d: ", tc);

        scanf("%d %s",&s, ar);

        int ans = 0;
        int cur = 0;
        for (int i=0;i<=s;i++)
        {
            if (ar[i]=='0') continue;

            if (i==0)
                cur += ar[i]-48;
            else
            {
                if (cur>=i)
                {
                    cur += ar[i]-48;
                }
                else
                {
                    ans += i-cur;
                    cur = i + ar[i]-48;
                }
            }
        }

        printf("%d\n",ans);
    }

    return 0;
}
