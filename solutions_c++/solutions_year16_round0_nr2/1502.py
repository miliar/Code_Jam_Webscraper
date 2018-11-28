#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

const int maxn = 220;

int t,n,ans;
char ch[maxn];

int main()
{
	#ifdef YZY
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	
	cin >> t;
	for (int i = 1; i <= t; i++) {
		scanf("%s",ch); n = strlen(ch);
		ans = 1;
		for (int j = 1; j < n; j++)
			if (ch[j] != ch[j-1])
				++ans;
		if (ch[n-1] == '+') --ans;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}

