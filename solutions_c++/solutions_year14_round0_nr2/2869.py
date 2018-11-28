#include <bits/stdc++.h>
using namespace std;
int main(){
	freopen("sol.txt","w",stdout);
	int test; scanf("%d",&test); 	
	for(int num = 1; num<=test; ++num){		
		double c,f,x;		
		double kq = 1000000000;
		double cur = 0; double gain = 2.0;
		scanf("%lf%lf%lf",&c,&f,&x);
		for(int i = 0; i <= (int)x; ++i){			
			kq = min(kq, x/gain + cur);
			cur = cur + c/gain;
			gain = gain + f;			
		}
		
		printf("Case #%d: %.9f\n",num,kq);
	}
}