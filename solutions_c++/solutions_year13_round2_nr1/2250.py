#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int solve(vector<int> &motes, long long A) {
	int N = motes.size();
	int nMoves = 0;
	if(A == 1) return N;
	for(int i = 0; i < N; i++) {
		if(A > motes[i]) {
			A += motes[i];
			motes[i] = 0;
		} else {
			// add or remove?
			long long amount = 0;
			int nAdd = 0;
			// how many additions are needed to eat the next mote?
			while(A + amount <= motes[i]) {
				//cout << (A + amount - 1) <<  " : " ;
				amount += (A + amount) - 1;
				//cout << ( A + amount) << endl;
				nAdd++;
			}
			int nRemove = N - i;
			if(nAdd < nRemove) {
				A += amount + motes[i];
				motes[i] = 0;
				nMoves += nAdd;
			} else {
				nMoves += nRemove;
				break;
			}
		}
	}
	return nMoves;
}
int main(int argc, char ** argv) {
	int T;
	cin >> T;
	
	for(int tcases = 1; tcases <= T; tcases++) {
		int A, N;
		cin >> A >> N;
		vector<int> motes;

		for(int i = 0; i < N; i++) {
			int m;
			cin >> m;
			motes.push_back(m);
		}

		sort(motes.begin(), motes.end());

		int nMoves = solve(motes, A);

		cout << "Case #" << tcases << ": " << nMoves << endl;

	}
	return 0;
}

/*
2 6
 9 64 19 16 81 80
*/