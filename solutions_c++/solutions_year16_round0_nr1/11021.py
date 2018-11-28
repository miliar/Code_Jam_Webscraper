#include <iostream>
#include <cstdlib>

using namespace std;

int remain = 10;

int main(int argc, char* argv[]) {

	int test_cases;
	cin >> test_cases;

	unsigned long long num_input;
	unsigned long long chances = 0;
	unsigned long long temp = 0;

	int mult = 1;
	for(int i = 0; i < test_cases; i++) {
		remain = 10;
		int num_list[10] = {};
		mult = 1;

		cin >> num_input;
		chances = 0;

		if(mult*num_input == 0) {
			cout << "Case #" << (i+1) << ": " << "INSOMNIA" << endl;
		} else {
			temp = mult*num_input;
			while(remain != 0) {
				chances = temp;
				while(temp != 0) {
					int last_d = temp%10;
					temp = temp/10;
					if(num_list[last_d] == 0) {
						num_list[last_d] = 1;
						remain--;
						if(remain == 0) {
							break;
						}
					}
				}
				if(remain == 0) {
					cout << "Case #" << (i+1) << ": " << chances << endl;
					break;
				}
				mult++;
				temp = num_input*mult;
			}	
		}
	}
	return 0;
}