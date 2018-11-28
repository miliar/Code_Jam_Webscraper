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
        N++;
        vector<int> v(N);
        string s;
        cin >> s;
        for(int i = 0; i < N; i++) {
            v[i] = s[i] - '0';
        }
        int ans = 0, total = 0;
        for(int i = 0; i < N; i++) {
            if(v[i] == 0) continue;
            int diff = i - total;
            ans += max(diff, 0);
            total += max(diff, 0);
            total += v[i];
        }
        cout << "Case #" << t << ": " << ans << "\n";
    }
}
