#include <cstdio>
#include <string>
#include <map>
#include <iostream>
using namespace std;
map<string,int> M;
int T,cas,n,nid,ch,f[111],a[111][1111],w[111],tag,v[2][100000],x,i,j,ans;
string s;

void proc(int k)
{
	if (k > n)
	{
		++tag;
		for (i=1; i<=n; ++i)
		for (j=1; j<=w[i]; ++j) v[f[i]][a[i][j]] = tag;
		x = 0;
		for (i=1; i<=nid; ++i)
		if (v[0][i]==tag && v[1][i]==tag) ++x;
		if (x < ans) ans = x;
		return;
	}
	f[k] = 0;
	proc(k+1);
	f[k] = 1;
	proc(k+1);
}

int main()
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	scanf("%d", &T);
	for (cas=1; cas<=T; ++cas)
	{
		M.clear();
		scanf("%d", &n);
		nid = 0;
		for (i=1; i<=n; ++i)
		{
			w[i] = 0;
			while (1)
			{
				
				cin >> s;
		//		printf("i=%d get ", i); cout << s << endl;
				if (M.find(s) != M.end()) x = M[s]; else M[s] = x = ++nid;
				a[i][++w[i]] = x;
				ch=getchar();
				if (ch=='\n' || ch=='\r' || ch==-1) break;
			}
		}
		f[1] = 0;
		f[2] = 1;
		ans = 11111111;
		proc(3);
		printf("Case #%d: %d\n", cas, ans);
	}
	return 0;
}
