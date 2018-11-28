#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	long double c,f,x,k,t1,t2,tt;
	int t; int caso = 1;
	scanf("%d",&t);
	while(t--){
		scanf("%Lf %Lf %Lf",&c,&f,&x);
		k = 0; tt = 0;
		while(true){
			t1 = c/(2 + k*f);
			double tr = x/(2 + (k + 1)*f);
			t2 = x/(2 + k*f);
			if((t1 + tr) > t2){
				tt += t2;
				break;
			}
			tt += t1;
			k += 1.0;
		}
		printf("Case #%d: %.6Lf\n",caso++,tt);
	}
	return 0;
}
