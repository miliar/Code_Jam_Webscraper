#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int T;
	int times=0;
	cin>>T;
	while(times++<T){
		double c,f,x;
		double p;
		cin>>c>>f>>x;
		p=((x-c)*f)/c;
		long long cnt=((p-2.0)/f +0.9999999999999);
		if(p<=0){
			printf("Case #%d: %lf\n",times,x/2.0);
		}else{
			double per=2.0;
			double sec=0;
			for(int i=0;i<cnt;i++){
				sec+=c/per;
				per+=f;
			}
			sec+=x/per;
			printf("Case #%d: %.10lf\n",times,sec);
		}
	}
	return 0;
}
