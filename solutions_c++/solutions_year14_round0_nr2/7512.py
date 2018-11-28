/* https://code.google.com/codejam/contest/2974486/dashboard#s=p1 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

int main() {
	int T;
	double C, F, X, curr_rate, curr_wait_time, curr_farm_buying_time, next_rate, next_wait_time, next_farm_buying_time, tot_time;
	// C - cookies required to buy another farm, F - extra cookies per/sec, X - no. of cookies to win

	cin>>T;

	for(int i = 0; i < T; i++) {
		C=F=X= curr_rate = curr_wait_time = curr_farm_buying_time = next_rate = next_wait_time = next_farm_buying_time = tot_time = 0;
		cin>>C>>F>>X;
		//cout<<"C="<<C<<" F="<<F<<" X="<<X<<endl;

		curr_rate = 2;
		curr_wait_time = X/curr_rate;
		curr_farm_buying_time = C/curr_rate;

		do {
			next_rate = curr_rate + F;
			next_wait_time = X/next_rate;
			next_farm_buying_time = C/next_rate;

			//cout<<"curr_rate="<<curr_rate<<" curr_wait_time="<<curr_wait_time<<" curr_farm_buying_time="<<curr_farm_buying_time;
			//cout<<" next_rate="<<next_rate<<" next_wait_time="<<next_wait_time<<" next_farm_buying_time="<<next_farm_buying_time;
			//cout<<endl;

			if((curr_farm_buying_time + next_wait_time) < curr_wait_time) {
				tot_time += curr_farm_buying_time; 
				//cout<<"(a) Adding "<<curr_farm_buying_time<<" to tot_time to make it => "<<tot_time<<endl<<endl;
			} else {
				tot_time += curr_wait_time;
				//cout<<"(b) Adding "<<curr_wait_time<<" to tot_time to make it => "<<tot_time<<endl<<endl;
				break;
			}

			curr_rate = next_rate;
			curr_wait_time = next_wait_time;
			curr_farm_buying_time = next_farm_buying_time;
		} while(1);

		// Have to consider the case where we start earning cookies right from the starting

		cout<<fixed<<setprecision(7);
		cout<<"Case #"<<i+1<<": "<<tot_time<<endl;
	}
} //end of main()
