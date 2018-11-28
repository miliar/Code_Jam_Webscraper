#include<iostream>
#include<algorithm>
#include<string>
#include <iomanip>

using namespace std;

int main(){
    int t;
    cin >> t;
    for(int i=0; i<t; i++){
		double c, f, x, time=0, rate=2;
		cin >> c >> f >> x;
		int farms = 0;
		while(1){
			double make = (c / rate) + (x / (rate+f));
			double wait = (x / rate);
			//cout << (c / rate) << "+" << (x / (rate+f)) << " vs " << wait << endl;
			if(make < wait){
				time += (c / rate);
				//cout << "time += " << (c / rate) << endl;
				rate += f;
				farms++;
			} else {
				time += wait;
				break;
			}
			//cout << time << ", rate=" << rate << endl;
		}
		cout << "Case #" << (i+1) << ": " << fixed << setprecision(7) << time << endl;
    }
    return 0;
}
