#include <stdio.h>
#include <cstring>

using namespace std;

int main(){
	freopen("B-large.in", "r", stdin);
//	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	double C, F, X, res;
	int T, k; //k is the number of farms
	scanf("%d", &T);
	for(int test=1; test<=T; test++){
		res = 0;
		scanf("%lf%lf%lf", &C, & F, &X);
		double temp = X/C -1 - 2/F;
		if(temp > 0.0) {
			k = int(temp);
			k++;
		}	
		else k = 0;
		for(int i=0; i<k; i++){
			res += C/(2+i*F);
		}
		res += X/(2+k*F);
		printf("Case #%d: %.7lf\n", test, res);
	}
	return 0;
}
