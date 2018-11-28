#include <bits/stdc++.h>

using namespace std;

typedef long double db;
db a,b,c;
int n;

int main()
{
	freopen("2.out","w",stdout);
	scanf("%d",&n);
	for(int i=1;i<=n;i++) {
		scanf("%Lf %Lf %Lf",&a,&b,&c);
		db t = 123456789.0;
		db mini = 0.0;
		db speed = 2.0;
		while( mini + (c/speed) <= t ) {
			t = mini + (c/speed);
			mini += (a/speed);
			speed += b;
		}
		printf("Case #%d: %.7Lf\n",i,t);
	}

	return 0;
}
