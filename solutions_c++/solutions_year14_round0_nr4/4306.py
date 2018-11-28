#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>

using namespace std;

#define FOR(i, a, b) for (int i = int(a); i < int(b); i++)
#define REP(i, a) for (int i = 0; i < int(a); i++)
#define INF 1000000000
#define debugueo false
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef vector<bool> vb;

deque<double> hombre, mujer, hombre2, mujer2;
int T, t, N;

void solve()
{
    cin >> N;
    hombre.assign(N, 0.0);
    mujer.assign(N, 0.0);

    REP(i, N)
        cin >> mujer[i];
    REP(i, N)
        cin >> hombre[i];

    sort(mujer.begin(), mujer.end(), greater<double>());
    sort(hombre.begin(), hombre.end(), greater<double>());

    hombre2.assign(hombre.begin(), hombre.end());
    mujer2.assign(mujer.begin(), mujer.end());

    if(debugueo)
    {
        REP(i, N)
        {
            cout << mujer[i] << " ";
        }
        cout<<endl;

        REP(i, N)
        {
            cout << hombre[i] << " ";
        }
        cout<<endl;
    }

    int buenas=0, malas=0;
    REP(i, N)
    {
        if(mujer[0] > hombre[0])
        {
            mujer.pop_front();
            hombre.pop_front();
            buenas++;
        }
        else
        {
            mujer.pop_back();
            hombre.pop_front();
        }

    }

    REP(i, N)
    {
        if(mujer2[0] < hombre2[0])
        {
            mujer2.pop_front();
            hombre2.pop_front();
        }
        else
        {
            hombre2.pop_back();
            mujer2.pop_front();
            malas++;
        }
    }

    printf("Case #%d: %d %d\n", t, buenas, malas);
}

int main()
{
    freopen("DeceitfulWar.out", "w", stdout);
    freopen("DeceitfulWar.in", "r", stdin);
    cin >> T;
    for(t = 1; t <= T; t++)
        solve();
    return 0;
}
