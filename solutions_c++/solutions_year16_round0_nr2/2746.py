#include <fstream>
#include <string>

using namespace std;

int main() {
	ifstream infile("B-large.in");
	ofstream outfile("B.out");
	
	int n, count;
	
	infile >> n;
	
	for (int i = 0; i < n; i++) {
		string input;
		infile >> input;
		bool needsFlip = (input[0] == '-');
		count = 0;
		for (int j = 0; j < input.size(); j++) {
			if (!needsFlip) {
				if (input[j] == '+') {
					continue;
				} else {
					count++;
					needsFlip = true;
				}
			} else {
				if (input[j] == '-') {
					continue;
				} else {
					count++;
					needsFlip = false;
				}
			}
		}
		
		count += needsFlip;

		outfile << "Case #" << i+1 << ": " << count << endl;
	}
}
