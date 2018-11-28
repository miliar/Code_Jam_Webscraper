#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main(){
	int t, icase = 0;
	scanf("%d", &t);
	while(t--){
		double c, f, x;
		scanf("%lf%lf%lf", &c, &f, &x);
		double ans = x / 2;
		double buytime = c / 2;
		for(int i  = 1; i * c < x; i++){
			double total = buytime + x / (i * f + 2);
		//	printf("%d %lf %lf\n", i, buytime, ans);
			if(total >= ans){
				break;
			}
			else{
				ans = total;
			}
			buytime += (c / ((i * f) + 2));
		}
		printf("Case #%d: %7lf\n", ++icase, ans);
	}
	return 0;
}

