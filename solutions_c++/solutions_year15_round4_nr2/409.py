#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cassert>
#include <cctype>

#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <unordered_map>

using namespace std;

typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned uint;
typedef long double ld;

template <class T> inline T sqr(const T& a) { return a * a; }
template <class T> inline void updMin(T& a, const T& b) { if (b < a) a = b; }
template <class T> inline void updMax(T& a, const T& b) { if (b > a) a = b; }

const ld EPS = 1e-8;


void solution()
{
    int n;
    cin >> n;
    ld V, X;
    vector <ld> R(n);
    vector <ld> C(n);

    cin >> V >> X;
    for (int i = 0; i < n; ++i)
    {
        cin >> R[i] >> C[i];
    }

    if (n > 2)
        return;

    if (n == 1)
    {
        if (abs(C[0] - X) > EPS)
        {
            cout << "IMPOSSIBLE";
            return;
        }

        cout << V / R[0];
        return;
    }

    if (n == 2)
    {
        ld C1 = C[0];
        ld R1 = R[0];
        ld C2 = C[1];
        ld R2 = R[1];

        if (C1 > C2)
        {
            swap(C1, C2);
            swap(R1, R2);
        }

        if (C2 + EPS < X || C1 - EPS > X)
        {
            cout << "IMPOSSIBLE";
            return;
        }

        if (abs(C1 - X) < EPS && abs(C2 - X) < EPS)
        {
            cout << V / (R1 + R2);
            return;
        }

        if (abs(C1 - X) < EPS)
        {
            cout << V / R1;
            return;
        }

        if (abs(C2 - X) < EPS)
        {
            cout << V / R2;
            return;
        }



        ld t1 = V / (R1 + R1 * (X - C1) / (C2 - X));
        ld t2 = t1 * R1 * (X - C1) / (R2 * (C2 - X));

        ld T = max(t1, t2);
        cout << T;
        return;

    }

}



int main()
{
    //freopen("input.txt", "r", stdin); freopen("output.txt", "w", stdout);

    ios::sync_with_stdio(false);

    cout << fixed << setprecision(10);

    int nTests;
    cin >> nTests;
    for (int test = 1; test <= nTests; ++test)
    {
        cout << "Case #" << test << ": ";
        solution();
        cout << "\n";
    }



    return 0;
}
