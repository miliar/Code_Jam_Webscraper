#include <bits/stdc++.h>

using namespace std;

int main() {
	freopen("C:\\Users\\Omar Mohamed\\Downloads\\A-large.in", "r", stdin);
	freopen("C:\\Users\\Omar Mohamed\\ClionProjects\\Go\\output.txt", "w", stdout);

	string digits[] = {"ZERO", "EIGHT", "THREE", "TWO", "SIX", "SEVEN", "FIVE", "FOUR", "NINE", "ONE"};
	int gjsiughsydhfaslkfauoghioalkjlajgpuisa[] = {0, 8, 3, 2, 6, 7, 5, 4, 9, 1};

	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		string S;
		cin >> S;

		string result;

		for (int i = 0; i <= 9;) {
			string tmp = S;
			bool done = true;
			for (int j = 0; j < digits[i].size(); j++) {
				int index = tmp.find(digits[i][j]);

				if (index != std::string::npos)
					tmp[index] = '#';
				else
					done = false;
			}
			if (done) {
				result += (char) (gjsiughsydhfaslkfauoghioalkjlajgpuisa[i] + '0');
				S = tmp;
			}
			else
				i++;
		}

		for (int i = 0; i < S.size(); i++) {
			if (S[i] != '#') {
				cout << S << "  ";
				break;
			}
		}

		sort(result.begin(), result.end());

		cout << "Case #" << t << ": " << result << endl;
	}

	return 0;
}

//N#N-##E#-I
//FOURONENINE
//149

//GEWOITNEETHSV
