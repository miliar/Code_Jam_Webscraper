#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt;
int n,m;
string s[100];

int test(int x,int y) {
	int res=0;
	bool flag=true;
	for (int i=x+1;i<n;++i)
		if (s[i][y]!='.') {
			flag=false;
			break;
		}
	if (!flag) {
		if (s[x][y]=='v') return 0;
		res++;
	}
	flag=true;
	for (int i=x-1;i>=0;--i)
		if (s[i][y]!='.') {
			flag=false;
			break;
		}
	if (!flag) {
		if (s[x][y]=='^') return 0;
		res++;
	}
	flag=true;
	for (int i=y+1;i<m;++i)
		if (s[x][i]!='.') {
			flag=false;
			break;
		}
	if (!flag) {
		if (s[x][y]=='>') return 0;
		res++;
	}
	flag=true;
	for (int i=y-1;i>=0;--i)
		if (s[x][i]!='.') {
			flag=false;
			break;
		}
	if (!flag) {
		if (s[x][y]=='<') return 0;
		res++;
	}
	if (res==0) return -1;
	else return 1;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	cin >> tt;

	for (int ii=1;ii<=tt;++ii) {
		cin >> n >> m;
		for (int i=0;i<n;++i)
				cin >> s[i];

		bool flag=true;
		int ans=0;
		for (int i=0;i<n;++i)
			for (int j=0;j<m;++j)
				if (s[i][j]!='.') {
					int cur=test(i,j);
					if (cur==-1) {
						flag=false;
						break;
					}
					ans+=cur;
				}

		printf("Case #%d: ",ii);
		if (flag) printf("%d\n",ans);
		else printf("IMPOSSIBLE\n");
	}

}
