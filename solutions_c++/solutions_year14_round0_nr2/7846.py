#include <iostream>
#include <stdio.h>
#include <vector>
#include <string>
#include <iomanip>
using namespace std;

int main() {
 //	C= cookies with which new farm can be bought
 // F = extra rate which would be earned
 // X target numebr of cookies to be achieved
	int cases;
	cin>>cases;
	vector <double> dump;
	for(int casen = 0; casen < cases; ++casen) {
		double target, rate; // target and rate
		rate = 2.0;
		double a, b, c;
		double Cost, F, dum;
		double coins = 0.0;
		b=0.0;
		cin>>Cost>>F>>target;
		double time, timeupto = 0.0;
		for (time = 0.001; ; time = time + 0.001) {
			coins = coins + rate*0.001;
			if (coins >= Cost) {
				coins = coins - Cost;
				//cout<<"this is target "<<target<<" this is rate "<<rate<<endl;	
				a = target/rate;
				//cout<<setprecision(10)<<a<<endl;
				b = target/(rate+F);
				c = Cost/rate;

			if (b+c < a) {
				rate = rate + F;
				timeupto += c;
				//cout<<timeupto<<endl;
			}
			else
				break;
			}

		}

		double total_time = timeupto + a;
		dump.push_back(total_time);

	}
	

	for (int sizes = 0; sizes < dump.size(); ++sizes) {
		cout<<"Case #"<<(sizes+1)<<": "<<setprecision(11)<<dump.at(sizes)<<endl;
	}
	return 0;

}
