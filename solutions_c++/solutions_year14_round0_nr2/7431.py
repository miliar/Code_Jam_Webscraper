#include <iomanip>
#include <iostream>

using namespace std;

int main(int argc, char **argv){
	size_t t;
	cin >> t;
	for(register size_t i = 1; i <= t; i++){
		double c, f, x;
		double r = 2.0;
		double tm = 0.0;
		cin >> c >> f >> x;
		while(true){
			if((x / r) < ((c / r) + (x / (r + f)))){
				tm += x / r;
				break;
			} else {
				tm += c / r;
				r += f;
			}
		}
		cout << "Case #" << i << ": " << setprecision(13) << tm << endl;
	}
	return 0;
}
