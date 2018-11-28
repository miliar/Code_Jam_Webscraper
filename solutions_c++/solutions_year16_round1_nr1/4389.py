#include <bits/stdc++.h>
using namespace std;
int main()
{
	freopen("inlarge", "r", stdin);
	freopen("outlarge", "w", stdout);
	int tt;
	scanf("%d", &tt);
	char foo[2000];
	deque<char> s;
	for(int qq = 1; qq<= tt; qq++)
	{
		scanf("%s", foo); 
		printf("Case #%d: ", qq);
		int n = strlen(foo);
		for(int i = 0; i< n; i++)
		{
			if(s.empty() || foo[i] >= s.front()) s.push_front(foo[i]);
			else s.push_back(foo[i]);
		}
		for(int i = 0; i< (int) s.size(); i++)
		{
			printf("%c", s[i]);
		}
		while(!s.empty()) s.pop_back();
		printf("\n");
	}
}