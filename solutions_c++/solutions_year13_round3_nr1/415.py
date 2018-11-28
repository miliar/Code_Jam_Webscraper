#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<cmath>
#include<algorithm>
#include<queue>

using namespace std;
int n;
char str[1000100];
long long last_dp;
int l_end;

void main(){
#ifdef MY_TEST_VAR
   freopen("input.txt", "rt", stdin);
   freopen("output.txt", "wt", stdout);
#endif

	int T;
	scanf("%d", &T);
	for (int I = 1; I <= T; I++)
	{
		long long ans = 0;
		scanf("%s %d\n", str, &n);
		int l = strlen(str);
		last_dp = 0;
		l_end = 0;
		for (int i = 0; i < l; i++)
		{
			long long next_add = last_dp;
			if (str[i] == 'a'
				||
				str[i] == 'e'
				||
				str[i] == 'i'
				||
				str[i] == 'o'
				||
				str[i] == 'u'
				)
			{	
				l_end = 0;
			}
			else
			{
				l_end++;
				if (l_end >= n)
					next_add = i + 2 - n;
			}
			ans += next_add;
			last_dp = next_add;
		}
		printf("Case #%d: %lld\n", I, ans);
	}
}