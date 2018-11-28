#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)

typedef long long ll;

int main()
{
    ll p[39] = {
        1, 4, 9, 121, 484,
        10201, 12321, 14641, 40804, 44944,
        1002001, 1234321, 4008004, 100020001, 102030201,
        104060401, 121242121, 123454321, 125686521, 400080004,
        404090404, 10000200001, 10221412201, 12102420121, 12345654321,
        40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201,
        1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121,
        1232346432321, 1234567654321, 4000008000004, 4004009004004
    };
    
    int t;
    cin >> t;
    
    rep(caseno, t) {
        ll a, b;
        cin >> a >> b;
        cout << "Case #" << caseno + 1 << ": ";
        cout << upper_bound(p, p + 39, b) - lower_bound(p, p + 39, a) << endl;
    }
}
