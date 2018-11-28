#include <iostream>
#include <iomanip>
using namespace std;
int main(){
	int tests;
	cin>>tests;
	double total_time;
	for (int t = 0; t < tests; t++){
		total_time=0.000000000000;
		double c, f, x;
		double curr_rate = 2.000000000000;
		cin>>c>>f>>x;

		while(true){
			double next_time = c/(curr_rate) + x/(curr_rate+f);
			double this_time = x/curr_rate;
			if(next_time > this_time){
				total_time += this_time;
				break;
			}
			else {
				total_time += c/curr_rate;
				curr_rate += f;
			}
		}

		cout<<"Case #"<<t+1<<": ";
		cout<<fixed<<setprecision(7)<<total_time<<endl;
	}
}