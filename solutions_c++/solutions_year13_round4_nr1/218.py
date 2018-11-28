#include "stdio.h"
#include "stdlib.h"
#include "string.h"
#include <vector>
#include <string>
#include <iostream>
#include <cmath>
#include <cctype>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <set>
#include <queue>

using namespace std;

typedef double real;
typedef long long TT;

#define PB push_back
#define SQR(x) ((x)*(x))
#define PII pair<int, int>
#define VI vector<int>
#define VVI vector<VI >
#define VS vector<string>
#define VTT vector<TT>
#define VR vector<real>
#define A first
#define B second

const TT mod = 1000002013;

struct event
{
    int station;
    int type;
    int num;
};

struct mass
{
    int station;
    int num;
};

vector<event> ev;
vector<mass> a;
TT should, will;

TT calc(TT p, TT k, TT n)
{
    return (TT(p) * ((TT(k)*TT(n) - (TT(k)*TT(k-1))/2) % mod)) % mod;
}

int main()
{
    int T;
    cin >> T;
    for (int sc = 0; sc < T; sc++) {
        ev.clear();
        a.clear();
        should = 0;
        will = 0;

        int i, j, k, n, m;
        cin >> n >> m;
        for (i = 0; i < m; i++) {
            int L, R, p;
            cin >> L >> R >> p;

            event t;
            t.station = L; t.type = 1; t.num = p;
            ev.push_back(t);
            t.station = R; t.type = -1; t.num = p;
            ev.push_back(t);

            k = R - L;
            should = (should + calc(p, k, n)) % mod;
        }

        for (i = 0; i < ev.size(); i++)
            for (j = i+1; j < ev.size(); j++) {
                if (!(ev[i].station < ev[j].station ||
                      ev[i].station == ev[j].station && ev[i].type > ev[j].type)) {
                    event tmp = ev[i];
                    ev[i] = ev[j];
                    ev[j] = tmp;
                }
            }

        for (i = 0; i < ev.size(); i++) {
            if (ev[i].type == 1) {
                mass tmp;
                tmp.num = ev[i].num;
                tmp.station = ev[i].station;
                a.push_back(tmp);
            } else {
                int want = ev[i].num;
                while (want) {
                    int best_j = -1, best_station = 0;
                    for (j = 0; j < a.size(); j++) {
                        if (a[j].num && a[j].station > best_station) {
                            best_station = a[j].station;
                            best_j = j;
                        }
                    }
                    int delta = min(a[best_j].num, want);
                    a[best_j].num -= delta;
                    want -= delta;
                    will = (will + calc(delta, ev[i].station - best_station, n)) % mod;
                }
            }
        }

        TT ans = should % mod - will % mod;
        while (ans < 0) ans += mod;
        ans %= mod;

        cout << "Case #" << sc+1 << ": ";
        cout << ans;
        cout << endl;
    }

     return 0;
}
