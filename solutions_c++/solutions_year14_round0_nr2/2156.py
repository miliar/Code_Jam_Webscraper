#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <climits>
#include <vector>
#include <iterator>
#include <set>
#include <bitset>
#include <ctime>
#include <iomanip>
#include <map>

using namespace std;

int main() {
	//ios_base::sync_with_stdio(false);
	int t;
	cin>>t;
	for(int test=1; test<=t; test++) {
		double c, f, x;
		cin>>c>>f>>x;
		int i = 0;
		double t, t_, total, best;
		t = t_ = total = 0;
		t_ = x / (i*f + 2);
		best = t_;
		while(1) {
			t += c / (i*f + 2);
			t_ = x / ((i+1)*f + 2);
			total = t + t_;
			if(best < total) {
				break;
			}
			else
				best = total;
			i++;
			//cout<<t<<" "<<t_<<" "<<total<<" "<<best<<"\n";
		}
		cout<<"Case #"<<test<<": ";//<<best<<"\n";
		printf("%.7lf\n", best);
	}
	return 0;
}