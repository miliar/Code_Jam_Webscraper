#include <bits/stdc++.h>
using namespace std;

#define MAX 200
char s[MAX];

void solve(int N)
{
	scanf("%s", s);
	int r = -1;
	int i = 0;
	int l = strlen(s);
	int t1;
	for(i = 0 ; i<l; i++)
	{
		r+=1;
		t1 = 0;
		while(s[i]=='-')
		{
			t1 = 1;
			i++;
		}

		r+=t1;
		while(s[i]=='+')
		{
			i++;
		}

		i--;
	}

	printf("Case #%d: %d\n",N,  r);
}

int main()
{
	int t;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin >> t;
	int i = 1;
	while(t--)
	{
		solve(i);
		i++;
	}
}