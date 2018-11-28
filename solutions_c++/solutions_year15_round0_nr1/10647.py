/*************************************************************************
	> File Name: a.cpp
	> Author: Zeleng Zhuang
	> Mail: zhuangzeleng19920731@gmail.com
	> Created Time: Sat Apr 11 12:09:46 2015
 ************************************************************************/

#include <iostream>
#include <stdlib.h>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <sstream>
#include <complex>
#include <ctime>
#include <cassert>
#include <functional>
#include <algorithm>
#include <fstream>
using namespace std;

typedef long long ll;
#define REP(i,s,t) for(int i=(s);i<(t);i++)
typedef pair<int, int> PII;
typedef pair<ll, ll> PLL;
const int INF = (int)1E9;
#define MAXN 600005
#define vv vector<int>
#define FILL(x,v) memset(x,v,sizeof(x))


int main () {
    int tests;
    cin >> tests;
    int uu = tests;
    while (tests --) {
        int s;
        int x [10];
        cin >> s;
        getchar ();
        for (int i = 0; i <= s; i++) {
            char tmpp;
            scanf ("%c", &tmpp);
            x [i] = (int)tmpp - '0';
        }
        int xx [10];
        xx [0] = 0;
        for (int i = 1; i <= s; i++) {
            xx [i] = xx [i - 1] + x [i - 1];
        }
        int res = 0;
        for (int i = 1; i <= s; i ++) {
            int tt = i - xx [i];
            if (tt > res)
                res = tt;
        }
        printf ("Case #%d: %d\n", uu - tests, res);
    }
    return (0);
}
