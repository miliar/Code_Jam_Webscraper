#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <string>
using namespace std;
const int Maxn=105;
int T,n;
char s[Maxn];

bool check() {
	for (int i=1;i<=n;i++)
		if (s[i]=='-') return false;
	return true;
}

int main() {
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	scanf("%d",&T);
	for (int _t=1;_t<=T;_t++) {
		scanf(" %s",s+1);
		n=strlen(s+1);
		int ans=0;
		while (!check()) {
			int l=1;
			while (s[l]!='-') l++;
			ans+=l==1?1:2;
			while (l<=n&&s[l]=='-') s[l++]='+';
		}
		printf("Case #%d: %d\n",_t,ans);
	}
	return 0;
}
