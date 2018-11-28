#include<iostream>
#include<vector>
#include<string>
#include<fstream>
using namespace std;

int main() {
	int t;
	ifstream inputF("Large Input.in");
	ofstream output("Large Output.out");
	inputF >> t;
	for (int i = 0; i < t; i++) {
		string input;
		inputF >> input;
		vector<bool> pancakes;
		for (int j = 0; j < input.length(); j++) {
			if (input[j] == '+')
				pancakes.push_back(true);
			else pancakes.push_back(false);

		}
		
		int times = 0;
		bool isSame;
		do {
			isSame = true;
			for (int j = 0; j < pancakes.size() - 1; j++) {
				bool last = pancakes[j];
				bool current = pancakes[j + 1];
				if (last != current) {
					isSame = false;
					for (int k = 0; k < j + 1; k++) 
						pancakes[k] = !pancakes[k];
					times++;
					break;
				}
			}


		} while (isSame == false);

		if (pancakes[0] == false)
			times++;
		output<< "Case #" + to_string(i+1) + ": " + to_string(times) << endl;



	}
	

	return 0;

}