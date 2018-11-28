#include <iostream>
#include <cstdlib>
#include <iomanip>
#include <cstring>
#include <string>
#include <algorithm>
#include <queue>
#include <map>
#include <set>
#include <stack>
#include <vector>
#include <ctime>
#include <fstream>
#include <cmath>
#include <functional>

using namespace std;

#define mp make_pair
#define pb push_back
#define F first
#define S second

const int INF = 1000000000;
const int C = 1000000;
const int mda = 1337 +  14664;

vector<pair<long long, vector<long long> > > ans;

int lp[10001000];

vector<int> pr;

long long p(long long x, int k){
    long long y = 0;
    long long d = 1ll;
    vector<int> T;
    long long X = x;
    while (X > 0){
        T.pb(X%2);
        X /= 2;
    }
    for (int i=0; i<T.size(); i++){
        y += T[i] * d;
        d *= k;
    }
    return y;
}

long long D(long long x){
    long long d = 2ll;
    while (1ll*d*d <= x){
        if (x % d == 0)
            return d;
        d++;
    }
    return 1ll;
}

int main()
{
    ios_base::sync_with_stdio(0);
    #ifdef LOCAL
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #else
        //freopen("encryption.in", "r", stdin);
        //freopen("encryption.out", "w", stdout);
    #endif // LOCAL
    int t;
    cin >> t;
    for (int T=1; T<=t; T++){
        int k, c, s;
        cin >> k >> c >> s;
        if (s < k) {
            cout << "Case #" << T << ": IMPOSSIBLE" << endl;
            continue;
        }
        cout << "Case #" << T << ": ";
        for (int i=0; i<k; i++)
            cout << i + 1 << ' ';
//        long long u = 1ll;
//        for (int i=0; i<c-1; i++)
//            u *= 1ll*k;
//        int j = 0;
//
//        for (int i=0; i<s; i++){
//            cout << 1ll*j*u + j + 1 << ' ';
//            j++;
//        }
        cout << endl;
    }
    return 0;
}
