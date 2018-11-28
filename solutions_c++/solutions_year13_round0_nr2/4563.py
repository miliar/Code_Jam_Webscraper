#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <string.h>
using namespace std;

int lawn[101][101], N, M;
bool verify(int r, int c)
{
	bool rs = false, cs = false;
	for (int i = 0; i < M; ++i)
		if (lawn[r][i] > lawn[r][c]) {
			rs = true;
			break;
		}
	for (int i = 0; i < N; ++i)
		if (lawn[i][c] > lawn[r][c]) {
			cs = true;
			break;
		}
	if (rs && cs) return false;
	return true;
}
main(int argc, char *argv[])
{
	int tc;
	ifstream myfile;
	myfile.open(argv[1]);
	myfile >> tc;
	for (int i = 1; i <= tc; ++i) {
		string ans = "YES";
		myfile >> N >> M;
		for (int l1 = 0; l1 < N; ++l1)
			for (int l2 = 0; l2 < M; ++l2)
				myfile >> lawn[l1][l2];
		for (int l1 = 0; l1 < N; ++l1)
			for (int l2 = 0; l2 < M; ++l2)
				if (!verify(l1, l2)) {
					ans = "NO";
					goto print_ans;
				}
print_ans:
		cout << "Case #" << i << ": " << ans << "\n";
	}
}
