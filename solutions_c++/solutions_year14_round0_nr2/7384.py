#include <iostream>
#include <cstdio>
using namespace std;

int T;
double C,F,X;
double ans;


void solve(int tCase){
	double rate=2.0;
	double farmTime=0;
	double ans = X/rate;
	for(int i=0; ;++i){
//		cout<<"rate "<<rate<<" farmtime "<<farmTime<<" ans "<<ans<<endl;
		farmTime += (C/rate);
		rate += F;
		double tempAns= farmTime + (X/rate);
		if(tempAns >ans)
			break;
		ans = tempAns;
	}
//	cout<<"Case #"<<tCase<<": "<<ans<<endl;
	printf("Case #%d: %.07f\n",tCase,ans);
}
int main(){
    cin>>T;
//	cout<<(1.0/3.0)<<endl;
	for(int xx=1;xx<=T;++xx){
		cin>>C>>F>>X;

		solve(xx);
	}

}
