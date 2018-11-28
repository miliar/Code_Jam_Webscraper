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
        int n; cin >> n;
        int s[1010]; for (int i=0; i<n; ++i) cin >> s[i];

        int ans = 0;

        int from = 0;
        int to = n;
        for (int i=0; i<n; ++i) {
            int pos = min_element(s + from, s + to) - s;
            if (pos - from < to - pos - 1) {
                for (int u=pos-1; u>=from; --u) {
                    swap(s[u], s[u+1]);
                    ++ans;
                }
                ++from;
            } else {
                for (int u=pos+1; u<to; ++u) {
                    swap(s[u], s[u-1]);
                    ++ans;
                }
                --to;
            }
        }

        cout << ans << endl;
	}

	return 0;
}


