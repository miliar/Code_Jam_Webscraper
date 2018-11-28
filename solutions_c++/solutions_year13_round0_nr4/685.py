#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <string>
#include <cmath>
#include <cstring>
#include <vector>

using namespace std;

typedef long long ll;
typedef double db;

#define forab(i, a, b) for(int i = int(a); i < int(b); ++i)
#define forba(i, b, a) for(int i = int(b) - 1; i >= int(a); --i)
#define forn(i, n) forab(i, 0, n)

const int MAXK = 200;

int sz0, n;
int k0[MAXK + 10];

struct chest {
  int type;
  int sz;
  int k[MAXK + 10];
};

chest c[MAXK + 10];

struct ans {
    vector<int> x;

    ans() {x.clear();}

    ans operator +(const int & a) const {
        ans tmp = (*this);
        tmp.x.push_back(a);
        return tmp;
    }

    bool operator <(const ans & a) const {
        forn(i, x.size())
            if (x[i] != a.x[i]) return x[i] < a.x[i];
        return 0;
    }
};

int k[MAXK + 10];

bool dp[2000010];
ans a[2000010];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d", &T);
    forn(t, T) {
        cerr << "Test: " << t << '\n';
        printf("Case #%d: ", t + 1);

        cin >> sz0 >> n;
        memset(k0, 0, sizeof(k0));
        forn(i, sz0) {
            int tmp;
            cin >> tmp;
            k0[tmp]++;
        }
        forn(i, n) {
            cin >> c[i].type >> c[i].sz;
            forn(j, c[i].sz)
                cin >> c[i].k[j];
        }

        forn(z, (1 << n))
            dp[z] = 0;
        dp[0] = 1;
        a[0].x.clear();

        int u;
        forn(z, (1 << n))
            if (dp[z]) {
                forn(i, MAXK + 10)
                    k[i] = k0[i];
                forn(i, n)
                    if ((z & (1 << i)) != 0) {
                        k[c[i].type]--;
                        forn(j, c[i].sz)
                            k[c[i].k[j]]++;
                    }

                forn(i, n)
                    if ((z & (1 << i)) == 0 && k[c[i].type] > 0) {
                        u = (z | (1 << i));
                        if (!dp[u] || a[z] + i < a[u]) {
                            a[u] = a[z] + i;
                            dp[u] = 1;
                        }
                    }
            }

        if (dp[(1 << n) - 1]) {
            forn(i, n)
                cout << a[(1 << n) - 1].x[i] + 1 << ' ';
                cout << '\n';
        } else
            cout << "IMPOSSIBLE\n";

    }
    return 0;
}
