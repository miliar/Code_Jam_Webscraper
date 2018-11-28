#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

bool is_numeric(string &line)
{
    char* p;
    strtol(line.c_str(), &p, 10);
    return *p == 0;
}

int main() {

	int cases;
	cin >> cases;
	vector<int> max_shyness(cases);
	vector<vector<int> > num_people(cases);
	for (int i=0; i<cases; ++i) {
		int max;
		cin >> max;
		string num;
		cin >> num;
		max_shyness[i] = max;
		for (const char& j : num) {
			num_people[i].push_back(j - '0');
		}
	}

	for (int i=0; i<cases; ++i) {
		int max = max_shyness[i];
		vector<int>& a = num_people[i];

		int needed = 0;
		int up_until = 0;
		for (int j=0; j<=max; ++j) {
			if (j>up_until) { // need more people
				int this_needed = (j-up_until);
				needed += this_needed;
				up_until += this_needed;
			}
			up_until += a[j];
		}
		cout << "Case #" << (i+1) << ": " << needed << endl;
	}


	return 1;
}