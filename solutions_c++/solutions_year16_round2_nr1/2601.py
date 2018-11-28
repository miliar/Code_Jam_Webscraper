#define BA

#ifdef BA
#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

bool check(vector<char> *myvector, int N, string letters) {
	bool res = false;
	char c;
	if (N == 0) {
		c = 'Z';
	} 
	else if (N == 1) {
		c = 'O';
	} 
	else if (N == 2) {
		c = 'W';
	}
	else if (N == 3) {
		c = 'T';
	}
	else if (N == 4) {
		c = 'U';
	}
	else if (N == 5) {
		c = 'F';
	}
	else if (N == 6) {
		c = 'X';
	}
	else if (N == 7) {
		c = 'V';
	}
	else if (N == 8) {
		c = 'G';
	}

	vector<char>::iterator it;

	it = find(myvector->begin(), myvector->end(), c);
	if (it != myvector->end()) {
		myvector->erase(it);
		for (int j = 0; j < letters.length(); j++) {
			it = find(myvector->begin(), myvector->end(), letters[j]);
			myvector->erase(it);
		}
		return true;
	}
	else {
		return false;
	}
	return false;
}

int main() {
	//freopen("in.txt", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("out.txt", "wt", stdout);

	int T;
	scanf("%d\n", &T);

	for (int i = 1; i <= T; i++) {
		string str;
		getline(cin, str);

		vector <char> sets;
		for (int j = 0; j < str.length(); j++) {
			sets.push_back(str[j]);
		}

		vector <int> number;

		while (check(&sets, 0, "ERO") == true) {
			number.push_back(0);
		}
		while (check(&sets, 2, "TO") == true) {
			number.push_back(2);
		}
		while (check(&sets, 4, "FOR") == true) {
			number.push_back(4);
		}
		while (check(&sets, 6, "SI") == true) {
			number.push_back(6);
		}
		while (check(&sets, 8, "EIHT") == true) {
			number.push_back(8);
		}
		while (check(&sets, 1, "NE") == true) {
			number.push_back(1);
		}
		while (check(&sets, 3, "HREE") == true) {
			number.push_back(3);
		}
		while (check(&sets, 5, "IVE") == true) {
			number.push_back(5);
		}
		while (check(&sets, 7, "SEEN") == true) {
			number.push_back(7);
		}

		//last count 9
		for (int j = 0; j < sets.size(); j++) {
			if (sets[j]=='I')
				number.push_back(9);
		}

		sort(number.begin(),number.end());

		printf("Case #%d: ", i);
		for (int j = 0; j < number.size();j++)
			printf("%d", number[j]);
		printf("\n");
	}

	return 0;
}

#endif