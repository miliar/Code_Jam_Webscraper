#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <string>
#include <cmath>
#include <functional>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>

using namespace std;

bool a[25][25];

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	ifstream inf("A-large.in");
	ofstream outf("output.txt");
	int t, q = 1;
	inf >> t;
	while (t--){
		int r, c, w;
		int ans = 0;
		inf >> r >> c >> w;
		for (int i = 1; i <= r; ++i)
		for (int j = 1; j <= c; ++j)
			a[i][j] = false;
		for (int i = 1; i <= r; ++i)
		for (int j = w; j <= c; j += w)
			a[i][j] = true, ++ans;
		ans += w - 1;
		if (!a[r][c]) ++ans;
		outf << "Case #" << q++ << ": " <<  ans << endl;
	}
	inf.close();
	outf.close();
	return 0;
}
