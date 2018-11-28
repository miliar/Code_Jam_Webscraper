#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <stack>
#include <cstring>

using namespace std;

int main(void) {
	int n;
	scanf("%d", &n);
	FILE * fp = fopen("output.txt", "w");

	for (int j = 1; j <= n; j++) {
		char str[101];
		scanf("%s", str);
		stack<pair<char, int>> st;

		for (int i = strlen(str)-1; i >=0 ; i--) {
			char c = *(str + i);
			
			if (st.empty() || st.top().first != c) {
				st.push(make_pair(c, 1));
			}
			else if (st.top().first == c){
				st.top().second++;
			}
		}

		int result = 0;
		while (!st.empty()) {
			int x = st.top().second;
			char c = st.top().first;
			st.pop();
			

			if (st.empty()) {
				if (c == '-')
					result++;
				break;
			}
			st.top().second += x;
			result++;
		}

		fprintf(fp, "Case #%d: %d\n", j, result);
	}
}