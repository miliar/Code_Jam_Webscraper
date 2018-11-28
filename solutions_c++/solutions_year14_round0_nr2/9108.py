#include<cstdio>

using namespace std;

#define INF 100000.0L

main(){
	int N,caso = 1;
	long double C,F,X;
	scanf("%d",&N);
	while(N--){
		scanf("%llf%llf%llf",&C,&F,&X);

		long double M1 = X/(2.0L); 
		long double M2 = 0.0L;
		long double MIN = M1;
		int i = 0;
		while(true){
			i++;
			M1 = X/(2.0L + (((long double)i) * F)); 
			M2 += C/(2.0L + (((long double)(i-1)) * F));
			if(MIN > M1+M2){
				MIN = M1+M2;
			}else{
				break;
			}
		}
		printf("Case #%d: %.7llf\n",caso++,MIN);
	}
}
