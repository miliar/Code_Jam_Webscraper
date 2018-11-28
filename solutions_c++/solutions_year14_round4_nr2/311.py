#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tag_and_trait.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <algorithm>
#include <cstdio>
#include <functional>
#include <iostream>
#include <map>
#include <utility>

template<typename key, typename value> class ext_map: public __gnu_pbds::tree<
		key, value, std::less<key>, __gnu_pbds ::rb_tree_tag,
		__gnu_pbds ::tree_order_statistics_node_update> {
};
using namespace std;

int main() {
	freopen("src/out.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		printf("Case #%d: ", t);
		int n, ans = 0;
		scanf("%d", &n);
		map<int, int> p;
		ext_map<int, int> st;
		for (int i = 0; i < n; i++) {
			int a;
			scanf("%d", &a);
			p[a] = i;
			st[i];
		}
		for (pair<int, int> x : p) {
			st.erase(x.second);
			n--;
			ans += min(st.order_of_key(x.second),
					n - st.order_of_key(x.second));
		}
		printf("%d\n", ans);
	}
}
