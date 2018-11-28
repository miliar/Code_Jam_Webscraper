#include<bits/stdc++.h>
using namespace std;

typedef long long ll;
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define INF 0x3f3f3f3f
#define MAX 105

int t;
char s[MAX];
map<char, char> inv;

void reverse(int j)
{
	int i = 0;
	while(i <= j)
	{
		char auxi = s[i];
		s[i] = inv[s[j]];
		s[j] = inv[auxi];
		++i; --j;
	}
}

int main()
{
	inv['+'] = '-';
	inv['-'] = '+';

	scanf("%d", &t);
	for(int tc=1; tc<=t; ++tc)
	{
		scanf(" %s ", s);
		
		int sol = 0;
		for(int j = strlen(s) - 1; j>=0; --j)
		{
			if(s[j] != '+')
			{
				if(s[0] == '+')
				{
					int k = 0;
					for(; k <= j && s[k] == '+'; ++k);
					k--;
					if(k != j) reverse(k), sol++;
				}
				reverse(j); sol++;
			}
		}
		if(s[0] == '-') sol++;

		printf("Case #%d: %d\n", tc, sol);
	}

	return 0;
}
