#define OSW2

#include <iostream>
#include <functional>
#include <algorithm>
#include <utility>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>

using namespace std;

typedef long long ll;




int main() {
#ifdef OSW
    freopen("//Users//osw//Desktop//in.txt", "r", stdin);
#endif
#ifdef OSW2
    string file_name = "B-large";
    freopen(("//Users//osw//Downloads//" + file_name + ".in").c_str(), "r", stdin);
    freopen(("//Users//osw//Downloads//" + file_name + ".out").c_str(), "w", stdout);
#endif
    
    int T, t = 0;
    cin >> T;

    while (T-(t++)) {

        int D;
        vector<int> v;
        cin >> D;
        for (int i = 0; i < D; ++i) {
            int n; cin >> n;
            v.push_back(n);
        }
        int ans = 1e9;

        for (int i=1; i<=1000; ++i) {
            int sum = i;
            for (auto x:v) {
                sum += (x-1)/i;
            }
            ans = min(ans,sum);
        }



        cout << "Case #" << t << ": ";
        cout << ans << endl;

    }
}



