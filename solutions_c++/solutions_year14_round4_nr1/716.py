#define OSW2
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <utility>
using namespace std;


typedef long long ll;

ll gcd(ll a, ll b) {
    if (0==a) return b;
    return gcd(b%a, a);
}

int main() {
    #ifdef OSW
    freopen("C:\\Users\\Administrator\\Desktop\\in.txt", "r", stdin);
    #endif // OSW
    #ifdef OSW2
    string file_name = "A-large";
    string file_in = file_name+".in";
    string file_out = file_name+".out";
    freopen(file_in.c_str(), "r", stdin);
    freopen(file_out.c_str(), "w", stdout);
    #endif // OSW
    ios::sync_with_stdio(false);

    int T;
    cin >> T;
    int t=0;
    while (T-(t++)) {
        cout << "Case #" << t << ": ";
        int x,n;
        cin >> n >> x;
        vector<int> v;
        for (int i=0; i!=n; ++i) {
            v.push_back(0);
            cin >> v[i];
        }
        sort(v.begin(), v.end());
        int cnt = 0;
        while (!v.empty()) {
            int a = v.front();

            int b = x-a;
            ++cnt;
            if (v.empty()) continue;
            for (auto it = v.end()-1; it!=v.begin(); --it) {
                if (*it<=b) {
                    v.erase(it);
                    break;
                }
            }
            v.erase(v.begin());
        }
        cout << cnt << endl;
    }
}


