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
    string file_name = "B-large";
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
        int n;
        cin >> n;
        vector<int> v;
        for (int i=0; i!=n; ++i) {
            v.push_back(0);
            cin >> v[i];
        }
        if (1==n) {cout << 0 << endl; continue;}
        vector<int> v2 = v;
        sort(v.begin(), v.end());
        int sum = 0;
        for(auto x:v) {
            auto it = find(v2.begin(), v2.end(), x);
            int a = it-v2.begin();
            int b = v2.end()-it-1;
            sum += min(a,b);
            v2.erase(it);
        }
        cout << sum << endl;
    }
}


