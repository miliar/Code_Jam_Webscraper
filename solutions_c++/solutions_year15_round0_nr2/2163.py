#include <algorithm>
#include <bitset>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>
using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t = 1; t <= T; t++) {
        int N;
        cin >> N;
        vector<int> v(N);
        for(int i = 0; i < N; i++) {
            cin >> v[i];
        }
        int ans = *max_element(v.begin(), v.end());
        for(int i = 1; i < 1000; i++) {
            int f = 0;
            for(int j = 0; j < N; j++) {
                if(v[j] <= i) continue;
                f += ((v[j] + i - 1) / i) - 1;
            }
            ans = min(ans, i + f);
        }

        cout << "Case #" << t << ": " << ans << "\n";
    }
}
