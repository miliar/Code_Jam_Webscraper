

#include <algorithm>
#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <sstream>
#include <map>
#include <limits>
#include <cmath>

using namespace std;

int main() {

	int cases;
	cin>>cases;
	for (int k = 1; k<=cases; k++) {
		long double time=0.0;
		long double freq=2.0;
		long double c,f,x;
		cin>>c>>f>>x;

		while(true){
			time+=c/freq;
			if(((x-c)/freq)<(x/(freq+f)))
			{
				time+=(x-c)/freq;
				break;
			}
			//continue getting farms
			freq+=f;
		}

		cout.precision(12);
		cout<<"Case #"<<k<<":"<<" "<<fixed<<time<<endl;
	}
	return 0;
}

