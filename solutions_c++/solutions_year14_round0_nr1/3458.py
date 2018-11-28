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


// int ar[2][4][4];
int row[2][17];
int main()
{
    ios_base::sync_with_stdio(false);
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        int a[2];
        for (int i = 0; i < 2; i++) {
            cin >> a[i];
            for (int j = 0; j < 4; j++)
                for (int k = 0; k < 4; k++) {
                    int tmp;
                    cin >> tmp;
                    row[i][tmp] = j + 1;
                }
        }
        vector<int> ans;
        for (int i = 1; i <= 16; i++) {
            if (row[0][i] == a[0]  && row[1][i] == a[1])
                ans.pb(i);
        }
        cout << "Case #" << t + 1 << ": ";
        if (ans.empty())
            cout << "Volunteer cheated!";
        else if (ans.size() > 1)
            cout << "Bad magician!";
        else
            cout << ans[0];
        cout << endl;
        
    }


    return 0;
}
