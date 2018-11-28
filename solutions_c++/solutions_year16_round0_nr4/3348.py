#include <map>
#include <set>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <vector>
#include <cassert>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
using namespace std;
#define int long long

int power(int a, int b)
{
    if (b == 0) return 1;
    if (b & 1) return power(a, b - 1) * a;
    return power(a * a, b / 2);
}

#undef int
int main()
{
#define int long long

    freopen("in", "r", stdin); freopen("out", "w", stdout);
    int t; cin >> t;
    for (int tt = 1; tt <= t; tt++)
    {
        cerr << "Executing Case #" << tt << "\n";
        cout << "Case #" << tt << ": ";
        int k, c, s;
        scanf("%lld%lld%lld", &k, &c, &s);
        for (int i = 0; i < k; i++){
            cout << i+1 << " ";
        }
        cout << endl;
//        if(s * c < k){
//            cout << "IMPOSSIBLE\n";
//            continue;
//        }
//        for (int i = 0; i*c < k; i++){
//            int ans = 0;
//            for (int j = 0; j < c && i*c + j < k; j++){
//                ans += (i*c+j) * pow(k,c-j-1);
//            }
//            cout << ans + 1 << " ";
//        }
//        cout << endl;
    }
    return 0;
}
