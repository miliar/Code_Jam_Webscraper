#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
double getFloat(string str){
	double val=0,mult=0.1,add=0;
	bool flag=true;
	for(int i=0;i<str.size();i++){
		if(str[i]!='.'){
			if(flag){
				val=val*10+str[i]-'0';
			}else{
				add=add+(str[i]-'0')*mult;	
				mult=mult*0.1;
			}
		}else flag=false;
	}
	add*=10000000;
	val*=10000000;
	val+=add;
	return val;	
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int tst=0,T;
	cin>>T;
	while(tst<T){
		double C,F,X,mini=1000000000.0;
		string A_,B_,C_;
		cin>>A_>>B_>>C_;
		C=getFloat(A_),F=getFloat(B_),X=getFloat(C_);
		double rate=20000000.0,time=0.0;//time per cookie
		double get_rate=F;
		for(int i=0;i<100000;i++){
			double time_for_X=(X)/rate;
			if(time_for_X<0)break;
			double net_time=time+time_for_X;
			mini=min(mini,net_time);			
			double time_for_C=(C)/rate;
			time=time+time_for_C;
			rate=rate+get_rate;
		}		
		//printf("Case %d: %.7f\n",++tst,mini);
		printf("Case #%d: ",++tst);
		printf("%.7f\n",mini);
	}
	return 0;
}
