#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
using namespace std;
int main()
{
	int t,c1;
	long double c,x,f,f1;
	scanf("%d",&t);
	
	for (int q = 1; q <= t; q++) {
		c1 =0 ;
		long double m1,sum = 0,sum1 = 0;
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		f1 = f;
		m1 = x/2;
		while (1) {
			if (c1 == 0) {
				sum = c/2 + x/(f+2);
				if (m1 <= sum) {
					printf("Case #%d: %.7Lf\n",q,m1);
					break;
				}
				m1 = sum;
				//cout << "sum =  " << sum << endl;
				sum1 = c/2;
				f += 2;
				c1++;
			} else {
				sum = sum1 + c/f + x/(f+f1);
				//cout << "sum = "<<sum << endl; 
				if (m1 <= sum) {
					printf("Case #%d: %.7Lf\n",q,m1);
					break;
				}
				m1 = sum;
				sum1 += c/f;
				f += f1;
			}
		}
	}
}
