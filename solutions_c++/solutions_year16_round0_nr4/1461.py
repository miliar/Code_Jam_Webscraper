#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

int main()
{
	#ifdef YZY
		freopen("in.txt","r",stdin);
		freopen("out.txt","w",stdout);
	#endif
	
	int T; cin >> T;
	for (int l = 1; l <= T; l++) {
		int a,b,c;
		printf("Case #%d: ",l);
		scanf("%d%d%d",&a,&b,&c);
		for (int i = 1; i <= c; i++) printf("%d ",i);
		printf("\n");
	}
	return 0;
}

