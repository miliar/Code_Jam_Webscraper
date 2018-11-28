#include <iostream>
using namespace std;
int main() {
	int T;
	long double C,F,X,farm,cookie=0,rate=2,ttaken=0;
	cin>>T;
	for(int i=1;i<=T;i++){
		rate=2;
		ttaken=0;
		cin>>C>>F>>X;
		while(1){
			
			cookie = X/rate;
			farm = C/rate + X/(rate + F);
			if(cookie < farm){
				ttaken += cookie;
				break;
			}
			else{
				ttaken += C/rate;
				rate += F;
			}
		}
		cout.precision(10);
		cout<<"Case #"<<i<<": "<<ttaken<<"\n";
	}
	return 0;
}