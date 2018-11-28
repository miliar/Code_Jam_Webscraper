#include <iostream>
#include <unordered_map>
using namespace std;


int table [4][4] = { 	{1, 2, 3, 4},
						{2, 1, 4, 3},
						{3, 4, 1, 2},
						{4, 3, 2, 1}};
int stable [4][4] = { 	{1, 1, 1, 1},
						{1,-1, 1,-1},
						{1,-1,-1, 1},
						{1, 1,-1,-1}};

unordered_map< string, bool > dp;

int convert(char a) {
	switch(a) {
		case '1':
			return 1;
		case 'i':
			return 2;
		case 'j':
			return 3;
		case 'k':
			return 4;
	} 
//	cout << "[" << a << "]" << endl;
	exit(-1);
}

int multiply(int a, int b) {
//	cout << a << "," << b << " = ";
	int sign = 1;
	if (a < 0) {
		a = a * -1;
		sign = -1;
	}
	int csign = stable[a-1][b-1];
	int cval = table[a-1][b-1];
	int val = csign * cval * sign;
//	cout << val << endl;
	return val;
}

bool check(string str, int target) {
	int acc = 0;
	if (target == 5) {
		return (str.length() == 0);
	}
//	cout << "Start checking " << str << " for " << target << endl;
	for(int i = 0; i < str.length(); ++i) {
//		cout << "-" << acc << " " << str[i] << endl;
		if (i == 0)
			acc = convert(str[0]);
		else
			acc = multiply(acc, convert(str[i]));
//		cout << acc << "[" << target << "]" << endl;
		if ( acc == target ) {
			string cur (str, 0, i + 1);
			string next (str, i + 1, -1);
//			cout << cur << "|" << next << endl;
			string key = next + ":" + to_string(target);
			bool ret;
			if (dp.count(key) == 0){
				ret = check(next, target + 1);
				dp[key] = ret;
			} else
				ret = dp[key];
			if (ret)
				return true;
		}
	}
	return false;
}

int main () {
	int turn;
	cin >> turn;

	for (int round = 1; round <= turn; ++ round) {
		bool ok = false;
		
		int len, repeat;
		cin >> len >> repeat;

		string input;
		cin >> input;

		string full = "";
		for (int i = 0; i < repeat; ++i) {
			full += input;
		}
		
//		cout << full << endl;
		ok = check(full, convert('i'));
//		cout << full << endl;
		
		

		if (ok)
			cout << "Case #" << round << ": YES" << endl;
		else
			cout << "Case #" << round << ": NO" << endl;
	}

	return 0;
}
