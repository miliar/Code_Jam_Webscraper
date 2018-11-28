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
#define mp make_pair
#define nl printf("\n")

int main()
{
    fin;
    fout;
    int t;
    double c, f, x, r, sum, time;
    s(t);

    lp (k , 1, t + 1) {
        r = 2.0;
        sum = 0;
        time = 0;
        scanf("%lf %lf %lf", &c, &f, &x);
        while (x / r > (c / r) + (x / (r + f))) {
            time += (c / r);
            r += f;
            //cout << time << " ";
        }
        //nl;
        time += (x / r);
        printf("Case #%d: %.7lf\n", k, time);
    }

    return 0;
}
