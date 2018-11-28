#include<iostream>
#include<iomanip>
using namespace std;



int main() {
	int T;
	int k;
	cin>>T;
	double C,F,X;
	for(k=1;k<=T; k++) {
		cin>>C>>F>>X;
		double rate = 2.0;
		double time;
		double get_one;
		double new_rate;
		double get_time;
		freopen("out.txt","a",stdout);
		get_one = C/rate;
		new_rate = rate + F;
		get_time = X/new_rate;

		
		//try get first farm
		if(X/rate <= get_one + get_time) {
			//cout<<"Case #"<<k<<": "<<setprecision(7)<<X/rate<<endl;
			cout<<setiosflags(ios::fixed)<<setprecision(7)<<"Case #"<<k<<": "<<X/rate<<endl;
		} else {
			time = get_one + get_time;
			while(true) {
				get_one = get_one + C/new_rate;
				new_rate += F;
				get_time = X/new_rate;
				if(time <= get_one+get_time) {
					break;
				} else {
					time = get_one+get_time;
				}
				
			}
			cout<<setiosflags(ios::fixed)<<setprecision(7)<<"Case #"<<k<<": "<<time<<endl;
			//cout<<"Case #"<<k<<": "<<setprecision(7)<<time<<endl;
			//cout<<"Case #"<<k<<": "<<time<<endl;
		}
	}
    return 0;
}