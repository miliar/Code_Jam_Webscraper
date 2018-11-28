#include <iostream>
#include <vector>

using namespace std;

inline bool checkHorizontal(int x, int y, vector<vector<int> >& lawn)
{
	for (int cy = y - 1; 0 <= cy; --cy) {
		if (!(lawn[x][cy] <= lawn[x][y]))
			return false;
	}
	for (int cy = y + 1, yMax = lawn[x].size() - 1; cy <= yMax; ++cy) {
		if (!(lawn[x][cy] <= lawn[x][y]))
			return false;
	}
	return true;
}

inline bool checkVertical(int x, int y, vector<vector<int> >& lawn)
{
	for (int cx = x - 1; 0 <= cx; --cx) {
		if (!(lawn[cx][y] <= lawn[x][y]))
			return false;
	}
	for (int cx = x + 1, xMax = lawn.size() - 1; cx <= xMax; ++cx) {
		if (!(lawn[cx][y] <= lawn[x][y]))
			return false;
	}
	return true;

}

inline bool solve(vector<vector<int> >& lawn)
{
	for (int i = 0; i < lawn.size(); ++i) {
	for (int j = 0; j < lawn[i].size(); ++j) {
		if (!(checkHorizontal(i, j, lawn) || checkVertical(i, j, lawn)))
			return false;
	}
	}
	return true;
}

int main()
{
	int T = 0;
	cin>>T;
	for (int i = 0; i < T; ++i) {
		int N = 0, M = 0;
		cin>>N>>M;
		vector<vector<int> > lawn(N, vector<int>(M, 0));
		for (int j = 0; j < N; ++j) {
		for (int k = 0; k < M; ++k) {
			cin>>lawn[j][k];
		}
		}
		const bool res = solve(lawn);
		cout<<"Case #"<<(i + 1)<<": "<<(res ? "YES" : "NO")<<endl;
	}
	return 0;
}
