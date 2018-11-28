#include <iostream>
#include <cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;
typedef long long ll;

char ss[1005];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,ans,L;
	string res;
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		scanf("%s", ss);
		res.clear();
		L = strlen(ss);
		res += ss[0];
		for (int i = 1; i < L; ++i)
		{
			if (ss[i] >= res[0])
				res = ss[i] + res;
			else
				res += ss[i];
		}
		printf("Case #%d: %s\n", tc, res.c_str());
	}

	return 0;
}