#include <iostream>
#include <vector>
#include <string>
using namespace std;

char won(vector<char> v) {
	char who = 0;
	for (int i=0; i<4; ++i) {
		switch(v[i]) {
			case '.': return 0; break;
			case 'X': case 'O':
			if (who) {
				if (who != v[i]) return 0;
			} else who = v[i];
		}
	}
	return who;
}

int main(int argc, char* argv[]) {
	int N;
	cin >> N;

	for (int I=0; I<N; ++I) {
		cout << "Case #" << I+1 << ": ";

		bool full = true;

		vector<string> f;
		for (int i=0; i<4; ++i) {
			string line;
			cin >> line;
			f.push_back(line);

			for (int j=0; j<4; ++j)
				if (line[j] == '.')
					full = false;
		}

		char res;
		for (int i=0; i<4; ++i) {
			if (( res = won({f[i][0], f[i][1], f[i][2], f[i][3]}) )) {
				cout << res << " won";
				goto end;
			}
		}
		for (int i=0; i<4; ++i) {
			if (( res = won({f[0][i], f[1][i], f[2][i], f[3][i]}) )) {
				cout << res << " won";
				goto end;
			}
		}
		if (( res = won({f[0][0], f[1][1], f[2][2], f[3][3]}) )) {
			cout << res << " won";
			goto end;
		}
		if (( res = won({f[3][0], f[2][1], f[1][2], f[0][3]}) )) {
			cout << res << " won";
			goto end;
		}

		if (full) {
			cout << "Draw";
		} else {
			cout << "Game has not completed";
		}


		end:
		cout << endl;
	}
	cout << won({'X', 'X', 'O', 'X'});
}