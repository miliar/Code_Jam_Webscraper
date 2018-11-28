#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
char st[111111];
using namespace std;
int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		scanf("%s", st);
		int len(strlen(st));
		static vector<char> vec;
		vec.clear();
		int ans(0);
		for(int i(0); i < len; i++) {
			if(vec.size() >= 1 && st[i] == vec.back()) {
				ans += 10;
				vec.pop_back();
			}else {
				vec.push_back(st[i]);
			}
		}
		ans += vec.size() / 2 * 5;
		printf("Case #%d: %d\n", qq, ans);
	}
}
