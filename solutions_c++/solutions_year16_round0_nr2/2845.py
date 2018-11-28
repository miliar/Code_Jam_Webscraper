#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
#define rep(i,s,t) for(int i=int(s); i<int(t); i++)
#define mst(A,k) memset(A,k,sizeof(A))

char str[105];

int main() {
	freopen("B-large.in","r",stdin); 
	freopen("ans.txt","w",stdout); 

	int Cas, n;
	scanf("%d", &Cas);
	rep(cas, 0, Cas)
	{
		scanf("%s", str);
		int strLen = strlen(str);
		int ans = 0;
		rep(i, 1, strLen)
		{
			if(str[i] != str[i-1]) ans++;
		}
		if(str[strLen - 1] == '-') ans++;
		printf("Case #%d: %d\n", cas + 1, ans);
	}
	return 0;
}

