#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
#include <fstream>
using namespace std;



int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w", stdout);
	int T;
	cin>>T;
	for (int t = 0; t < T; t++){
		double c,f,x;
		cin>>c>>f>>x;
		double time = 0;
		double dc = 2;
		double mintime = x/dc;
		while (true) {
			time+=c/dc;
			dc+=f;
			double tm = x/dc + time;
			if (tm < mintime) mintime = tm;
			else break;
			
		}
		cout.setf(ios::fixed);
		cout.precision(7);
		cout<<"Case #"<<t+1<<": ";
		cout<<mintime<<endl;
	}
	return 0;
}
