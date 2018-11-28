#include <iostream>
#include <tuple>
#include <sstream>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <algorithm>
#include <numeric>
#include <algorithm>
#include <iterator>
#include <iostream>

using namespace std;

typedef char u8;
typedef int i16;
typedef unsigned int u16;
typedef long int i32;
typedef unsigned long int u32;
typedef long long int i64;
typedef unsigned long long int u64;

array<string, 10> digitsString = 
{
	"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"
};

array<pair<char, u16>, 10>  uniqChar = { {
	{'Z', 0},
	{'G', 8},
	{'U', 4},
	{'X', 6},
	{'S', 7},
	{'V', 5},
	{'R', 3},
	{'T', 2},
	{'O', 1},
	{'I', 9}
} };

void calculate(u32 number, u32 howMany, vector<i32>& letters) {
	for(char l : digitsString[number]) {
		letters[l-'A'] -= howMany;
	}
}

string solve(string S) {
	vector<i32> letters(26, 0);
	vector<i32> digits(10, 0);

	for (char c: S ) {
		letters[c-'A']++;
	}

	for (const auto p: uniqChar) {
		if (letters[p.first-'A'] > 0) {
			digits[p.second] = letters[p.first-'A'];
			calculate(p.second, digits[p.second], letters);
		}
	}

	ostringstream oss;

	for(u32 j=0; j<=9; ++j) {
		for(u32 i=0; i<digits[j]; ++i) {
			digits[j];
			oss << j;
		}
	}

	return oss.str();
}

int main() {
    ios::sync_with_stdio(false);
    cout.precision(10);
    cout << fixed;

    u16 cases;

    cin >> cases;

    for(u16 i=0; i<cases; ++i) {
    	string S;
    	cin >> S;
    	auto out = solve(S);
    	cout << "Case #" << i+1 << ": " << out << "\n";
    }


    return 0;
}
