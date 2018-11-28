#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int main() {
	int T;
	char s[4096];
	int cnt[256];
	vector<int> lst;

	scanf_s("%d\n", &T);

	for (int i = 1; i <= T; ++i) {
		
		cin.getline(s, sizeof(s));
		//cout << "S : " << s << "\n";

		memset(cnt, 0, sizeof(cnt));

		for (int j = 0; s[j]; ++j) {
			++cnt[s[j]];
		}


		lst.clear();

		while (1) {

			if (cnt['Z'] > 0 && cnt['E'] > 0 && cnt['R'] > 0 && cnt['O'] > 0) {
				--cnt['Z']; --cnt['E']; --cnt['R']; --cnt['O'];
				lst.push_back(0);
				continue;
			}


			if (cnt['E'] > 0 && cnt['I'] > 0 && cnt['G'] > 0 && cnt['H'] > 0 && cnt['T'] > 0) {
				--cnt['E']; --cnt['I']; --cnt['G']; --cnt['H']; --cnt['T'];
				lst.push_back(8);

				continue;
			}

			if (cnt['S'] > 0 && cnt['I'] > 0 && cnt['X'] > 0) {
				--cnt['S']; --cnt['I']; --cnt['X'];		
				lst.push_back(6);

				continue;
			}

			if (cnt['T'] > 0 && cnt['H'] > 0 && cnt['R'] > 0 && cnt['E'] > 0 && cnt['E'] > 0) {
				--cnt['T']; --cnt['H']; --cnt['R']; --cnt['E']; --cnt['E'];
				lst.push_back(3);

				continue;
			}

			if (cnt['T'] > 0 && cnt['W'] > 0 && cnt['O'] > 0 ) {
				--cnt['T']; --cnt['W']; --cnt['O'];
				lst.push_back(2);

				continue;
			}

			if (cnt['S'] > 0 && cnt['E'] > 0 && cnt['V'] > 0 && cnt['E'] > 0 && cnt['N'] > 0) {
				--cnt['S']; --cnt['E']; --cnt['V']; --cnt['E']; --cnt['N'];
				lst.push_back(7);

				continue;
			}

			if (cnt['F'] > 0 && cnt['I'] > 0 && cnt['V'] > 0 && cnt['E'] > 0) {
				--cnt['F']; --cnt['I']; --cnt['V']; --cnt['E']; 
				lst.push_back(5);

				continue;
			}

			if (cnt['F'] > 0 && cnt['O'] > 0 && cnt['U'] > 0 && cnt['R'] > 0) {
				--cnt['F']; --cnt['O']; --cnt['U']; --cnt['R'];
				lst.push_back(4);

				continue;
			}

			if (cnt['N'] > 0 && cnt['I'] > 0 && cnt['N'] > 0 && cnt['E'] > 0) {
				--cnt['N']; --cnt['I']; --cnt['N']; --cnt['E'];
				lst.push_back(9);

				continue;
			}		
			
			if (cnt['O'] > 0 && cnt['N'] > 0 && cnt['E'] > 0) {
				--cnt['O']; --cnt['N']; --cnt['E'];
				lst.push_back(1);

				continue;
			}

			break;
		}

		std::sort(lst.begin(), lst.end());

	
		cout << "Case #" << i << ": ";
		for (auto x : lst) {
			cout << x;
		}
		cout << "\n";
	}

	return 0;
}