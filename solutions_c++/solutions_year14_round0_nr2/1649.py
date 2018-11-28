#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;


int main(void){
	unsigned T;
	ifstream fin("B-large.in");
	ofstream fout("B-large.out");
	fin>>T;
	for (unsigned t=1; t<=T; t++){
		double rate = 2.0;
		double totalTime = 0.0;
		double c, f, x;
		fin >> c >> f >> x;
		double cur = 0.0;
		if (x<=c){
			cur = x;
			totalTime = x/rate;
		}
		while (cur < x){
			if (cur < c){
				totalTime = totalTime + (c-cur)/rate;
				cur = c;
			}
			double remain = x-cur;
			double t0 = totalTime +  remain/rate;
			double t1 = totalTime + (remain+c)/(rate+f);
			if (t0<=t1){
				totalTime = t0;
				break;
			}
			else {
				rate = rate + f;
				cur = cur-c;
			}
		}
		fout <<"Case #"<<t<<": "<<fixed << setprecision(7)<<totalTime<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}