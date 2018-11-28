#include <cstdio>
#include <stack>
using namespace std;


int main()
{
	int testcases;

	scanf("%d", &testcases);

	for(int casenum = 1; casenum <= testcases; ++casenum) {

		char s[20004];
		int ans = 0;
		stack<char> st;

		scanf("%s", s);

		for(int it = 0; s[it] != 0; ++it) {
			if(st.empty() || st.top() != s[it]) {
				st.push(s[it]);
				continue;
			}
			st.pop();
			ans += 2;
		}
		ans += st.size() / 2;

		printf("Case #%d: %d\n", casenum, ans * 5);
	}

	return 0;
}
