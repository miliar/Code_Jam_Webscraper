#include<iostream>
using namespace std;

int main(){
	int testit;
	cin>>testit;
	for(int t=0;t<testit;t++) {
		double cost,pr,target,vastaus;
		cin>>cost>>pr>>target;
		double rate = 2.0;
		vastaus = 0.0;
		if (cost>=target) {
			vastaus=target/rate;
		} else {
			while(true){
				if(target/rate<=(target/(rate+pr)+(cost/rate))) {
					vastaus += target/rate;
					break;
				} else {
					vastaus += cost/rate;
					rate += pr;
				}
			}
		}


		cout.precision(8);
		cout<<"Case #"<<t+1<<": "<<fixed<<vastaus<<endl;
	}
	return 0;
}
