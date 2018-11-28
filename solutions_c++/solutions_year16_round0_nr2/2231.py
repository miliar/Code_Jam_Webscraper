//By Lin
#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<set>
#include<vector>
#include<map>
#include<queue>
#include<cctype>
#include<cmath>

#define eps 1e-9
#define sqr(x) ((x)*(x))
#define Rep(i,n) for(int i = 0; i<n; i++)
#define foreach(i,n) for( __typeof(n.begin()) i = n.begin(); i!=n.end(); i++)
#define X first
#define Y second
#define mp(x,y) make_pair(x,y)

using namespace std;
typedef long long LL;
typedef pair<int,int> pii;

#define N 100010

int n;
char s[N];

int	main(){
	int cas, tt = 0;
	cin >> cas;
	while (cas --) {
		scanf("%s", s);
		int ans = 0, len = strlen(s);
		for (int i = 0; i < len - 1; i++) 
			if (s[i] != s[i + 1]) ans++;
		if (s[len - 1] != '+') ans++;
		printf("Case #%d: %d\n", ++tt, ans);
	}
	return 0;
}
