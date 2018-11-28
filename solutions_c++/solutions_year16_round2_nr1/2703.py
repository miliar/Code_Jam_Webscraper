#include <iostream>
#include <tuple>
#include <sstream>
#include <cmath>
#include <ctime>
#include <cassert>
#include <cstdio>
#include <vector>
#include <queue>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <fstream>
#include <cstdlib>
#include <string>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <memory>
#include <array>

using namespace std;

string solve(string s)
{
	array<string, 10> digits = { "ZERO", "SIX", "EIGHT", "TWO", "FOUR", "THREE", "FIVE", "SEVEN", "ONE", "NINE" };
	array<char, 10> digitsch = { '0', '6', '8', '2', '4', '3', '5', '7', '1', '9' };

	string solution;
	for (int i = 0; i < 10; ++i) {
		const string test = digits[i];
		
		bool found = true;
		while (found) {
			string slough;
			for (char c : test) {
				size_t it = s.find(c);
				if (it == string::npos) {
					found = false;
					break;
				}
				else {
					slough.push_back(c);
					s.erase(it, 1);
				}
			}

			if (found) {
				solution.push_back(digitsch[i]);
			}
			else {
				s += slough;
			}
		}
	}

	sort(solution.begin(), solution.end());

    return solution;
}

int main()
{
    int numCases;
    cin >> numCases;

    int casen = 0;
	string s;
    while (++casen, cin >> s) {
        cout << "Case #" << casen << ": ";

		string solution = solve(s);

		cout << solution;

        cout << endl;
    }

    return 0;
}

