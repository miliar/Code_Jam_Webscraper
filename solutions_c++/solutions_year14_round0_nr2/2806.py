#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int T;
	double C, F, X;
	cin >> T;
	for (int i=1;i<=T;i++){
		cin >> C >> F >> X;
		double a=2, tt=0;
		while (X/(a+F) < (X-C)/a){
			tt += C/a;
			a += F;
		}
		tt += X/a;
		cout << "Case #" << i << ": " << setprecision(7) << fixed << tt << endl;
	}
}
