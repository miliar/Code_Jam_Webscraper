#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#define FOR(i,k,n) for(int i=k; i<n; i++)

using namespace std;

double a[1001], b[1001];

int war(int ab, int ae, int bb, int be)
{
    int ret = 0;

    vector<double> v(b+bb, b+be);
    vector<double>::iterator it;
    for(int i=ae-1; i>=ab; i--)
    {
        it = lower_bound(v.begin(), v.end(), a[i]);
        if (it == v.end())
        {
            ret++;
            v.erase(v.begin());
        }
        else v.erase(it);
    }

    return ret;
}

int dwar(int ab, int ae, int bb, int be)
{
    int ret = 0;

    vector<double> v(a+ab, a+ae), u(b+bb, b+be);
    vector<double>::iterator it;

    while(v.size())
    {
        it = lower_bound(v.begin(), v.end(), u[0]);
        if (it == v.end()) break;
        v.erase(it); u.erase(u.begin()); ret++;
    }

    return ret;
}

int main()
{
    //freopen("D-large.in", "r", stdin);
    //freopen("D-large.out", "w", stdout);

    int T;
    int n, y, z;

    scanf("%d", &T);
    for(int ncaso=1; ncaso<=T; ncaso++)
    {
        scanf("%d", &n);
        FOR(i,0,n) scanf("%lf", &a[i]); sort(a, a+n);
        FOR(i,0,n) scanf("%lf", &b[i]); sort(b, b+n);

        y = dwar(0,n,0,n);
        z = war(0,n,0,n);

        printf("Case #%d: %d %d\n", ncaso, y, z);
    }

    return 0;
}
