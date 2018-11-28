
#include <iostream>
#include <string>

using namespace std;



int main()
{
	// Read number of testcases
	int numTestcases, number;
	cin >> numTestcases;

	for (int i = 1; i <= numTestcases; i++) {
		// Parse number as string
		int number;
		cin >> number;
		
		// Initialize table
		bool digit[10];
		for (int d = 0; d < 10; d++) digit[d] = false;

		bool hasBeenSeen = false;
		int lastNum = 0;
		for (int k = 1; k < 1000; k++)
		{
			// Set digits in the number to true
			lastNum = k * number;
			string numStr = to_string(k * number);
			for (int s = 0; s < numStr.length(); s++) digit[(uint8_t)(numStr.at(s)) - 0x30] = true;

			// All digits seen?
			hasBeenSeen = true;
			for (int d = 0; d < 10; d++) {
				if (digit[d] == false) hasBeenSeen = false;
			}
			if (hasBeenSeen == true) break;
		}

		if (hasBeenSeen == true) cout << "Case #" << i << ": " << lastNum << (char)(0x0D) << endl;
		else cout << "Case #" << i << ": INSOMNIA" << (char)(0x0D) << endl;
	}

}