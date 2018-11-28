#include <cstdio>
#include <algorithm>
#include <set>

using namespace std;

multiset<int> st;

int main(){
	int T, x, n, i, tmp, b, ans;
	scanf("%d", &T);
	for (int cas = 1; cas <= T; cas++){
		scanf("%d %d" ,&n, &x);
		st.clear();
		for (i = 0; i < n; i++){
			scanf("%d", &tmp);
			st.insert(tmp);
		}
		ans = 0;
		while (!st.empty()){
			auto a = st.begin();
			st.erase(a);
			ans++;
			auto b = st.upper_bound(x-*a);
			if (b == st.begin()) break;
			st.erase(--b);
		}
		ans += st.size();
		printf("Case #%d: %d\n", cas, ans);
	}
}

