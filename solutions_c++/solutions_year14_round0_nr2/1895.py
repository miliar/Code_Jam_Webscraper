#include<iostream>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;

int main(){
	ifstream ifs("B-large.in");
	ofstream ofs("B-large.out");
	int numCases;
	ifs>>numCases;
	double C, F, X, FP;
	for(int q = 0; q<numCases; q++){
		FP = 2;
		ifs>>C;
		ifs>>F;
		ifs>>X;
		double second = 0;
		while(1){
			double lhs = X/FP, rhs = C/FP + X/(FP + F);
			if( lhs > rhs){
				second += C/FP;
				FP += F;
			}else{
				second += X/FP;
				break;
			}
		}
		ofs<<fixed;
		ofs.precision(7);
		ofs<<"Case #"<<q+1<<": "<<second<<endl;
	}

	system("pause");
}