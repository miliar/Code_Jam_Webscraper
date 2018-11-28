#include <cstdio>
#include <string>

using namespace std;

const char SYM[4] = "RPS";

string build(int n, int u){
	if (n == 0)
		return string(1, SYM[u]);

	string a(build(n - 1, u)), b(build(n - 1, (u + 2) % 3));
//	printf("%s %s\n", a.c_str(), b.c_str());
	return a < b ? a + b : b + a;
}

int main(){
	int cas;
	scanf("%d", &cas);
	for (int casi = 1; casi <= cas; ++casi){
		printf("Case #%d: ", casi);

		int n, R, P, S;
		scanf("%d%d%d%d", &n, &R, &P, &S);
		string ans = "";
		for (int i = 0; i < 3; ++i){
			string t = build(n, i);

			int cnt[3] = {R, P, S};
			for (int j = 0; j < t.size(); ++j){
				cnt[0] -= t[j] == 'R';
				cnt[1] -= t[j] == 'P';
				cnt[2] -= t[j] == 'S';
			}

			if (cnt[0] || cnt[1] || cnt[2])
				continue;
			if (ans.empty() || t < ans)
				ans = t;
		}
		if (ans.empty())
			puts("IMPOSSIBLE");
		else
			puts(ans.c_str());
	}
	return 0;
}
