
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
#define file freopen("in.txt", "r", stdin)
#define s(n) scanf("%d", &n)
#define sl(n) scanf("%lld", &n)
#define sc(n) scanf("%c", &n)
#define ss(n) scanf("%s", &n)
#define mp make_pair
#define nl printf("\n")

int main()
{
    file;
    freopen("out.txt", "w", stdout);
    int t, x, y, cnt, ans;
    int a[4][4], b[4][4];
    s(t);
    lp (k, 1, t + 1) {
        cnt = 0;
        scanf("%d", &x);
        lp (i, 0, 4) {
            lp (j, 0, 4) {
                s(a[i][j]);
            }
        }
        scanf("%d", &y);
        lp (i, 0, 4) {
            lp (j, 0, 4) {
                s(b[i][j]);
            }
        }
        lp (i, 0, 4) {
            lp (j, 0, 4) {
                if (a[x - 1][i] == b[y - 1][j]) {
                    cnt++;
                    ans = a[x - 1][i];
                }
            }
        }
        if (cnt == 1) {
            printf("Case #%d: %d\n", k, ans);
        } else if (cnt > 1) {
            printf("Case #%d: Bad magician!\n", k);
        } else {
            printf("Case #%d: Volunteer cheated!\n", k);
        }
    }

    return 0;
}
