#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>

using namespace std;

int main() {

	freopen("C-small-1-attempt0.in","r",stdin);
	freopen("C-small-1-attempt0.out","w",stdout);

	int T, R, N, M, K;
	vector<int> product;
	cin >> T >> R >> N >> M >> K;
	cout << "Case #1:" << endl;
	for (int i = 0; i < R; i++) {
		long p;
		product.clear();
		for (int j = 0; j < K; j++) {
			cin >> p;
			product.push_back(p);
		}

		int size = 0;
		vector<int> guess;
		for (vector<int>::iterator it = product.begin(); it != product.end() ; ++it) {
			if (guess.size() >= N)
				break;

			if (*it == 1)
				continue;
			else if (*it == 2) {
				guess.push_back(2);
				continue;
			} else if (*it == 3) {
				guess.push_back(3);
				continue;
			} else if (*it == 4) {
				continue;
			} else if (*it == 5) {
				guess.push_back(5);
				continue;
			}  else if (*it == 7) {
				guess.push_back(7);
				continue;
			} 
			else if (*it == 9) {
				guess.push_back(3);
				guess.push_back(3);
			} else {
				int guessNum = M;
				float tmp = (float)*it;
				float tester;
				while (guessNum >= 2 && guess.size() < N) {
					tester = (float)tmp/guessNum;
					if (floor(tester) == tester) {
						tmp = tester;
						guess.push_back(guessNum);
					} else
						guessNum--;
				}
			}
		}

		if (guess.size() < N) {
			for (int j = 0; j < guess.size() - N; j++) {
				guess.push_back(2);
			}
		}
		for (int j = 0; j < N; j++) {
			cout << guess[j];
		}
		cout << endl;
	}


	//cout << "Case #" << i+1 << ": " << count << endl;

	return 0;
}