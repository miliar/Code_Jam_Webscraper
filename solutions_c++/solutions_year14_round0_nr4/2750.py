#include <stdio.h>
#include <algorithm>
using std::sort;
#define MAXN 1000
double x[MAXN], y[MAXN];

int main(){
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;++i)
			scanf("%lf",&x[i]);
		for(int i=0;i<n;++i)
			scanf("%lf",&y[i]);
		sort(x,x+n);
		sort(y,y+n);
		int p2 = 0, cnt2 = 0;
		for(int i=0;p2<n;++i){
			while( p2 < n && x[i] > y[p2] ) 
				++p2, ++cnt2;
			++p2;
		}
		int cnt1 = 0;
		int p1 = 0;
		for(int i=0;p1<n;++i){
			while( p1 < n && x[p1] < y[i] ) ++p1;
			if( p1 < n ) ++cnt1, ++p1;
		}
		/*for(int i=0;i<n;++i)
			printf("%.4f ", x[i]);
		printf("\n");
		for(int i=0;i<n;++i)
			printf("%.4f ", y[i]);
		printf("\n");
		*/
		printf("Case #%d: %d %d\n", t, cnt1, cnt2);
	}
	return 0;	
}
