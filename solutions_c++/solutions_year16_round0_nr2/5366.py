#include "cstdio"
#include "iostream"
#include "string"

using namespace std;

int main(void) {
	int t;
	scanf("%d", &t);
	for(int test = 1;test<=t;test++) {
		string s;
		cin >> s;

		s = "*" + s;
		int len = s.length();

		int ans = 0;
		for(int i=1;i<len;i++)
			ans += (s[i] != s[i-1]);

		printf("Case #%d: %d\n", test, ans - (s[len-1] == '+'));		
	}

	return 0;
}
