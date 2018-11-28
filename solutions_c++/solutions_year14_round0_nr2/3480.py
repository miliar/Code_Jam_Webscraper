// In the name of God
#include <algorithm>
#include <cassert>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <queue>
#include <utility>
#include <vector>


using namespace std;


typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<double> point;

#define siz(x) (int(x.size()))
#define err(x) cerr << #x << " = " << x << endl;
#define pb push_back
#define mp make_pair

#define X first
#define Y second
// #define X real()
// #define Y imag()

const double eps = 1e-8;



int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        double C, F, X;
        cin >> C >> F >> X;
        double curt = 0, curf = 2.0, courc = 0;
        double mint = X / 2.0 + 1;
        for (int nof = 0; nof * C <= X; nof++) {
            mint = min(mint, curt + X / curf);
            // cerr << nof << " " << mint << endl;
            double deltaT = C / curf;
            curt += deltaT;
            curf += F;
            // curc += 0; // no change
        }
        cout << "Case #" << t << ": ";
        cout.precision(7);
        cout << fixed << mint << endl;
    }


    return 0;
}
