#include <iostream>

using namespace std;

int main()
{
	int t;
	int cnt_case = 0;
	double result =0 ;
	double c,f,x;
	double c_Ck = 0;
	double pTime = 0;
	double tmp1= 0;
	double tmp2 =0;
	double cps = 2.0;
	cin>>t;

	while(t--){		
		cnt_case++;
		pTime = 0;
		cps = 2.0;
		cin>>c>>f>>x;
		for(; ; ){
			tmp1 = pTime + x / cps;	//right now
			tmp2 = pTime + c / cps + (x/(cps+f));				//future

		/*	printf("\n%lf %lf %lf \n",c,f,x);
			printf("%lf %lf \n",tmp1, tmp2);*/
			if(tmp1 < tmp2){
				result = tmp1;
				break;
			}else{
				pTime += c/cps;
				cps += f;
			}
		}

		printf("Case #%d: %.7lf\n",cnt_case,result);
	}
	return 0;
}
