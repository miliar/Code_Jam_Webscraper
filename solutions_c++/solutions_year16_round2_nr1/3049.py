#include <iostream>
#include <string>

using namespace std;

int main() 
{
	int tests;
	cin >> tests;
	
	for (int i = 0; i < tests; ++i) {
		string num;
		int lets[26] = {0};
		int nums[10] = {0};
		cin >> num;
		int l = num.length();
		for (int j = 0; j < l; ++j) {
			++lets[num[j] - 'A'];
		}
		cout << "Case #" << i + 1 << ": ";
			
		nums[0] = lets[25];
		lets[4] -= lets[25];
		lets[17] -= lets[25];
		lets[14] -= lets[25];
		nums[2] = lets[22];
		lets[19] -= lets[22];
		lets[14] -= lets[22];
		lets[4] -= lets[7] * 2;
		nums[4] = lets[20];
		lets[5] -= lets[20];
		lets[14] -= lets[20];
		lets[17] -= lets[20];
		nums[5] = lets[5];
		lets[8] -= lets[5];
		lets[21] -= lets[5];
		lets[4] -= lets[5];
		nums[6] = lets[23];
		lets[8] -= lets[23];
		lets[18] -= lets[23];
		nums[7] = lets[18];
		lets[4] -= lets[18] * 2;
		lets[13] -= lets[18];
		nums[8] = lets[6];
		lets[8] -= lets[6];
		lets[7] -= lets[6];
		nums[3] = lets[7];
		lets[19] -= lets[7];
		lets[17] -= lets[7];
		nums[9] = lets[8];
		nums[1] = lets[14];
			
			
			
			
			
		for (int j = 0; j < 10; ++j) {
			//cout << nums[j] << endl;
			while (nums[j]--) cout << j;
		}
		cout << endl;
		
		
	}
	
	return 0;
}