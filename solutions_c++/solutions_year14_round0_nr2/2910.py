//cookie.cc

#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <iomanip> 

using namespace std;

int main(){
	ifstream input_file;
	ofstream output_file;
	input_file.open("B-large.in");
	output_file.open("B-large-1-ans.out");
	int t= 0;
	int k = 1;
//	cin >> t;
	input_file >> t;

	while(t){
		double C,F,X, time = 0;
//		cin >> C >> F >> X;
		input_file >> C >> F >> X;
		double cps = 2;
		time = 0;
		int cookie = 1;
		int j = 1;
		if( C < X ){
	//		int j = 1;
			while( X/cps >= C/cps +  X/(cps+F)){
				time = time + C/cps;
				cps = cps + F;
//				cookie = j*cps;
//				j = j + 1;
//					if(cookie == C){
//						cps = cps + F;
//						time = time + C/cookie;
//						cookie = 0;
//						j = 1;
//					}
				}
				time = time + X/cps;
			}
		else{
			time = X/cps;
		}
//		cout << "Case #" << k << ": " << std::fixed << std::setprecision(8) << time << "\n";
		output_file << "Case #" << k << ": " << std::fixed << std::setprecision(8) << time << "\n";
//		printf("Case #%d: %0.7f\n", k, time);
		k = k + 1;
		t = t - 1;
	}
	return 0;
}
