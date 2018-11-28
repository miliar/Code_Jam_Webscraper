#include <iostream>
#include <fstream>

using namespace std;

int main() {
	fstream in("input.txt");
	int n;
	in >> n;
	for(int i = 1; i <= n; i++) {
		double C, F, X;
		in >> C >> F >> X;
		double rate = 2.0;
		double minimum = X/rate;
		while(true) {
			rate += F;
			double temp = X/rate;
			double temp_rate = 2;
			while(temp_rate < rate) {
				temp += C/temp_rate;
				temp_rate += F;
			}
			
			if(temp < minimum)
				minimum = temp;
			else
				break;
		}
		printf("Case #%d: %.7lf\n", i, minimum);
	}
	in.close();
	return 0;
}