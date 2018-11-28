#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cstring>
using namespace std;

char s[1006];

int main() {
	int T;
	scanf("%d", &T);
	for (int test = 1; test <= T; ++ test) {
		scanf("%s", s);
		string ans(1, s[0]);
		int len = strlen(s);
		for (int i = 1; i < len; ++i) 
			if (s[i] >= ans[0]) ans.insert(0, 1, s[i]);
			else ans.insert(i, 1, s[i]);
		printf("Case #%d: ", test);
		cout<<ans<<endl;
	}
	return 0;
}