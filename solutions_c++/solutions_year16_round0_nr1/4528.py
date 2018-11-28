#include <iostream>
#include <set>

using namespace std;

int main()
{
	int T, N;
	cin >> T;

	for (int caseN = 1; caseN <= T; caseN++) {
		cin >> N;
		string ans;

		if (N == 0) {
			ans = "INSOMNIA";
		} else {
			set<char> digits;
			int M = N;
			while (1) {
				string strM = to_string(M);
				for (char d : strM) {
					digits.insert(d);
				}

				if (digits.size() == 10)
					break;

				M += N;
			}
			ans = to_string(M);
		}

		cout << "Case #" << caseN << ": " << ans << endl;
	}
	return 0;
}