#include <iostream>
#include <cstring>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>

using namespace std;

int main() {
	int t; cin >> t;

	for (int e=1; e<=t; ++e) {
		cout << "Case #" << e << ": ";
        multiset<int> s;
        int n, x; cin >> n >> x;
        for (int i=0; i<n; ++i) {
            int a; cin >> a;
            s.insert(a);
        }

        int ans = 0;

        for (;s.size();) {
            int greater = *--s.end();
            s.erase(--s.end());

            if (s.size()) {
                const int lft = x - greater;
                auto it = s.upper_bound(lft);
                if (it != s.begin()) {
                    --it;
                    s.erase(it);
                }
            }

            ++ans;
        }

        cout << ans << endl;
	}

	return 0;
}


