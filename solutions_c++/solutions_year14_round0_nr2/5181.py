#include <iostream>
#include <cstdio>
#include <cmath>
#define lli long long int
using namespace std;

int main() {
	// your code goes here
	lli tcase,li,i,k1,j,count,ch1,ch2;
	double x,c,f,ans,k,v1;
	scanf("%lld", &tcase);
	
	for (li = 1; li <= tcase; ++li) {
		scanf("%lf%lf%lf", &c, &f, &x);
		
		k = ((x - c) * f - 2 * c) / (c * f);
		
		k1 = (lli)ceil(k);
		
		if (k1 < 0)
			k1 = 0;
			
		count = 0;
		ans = 0.0;
		v1 = 2.0;
		
		//cout << "c = " << c << "f = "<< f <<"x = "<< x << endl;
		while (count < k1) {
			ans = ans + c/v1;
			v1 = v1 + f;
			++count;
		}
		
		ans = ans + x / v1;
		
		printf("Case #%lld: %0.7lf\n", li, ans);
	}
	return 0;
}