#include <iostream>
#include<cstdio>
using namespace std;

int main() {
	int t1,i,a,l=1;
	double c,f,x,b,t,q,z;
	cin>>t1;
	
	while(t1--) {
		q = 2;
		t = 0;
		z = 0;
		a = 1;
		cin>>c>>f>>x;
		double t1 = x/2;
		for(i=1;;i++) {
			t = t + c/q;
		//	printf("%lf ",c/q);
			z = z+c;
			q = q+f;
			if(t1>(t+x/q)) {
				t1 = t+x/q;
			}
			else
			break;
		}
		printf("Case #%d: %0.7lf\n",l,t1);
		l++;
		}
	return 0;
}