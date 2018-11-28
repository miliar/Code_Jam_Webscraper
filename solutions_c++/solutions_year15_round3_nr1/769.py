#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;
typedef long long ll;
const int inf=0xfffffff;

int solve(){
	int r,c,w;
	cin >> r >> c >> w;
	int ans=c/w*r+w;
	if(c%w==0) ans--;
	return ans;
}

int main(){
	//freopen("test.in","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("out.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas = 1; cas <= T; ++cas)
	{
		printf("Case #%d: %d\n",cas,solve());
	}
	return 0;
}