#include <iostream>
#include <cstdio>
#include <climits>

using namespace std;

int main()
{
	int t,test = 1;
	double c,f,x,op,tt,t1,t2,cook,tot;
	scanf("%d",&t);
	while ( t-- ) {
		scanf("%lf%lf%lf",&c,&f,&x);
		op = INT_MAX;		
		tt = tot = 0;
		cook = 2;
		while ( 1 ) {
			t1 = c / cook;
			t2 = x / cook;
			if ( tot + t2 <= op ) {
				op = tot + t2;
			}
			else {

				break;
			}
			tot += t1;
			cook += f;
		}
		printf("Case #%d: %.7lf\n",test,op);
		test += 1;
	}
}
