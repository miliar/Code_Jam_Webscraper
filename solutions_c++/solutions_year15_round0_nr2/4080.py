
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
int d;
int p[1005];
int ada[1005];
map<vector<int>,int> mymap;

int f(vector<int> v)
{
    if (mymap.find(v)!=mymap.end()) return mymap[v];
    int &res = mymap[v];
    res = INF;
    for (int i=v.size()-1;i>=0;i--)
    {
        if (v[i]==0) continue;
        res = min(res, i);

        for (int j=1;j<i;j++)
        {
            v[j]+=v[i];
            v[i-j]+=v[i];

            int add = v[i];
            v[i] = 0;
            res = min(res, add + f(v));
            v[i] = add;

            v[j]-=v[i];
            v[i-j]-=v[i];
        }
        break;
    }
    return res;
}

int main()
{
    scanf("%d",&t);

    for (int tc=1;tc<=t;tc++)
    {
        scanf("%d",&d);
        for (int i=0;i<d;i++) scanf("%d",&p[i]);

        int ans = INF;

        vector<int> v(10, 0);

        for (int i=0;i<d;i++) v[p[i]]++;

        ans = f(v);

        printf("Case #%d: %d\n",tc,ans);

    }

    return 0;
}
