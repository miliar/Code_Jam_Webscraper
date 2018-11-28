#include <iostream>
#include <cstdio>

using namespace std;

const int maxn=1000+5;
char s[maxn];

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);	int T; cin >> T;
	int n;
	for (int kase=1; kase<=T; kase++)
	{
		scanf("%d", &n);
		scanf("%s", s);
		int ans=0;
		int res=0;
		for (int i=0; i<=n; i++)
		{
			int temp=s[i]-'0';
			
			if (ans>=i)
				ans+=temp;
			else 
			{
				res+=i-ans;
				ans+=temp+i-ans;
			}
			// cout << ans << endl;
		}
		printf("Case #%d: %d\n", kase, res);
	}
	fclose(stdin);
	fclose(stdout);
}