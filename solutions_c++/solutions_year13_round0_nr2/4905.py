#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t=1; t<=T; t++) {
		int N, M;
		cin >> N >> M;

		int bigger_in_row[N],
			bigger_in_column[M],
			lawn[N][M];

		for (int i=0; i<N; i++)
			bigger_in_row[i] = 0;

		for (int i=0; i<M; i++)
			bigger_in_column[i] = 0;

		for (int i=0; i<N; i++)
			for (int j=0; j<M; j++) {
				cin >> lawn[i][j];
				bigger_in_row[i] = max(lawn[i][j], bigger_in_row[i]);
				bigger_in_column[j] = max(lawn[i][j], bigger_in_column[j]);
			}

		bool possible = true;
		for (int i=0; i<N; i++)
			for (int j=0; j<M; j++) {
				if (lawn[i][j] < bigger_in_row[i] && lawn[i][j] < bigger_in_column[j]) {
					possible = false;
					goto Result;
				}
			}

		Result:
			string answer;
			if (possible)
				answer = "YES";
			else
				answer = "NO";

			cout << "Case #" << t << ": " << answer	<< endl;
	}
}