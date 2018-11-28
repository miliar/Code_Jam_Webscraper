#include <iostream>
#include <iomanip> 

using namespace std;

int T;
double C,X,F;
int tc;
int solve(){
	tc++;
	cin >> C >> F >> X;
	double r = 2.0, res=0.0;
	
	while(1){
		double r1  = X/r;
		double r2  = (C/r) + (X)/(r+F);
		if(r1 <= r2 ){
			res += r1;
			break;
		}else{
			res += (C/r);
			r += F;
		}
		//cout << res << "\t" << X << "\t" << r<< endl;
	}
	cout << std::fixed;
	cout << std::setprecision(7);
	cout << "Case #"<<tc<<": "<< res << endl;
	return 0; 
}

int main(){
	cin >> T;
	while(T--) solve();
}
