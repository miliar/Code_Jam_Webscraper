#include <iostream>
#include <string>
using namespace std;

int main() {

	int T; 
	cin >> T;
	for (int i = 1; i <= T; i++) {
		long N;
		cin >> N;
		if (N == 0) {

			cout << "Case #" << i << ": " << "INSOMNIA "<<endl;
			continue;
		}
		int j = 1;
		bool *p = new bool [10];
		for (int k = 0; k < 10; k++) {
			p[k] = false;
		}
		long value;
		int temp;
		bool correct = false;
		while (true) {
			value = j * N;
		 	temp = 0;
			while (value > 0) {
				temp = value %10;
				value = value / 10;
				p [temp] = true;
			}
			for (int k = 0; k < 10; k++) {
                    		if ( !p[k]) {
					j++;
					correct = false;
					break;
				}
				correct = true;
               		}
			if (correct) {
				value = j * N;
				cout << "Case #" << i << ": " << value << " " <<endl;
				break;
			}


		}
	}
	return 0;
}
