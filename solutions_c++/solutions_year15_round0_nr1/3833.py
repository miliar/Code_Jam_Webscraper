#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	ifstream fin(argv[1]);
	int n;
	fin >> n;
	for(int i = 0; i < n; i++) {
		int max_s;
		string counts;
		fin >> max_s >> counts;

		int sum = 0;
		int friends = 0;
		sum = counts[0] - '0';

		for(int j = 1; j <= max_s; j++) {
			int count = counts[j] - '0';
			if(count > 0 && sum + friends < j) {
				friends += (j - sum - friends);
			}
			sum += count;
		}
		cout << "Case #" << (i + 1) << ": " << friends << endl;
	}
	fin.close();
}