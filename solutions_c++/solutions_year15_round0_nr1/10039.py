#include<iostream>
#include<string>
#include<vector>
#include<fstream>

using namespace std;

int function(int * people, int max) {
	int result = 0, invitees = 0, total = 0;
	for (int j = 0; j < max + 1; j++) {
		if (people[j] > 0) {
			if ((j - total) > 0) {
				result += (j - total);
				total += result;
			}
			total += people[j];
		}
	}
	return result;
}

int main(void) {
	ifstream file;
	ofstream output;
	output.open("out.out");
	file.open("input.in");
	int test_cases;
	string test;
	getline(file, test);
	test_cases = atoi(test.c_str());

	int max, case_num, j, invitees, total, result;
	string input;
	const char * m;
	int * shyness = new int[];

	for (int i = 0; i < test_cases; i++) {
		case_num = i + 1;
		getline(file, input);
		output << "Case #" << case_num << ": ";

		m = input.c_str();
		max = atoi(m);
		m += 2;
		j = 0, total = 0, invitees = 0, result = 0;
		while (*m != '\0') {
			shyness[j] = (*m - 48);
			total += shyness[j];
			j++, m++;
		}
		output << function(shyness, max);
		output << endl;
	}
	file.close();
	output.close();
	return 0;
}