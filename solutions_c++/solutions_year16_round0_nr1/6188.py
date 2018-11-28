#include <iostream>
#include <fstream>
#include <map>

using namespace std;

int main() {
	ifstream file("input.txt");
	int times;
	file >> times;
	for (int i = 0; i < times; i++) {
		map<int, int> m;
		int num;
		file >> num;
		bool terminate = false;
		if (num == 0) {
			cout << "Case #" << i +1 << ": " << "INSOMNIA\n"; 
			continue;
			cout << "LOL";
			// fuck this
		}
		int num1 = num;
		for (int j = 0; j < 10000; j++) { // going to multiply 45 times at max.
			int temp = num1;
			while (temp !=0) {
				int digit = temp%10;
				m[digit] = 1;
				temp = temp/10;
				if (m.size() >= 10) {
					// terminate this test case. we have won.
					terminate = true;
					break;
				}
			}
			
			if (terminate)
				break;
			num1 = num1 + num;
		}
		cout << "Case #" << i +1 << ": ";
		if (terminate)
			cout << num1 << "\n";
		else
			cout << "INSOMNIA\n";

	}
}