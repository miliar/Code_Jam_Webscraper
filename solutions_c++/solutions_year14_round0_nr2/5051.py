#include <iostream>
#include <stdio.h>
#include <iomanip>
using namespace std;
int main(){

	int t;
	double c,f,x,r,tim;
	cin>>t;
	while(t--){
		cin>>c>>f>>x;
		r=2;
		tim=0;
		while(1){
			if((x/r)<((c/r)+(x/(r+f))))
			{
				tim+=x/r;
				break;
			}
			else
			{
				tim+=c/r;
				r+=f;
			}
		}

		cout<<std::setprecision(13)<<tim<<endl;

	}
	return 0;
}