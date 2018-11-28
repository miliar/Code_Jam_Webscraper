#include <cstdio>
#include <algorithm>

using namespace std;
int main()
{
	int TC,c;
	double res,C,F,X,rate,cur;
	scanf("%d", &TC);
	c = 1;
	while(TC--){
		rate = 2;
		res = cur = 0;
		scanf("%lf %lf %lf", &C, &F, &X);
		while(true){
			if (cur >= C){
				if ((X-cur)/rate < (X-(cur-C))/(rate+F)){
					res += (X-cur)/rate;
					break;
				}
				else if ((X-cur)/rate >= (X-(cur-C))/(rate+F)){
					cur -= C;
					rate+=F;
				}
			}
			else if ((X - cur) / rate <= (C-cur)/rate){
				res += (X - cur) / rate;
				break;
			}
			else {
				res+= (C-cur)/rate;
				cur = C;
			}
		}
		printf("Case #%d: %.7lf\n",c++, res);
	}
	return 0;
}