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
    int t, n, end, flag, st, cnt;
    set<int>::iterator it, jt, xt;
    s(t);

    lp (k, 1, t + 1) {
        s(n);
        flag = 0;
        double a[n], b[n], a1[n], b1[n];
        lp (i, 0, n) {
            slf(a[i]);
        }
        lp (i, 0, n) {
            slf(b[i]);
        }
        sort(a, a + n);
        sort(b, b + n);
        lp (i, 0, n) {
            a1[i] = a[i];
            b1[i] = b[i];
        }
        //for deceitful war
        end = n - 1;
        st = cnt = 0;
        lpd (i, n - 1, st) {
            if (a[i] < b[end]) {
                st++;
                i++;
                b[end] = -1;
            }
            end--;
        }
        lp (i, 0, n) if (b[i] == -1) cnt++;
        printf("Case #%d: %d ", k, n - cnt);

        //for war
        st = cnt = 0;
        lp (i, 0, n) {
            lp (j, st, n) {
                if (b1[j] > a1[i]) {
                    b1[j] = -1;
                    st = j + 1;
                    //lp (p, 0, n) cout << b1[p] << " ";
                    //nl;
                    break;
                }
            }
        }
        lp (i, 0, n) if (b1[i] == -1) cnt++;
        printf("%d\n", n - cnt);

    }
    return 0;
}
