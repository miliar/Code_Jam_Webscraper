#include <bits/stdc++.h>

using namespace std;

int t,r,c,w;
int ans;

int main(){
	scanf("%d",&t);
	for (int jj=1; jj<=t; jj++){
		scanf("%d%d%d",&r,&c,&w);
		ans = w;
		ans += (r*(c/w));
		if (c%w != 0) ans++;
		ans--;
		printf("Case #%d: %d\n",jj,ans);
	}
	return 0;
}