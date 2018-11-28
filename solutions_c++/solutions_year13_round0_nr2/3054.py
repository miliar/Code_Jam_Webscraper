#include <fstream>
#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;
int T,n,m;
int a[101][101];
bool b[101];
bool pd(){
	int c,ll;
	for (int i = 100;i > 0;i--){
		if (!b[i]) continue;

		for (int j = 0;j < n;j++){
			for (int k = 0;k < m;k++){
				if (a[j][k] != i) continue;
				c = ll = 0;
				for (int l = 0;l < m;l++)
					if (a[j][l] <= i)
						c++;
				for (int l = 0;l < n;l++)
					if (a[l][k] <= i)
						ll++;
				if (ll < n && c < m) return false;
			}
		}
	}
	return true;
}
int cas;
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&T);
	while (T--){
		cas++;
		scanf("%d%d",&n,&m);
		memset(b,0,sizeof b);
		for (int i = 0;i < n;i++)
			for (int j = 0 ;j < m;j++){
				scanf("%d",&a[i][j]);
				b[a[i][j]] = 1;
			}
		if (pd())
			printf("Case #%d: YES\n",cas);
		else printf("Case #%d: NO\n",cas);
		
	}
}