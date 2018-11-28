#include <stdio.h>
using namespace std;

int main(){
	int cases;
	scanf("%d",&cases);
	double c,f,x;
	for(int i=0;i<cases;i++){
		scanf("%lf %lf %lf",&c,&f,&x);
		double time_taken=0.0,cur_rate=2.0;
		while(x/cur_rate>(c/cur_rate)+(x/(cur_rate+f))){
			time_taken+=(c/cur_rate);
			cur_rate+=f;
		}
		time_taken+=(x/cur_rate);
		printf("Case #%d: %.7f\n",i+1,time_taken);
		//cout << "Case #"<<i+1<<":"<< time_taken << endl;
	}
}
		
