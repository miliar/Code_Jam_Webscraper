#include <bits/stdc++.h>
using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A_out.txt", "w", stdout);
	
	int T;
	scanf("%d", &T);
	
	for (int t = 1; t <= T; t++)
	{
		int n;
		scanf(" %d ", &n);
		
		string s;
		cin >> s;
		
		int ans = 0;
		int cnt = s[0] - '0';
		
		for (int i = 1; i < s.size(); i++) {
			if (s[i] > '0' and cnt < i) {
				ans += i-cnt;
				cnt += i-cnt;
			}
			cnt += s[i] - '0';
		}
		
		printf("Case #%d: %d\n", t, ans);
	}
	
	fclose(stdin);
	fclose(stdout);
	
	return 0;
}
