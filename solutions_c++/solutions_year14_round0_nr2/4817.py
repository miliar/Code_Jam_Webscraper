#include <stdio.h>
#include <iostream>
#include <string.h>
#include <queue>
#include <vector>


#define eps 0.00000001
using namespace std;

double ans,number,C,F,X,Dist;
int T;

void work( int cas ){

		number = 0; 	Dist = 2.0;
		scanf("%lf%lf%lf",&C,&F,&X);

		ans = X/Dist;
		while ( 1 ){
			ans = min(ans,number+X/Dist);
			number += ( C / Dist );
			Dist += F;
			if (  ans - (number + X / Dist ) < eps) break;
		}
		printf("Case #%d: %0.7lf\n",cas,ans);
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);
	int i = 0;
	scanf("%d",&T);
	while ( T-- ) work(++i);
	return 0;
}
