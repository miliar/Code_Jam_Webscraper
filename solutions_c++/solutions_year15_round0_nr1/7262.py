#include <bits/stdc++.h>

using namespace std;

typedef vector<int>	vi;

#define pb	push_back

int main()
{
	int t;
	int caso = 1;
	scanf("%d", &t);
	while(t--)
	{
		int smax;
		scanf("%d", &smax);
		string s;
		cin >> s;
		int ans = 0;
		for(int i=1; i<=smax; i++) {
			int sum = 0;
			for(int j=0; j<i; j++)
			{
				sum+=(s[j]-'0');
			}
			if(sum < i) {
				ans++;
				s[i]++;
			}
		}
		printf("Case #%d: %d\n", caso++, ans);
	}
	return 0;
}