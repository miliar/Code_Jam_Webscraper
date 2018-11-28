#include <fstream>
#include <iostream>
#include <unordered_set>


using namespace std;
int main() {
	ifstream input;
	ofstream output;
	input.open("A-large.in");
	output.open("output.in");
	int t;
	input >> t;

	for (int i = 0; i < t; ++i) {
		long long number;
		input >> number;
		if (number > 0) {
			long long num = 0;
			unordered_set<long long> count;
			while (count.size() != 10) {
				num += number;
				long long temp=num;
				while (temp > 0) {
					count.emplace(temp % 10);
					temp = temp / 10;
				}


			}
			output << "Case #" << i + 1 << ": " << num << endl;
		}
		else { output << "Case #" << i + 1 << ": INSOMNIA" << endl; }
	}

	output.close();
	input.close();
	return 0;
}