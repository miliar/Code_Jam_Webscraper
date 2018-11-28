#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <climits>
#include <vector>
#include <cstdlib>
#include <cctype>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <utility>
#include <sys/time.h>

using namespace std;

#define ll long long
#define ull unsigned long long
#define ve(x) vector<x>
#define pb(x) push_back(x)
#define lp(i, a, b) for (int i = (a); i < (b); i++)
#define lpl(i, a, b) for (ll int i = (a); i < (b); i++)
#define lpd(i, a, b) for (int i = (a); i >= (b); i--)
#define lpe(it, v) for (it = ((v).begin()); it != ((v).end()); it++)
#define max(a, b) (((a) >= (b)) ? (a) : (b))
#define fin freopen("in.txt", "r", stdin)
#define fout freopen("out.txt", "w", stdout)
#define s(n) scanf("%d", &n)
#define sl(n) scanf("%lld", &n)
#define sc(n) scanf("%c", &n)
#define ss(n) scanf("%s", &n)
#define sf(n) scanf("%f", &n);
#define slf(n) scanf("%lf", &n);
#define mp make_pair
#define nl printf("\n")


int main()
{
    fin;
    fout;
    ll int t, x, y, i, f, s;
    double sum;
    sl(t);
    lpl (k, 1, t + 1) {
        scanf("%lld/%lld", &x, &y);
        i = 0;
        f = 0;
        //cout << x << " " << y << endl;
        while (y % 2 == 0 && y > x) {
            y >>= 1;
            i++;
        }
        lpl (p, 0, 60) {
            if ((ll int)pow(2, p) == y) {
                f = 1;
                break;
            }
        }
        if (x >= y && f == 1) printf("Case #%lld: %lld\n", k, i);
        else printf("Case #%lld: impossible\n", k);
    }
    return 0;
}
