#include <iostream>
#include <cstdio>
using namespace std;
int main(){
	int T;
	//freopen("InputCookie.txt","r",stdin);
	//freopen("OutCookie.txt","w",stdout);
	cin>>T;
	for(int kasus=0;kasus<T;kasus++){
		double C,F,X;
		scanf("%lf %lf %lf",&C,&F,&X);
		double rate=2.0;
		double time=0.0;
		//printf("C : %lf , F : %lf , X : %lf\n",C,F,X);
		while(1){
			double Current=X/rate;
			double Later=C/rate+X/(rate+F);
			//cout<<Current<<" "<<Later<<endl;
			if (Current>Later){
				time+=C/rate;
				rate+=F;}
			else{
				time+=X/rate;
				break;}
		}
		printf("Case #%d: %.7lf\n",kasus+1,time);
	}
	return 0;}