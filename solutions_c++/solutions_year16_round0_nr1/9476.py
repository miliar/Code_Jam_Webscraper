#include <fstream>
using namespace std;

int main() {
	ifstream input("input.txt");
	ofstream output("output.txt");

	int t;
	long long int num;

	input >> t;

	for (int i = 1; i <= t;i++) {
		input >> num;
		long long int temp = num;
		int n = 1;

		if (num != 0) {
			bool shapes[10] = { false,false,false,false,false,false,false,false,false,false };
			bool flag = false;

			while (!flag) {
				temp = num * n;
				while (temp > 0) {
					int digit = temp % 10;
					temp /= 10;
					shapes[digit] = true;
				}
				flag = shapes[0] && shapes[1] && shapes[2] && shapes[3] && shapes[4] && shapes[5] && shapes[6] && shapes[7] && shapes[8] && shapes[9];
				n++;
			}
			n--;
			output << "Case #" << i << ": " << n * num << endl;
		}else 
			output << "Case #" << i << ": " << "INSOMNIA" << endl;
	}
	return 0;
}