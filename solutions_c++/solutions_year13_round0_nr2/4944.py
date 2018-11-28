#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
	int T;
	int N, M;
	cin >> T;
	int t = 1;
	while (t <= T){
		cin >> N >> M;
		vector<vector<int> > lawn(N, vector<int> (M));
		vector<int> maxrows(N,-1);
		vector<int> maxcols(M,-1);
		bool sol = true;
		for (int i = 0; i < N; ++i) {
			for (int j = 0; j < M; ++j) {
				cin >> lawn[i][j];
				if (maxrows[i] < lawn[i][j]) maxrows[i] = lawn[i][j];
			}
		}
		for (int i = 0; i < M; ++i) {
			for (int j = 0; j < N; ++j) {
				if (maxcols[i] < lawn[j][i]) maxcols[i] = lawn[j][i];
			}
		}
	
	
		for (int i = 0; i < N and sol; ++i) {
			for (int j = 0; j < M and sol; ++j) {
				if (lawn[i][j] < maxrows[i] and lawn[i][j] < maxcols[j]) sol = false;
			}
		}
		cout << "Case #" << t << ": " ;
		if (sol) cout << "YES" << endl;
		else cout << "NO" << endl;
		
		/*for (int i = 0; i < N; ++i) cout << maxrows[i] << " ";
		cout << endl;
		for (int j = 0; j < M; ++j) cout << maxcols[j] << " ";
		cout << endl;*/
		t++;
	}
    return 0;
}

