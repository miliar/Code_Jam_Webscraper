bool debug=false;
#include <iostream>
#include <cstring>
#define N 4
using namespace std;

int cards[5][5];
bool appeard[20];

int main() {

	int cases;
	cin >> cases;
	for(int T=1; T<=cases; ++T) {

		int row;
		cin >> row;
		--row;
		for(int i=0; i<N; ++i) for(int j=0; j<N; ++j)
			cin >> cards[i][j];

		memset(appeard, false, sizeof(appeard));
		for(int j=0; j<N; ++j) {
			appeard[cards[row][j]]=true;
			if(debug) {
				cout << " > " << cards[row][j] << endl;
			}
		}

		cin >> row;
		--row;
		for(int i=0; i<N; ++i) for(int j=0; j<N; ++j)
			cin >> cards[i][j];

		int cnt=0, ans;
		for(int j=0; j<N; ++j)
			if (appeard[cards[row][j]]) {
				++cnt;
				ans = cards[row][j];
			}

		cout << "Case #" << T << ": ";
		if (cnt > 1)
			cout << "Bad magician!" << endl;
		else if (cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << ans << endl;

	}

	return 0;

}
