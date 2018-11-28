#include <iostream>
#include <stdio.h>
#include <fstream>
#include <stack>
#include <queue>
#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>

using namespace std;

int main() {
	ifstream in("B-small-attempt1.in");
	ofstream out;
	out.open("B-small.out");
	int T;
	in >> T;
	int n;
	long double V, X;
	for(int t = 0; t < T; t++){
		vector<long double> rate;
		vector<long double> temp;
		in >> n >> V >> X;	
		for(int i = 0; i < n; i++){
			long double ri, ci;
			in >> ri >> ci;
			rate.push_back(ri);
			temp.push_back(ci);
			cout << rate[i] << "  " << temp[i] << endl;
		}
		bool low = false;
		bool high = false;
		for(int i = 0; i < n; i++){
			if(temp[i] == X){
				low = high = true;
				break;
			}
			if(temp[i] > X){
				high = true;
			}
			else if(temp[i] < X){
				low = true;
			}
		}
		cout << "Case " << t+1 << endl;
		cout << V << "  " << rate[0] << "  "  << rate[1] << endl;
		if(!low || !high){
			out << "Case #" << t+1 << ": " << "IMPOSSIBLE" << endl;
			continue;
		}
		if(n == 1) {
			out << "Case #" << t+1 << ": " << setprecision(15)<< V/rate[0] << endl;
			continue;
		}
		if(temp[0] == temp[1]){
			out << "Case #" << t+1 << ": " << setprecision(15)<< V/(rate[0]+rate[1]) << endl;
			continue;
		}
		if(temp[0] == X){
			out << "Case #" << t+1 << ": " << setprecision(15)<< V/rate[0] << endl;
			continue;
		}
		if(temp[1] == X){
			out << "Case #" << t+1 << ": " << setprecision(15)<< V/rate[1] << endl;
			continue;
		}
		if(temp[0] > temp[1]) {
			long double tr = rate[0];
			rate[0] = rate[1];
			rate[1] = tr;
			long double tt = temp[0];
			temp[0] = temp[1];
			temp[1] = tt;
		}
		long double v1 = V*(X-temp[0])/(temp[1]-temp[0]);
		cout << v1 << endl;
		long double v0 = V*(temp[1] - X)/(temp[1]-temp[0]);
		cout << v0 << endl;
		long double t0 = v0 / rate[0]; 
		long double t1 = v1 / rate[1];
		out << "Case #" << t+1 << ": " << setprecision(15) << max(t0, t1) << endl;
		
	}

	out.close();
	return 0;
}
