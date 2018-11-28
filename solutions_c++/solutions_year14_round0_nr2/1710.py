#include <bits/stdc++.h>
using namespace std;
int T;
double C,F,X,r1,r2,pt1,pt2,tx1,tx2;
int main(){
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc){
		scanf("%lf %lf %lf", &C,&F,&X);
		r1=r2=2.0;
		pt1=pt2=tx1=tx2=0.0;
		do{
			pt1=pt2;
			r1=r2;

			tx1=pt1+X/r1;

			tx2=pt2+C/r2;
			r2+=F;
			pt2=tx2;
			tx2+=X/r2;

		// printf("vals: %7lf %7lf %7lf %7lf\n", r1,r2,pt1,pt2);
		// printf("tx1 tx2 %7lf %7lf\n", tx1,tx2);
		}while(tx1>tx2);
		printf("Case #%d: %.8lf\n",tc, tx1);
	}
}