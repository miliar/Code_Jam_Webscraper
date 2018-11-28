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
const int maxn = 1000 + 10;

double a[maxn + 1], b[maxn + 1];



int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        cin >> N;

        for (int i = 0; i < N; i++) { 
            cin >> a[i];
        }
        for (int i = 0; i < N; i++) { 
            cin >> b[i];
        }
        sort(a, a + N);
        sort(b, b + N);
        
        // for (int i = 0; i < N; i++) 
            // cout << a[i] << " ";
        // cout << endl;
        // for (int i = 0; i < N; i++) 
            // cout << b[i] << " ";
        // cout << endl;
        int ans = 0;
        while (ans < N) {
            bool flag = true;
            for (int i = ans; i < N; i++)
                if (a[i] < b[i - ans]) {
                    flag = false;
                    break;
                }
            if (flag)
                break;
            ans++;
        }
        cout << "Case #" << t << ": ";
        cout << N - ans << " ";
        ans = 0;
        int counter = 0;
        int i;
        for (i = 0; i < N; i++) {
            while (counter < N && a[i] > b[counter])
                counter++;
            if (counter == N)
                break;
            counter++;
        }
        cout << N - i << endl;
    }


    return 0;
}
