#include <cstdio>

using namespace std;

struct solver{
	int n;
	char s[11111];
	void Input(){
		scanf("%d%s", &n, s);
		++n;
	}
	void Answer(){
		int ans = 0;
		int foo = 0;
		for(int i = 0; i < n; ++i){
			if (s[i] != '0' && i > foo){
				ans += i - foo;
				foo = i + s[i] - '0';
			}
			else foo += s[i] - '0';
		}
		printf("%d\n", ans);
	}
} data;

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	scanf("%d", &tc);
	for(int t = 1; t <= tc; ++t){
		printf("Case #%d: ", t);
		data.Input();
		data.Answer();
	}
	return 0;
}