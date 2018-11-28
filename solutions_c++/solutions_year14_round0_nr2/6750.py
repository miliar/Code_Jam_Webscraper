#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int t,num = 1;;
	cin >> t;
	while(t--){
		double c,f,x;

		cin >> c >> f >> x;
		double total = 0.0, init = 2.0;
		while( x / init > x / (init+f) + c / init){
			total += c / init + 0.1e-7;
			init += f;
		}
		total += x / init;

		cout  << fixed << setprecision(7)<< "Case #" << num++ << ": " << total << endl;
	}
	return 0;
}