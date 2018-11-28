#include <iostream>
#include <iomanip>
#include <fstream>
using namespace std;
int main(){
	ifstream ifs("B-large.in");
	ofstream ofs("output.txt");
	int n; ifs >> n ;
	for(int i=1;i<=n;++i){
		double C, F, X; ifs >> C >> F >> X ;
		double MIN=X/2.0;
		for(int j=1; ;++j){
			double tmp=0.0;
			tmp+=X/(2+j*F);
			for(int k=0;k<j;++k) tmp+=C/(2+k*F);
			if(tmp<MIN) MIN=tmp;
			else break;
		}
		ofs << fixed << setprecision(7);
		ofs << "Case #" << i << ": " << MIN << '\n';
	}
}