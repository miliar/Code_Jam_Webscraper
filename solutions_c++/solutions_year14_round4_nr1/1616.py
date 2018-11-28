#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>
#include <map>
#include <set>
#include <functional>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);

    int t;
    cin >> t;

    for (int CN = 1; CN <= t; CN++) {
        int N, X;

        cin >> N >> X;

        vector<int> szs;
        for (int i = 0; i < N; i++) {
            int x;
            cin >> x;
            szs.push_back(x);
        }
        sort(szs.begin(), szs.end());

        int ans = 0;

        while (szs.size()) {
            ans++;
            
            int biggest = szs.back();
            szs.pop_back();

            for (int i = szs.size() - 1; i >= 0; i--) {
                if (biggest + szs[i] <= X) {
                    szs.erase(szs.begin() + i);
                    break;
                }
            }
        }
        cout << "Case #" << CN << ": " << ans << "\n";
    }

    return 0;
}

