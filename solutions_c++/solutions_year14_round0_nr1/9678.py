#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string>
#include <stack>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>

using namespace std;
typedef long long LL;


int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	int m, n, T,c,a[4][4], b[4][4];
	cin >> T;
	
	for (c = 1; c <= T; ++ c) {
		cin >> m;
		set<int> v;
		for (int i = 0; i < 4; ++ i) {
			for (int j = 0; j < 4; ++ j) {
				cin >> a[i][j];	
				if (i == m - 1)
					v.insert(a[i][j]);
			}
		}
		cin >> n;
		for (int i = 0; i < 4; ++ i) {
			for (int j = 0; j < 4; ++ j)
				cin >> b[i][j];	
		}
		int cnt = 0, ans;
		for (int j = 0; j < 4; ++ j) {
			if (v.find(b[n - 1][j]) != v.end()) {
				++ cnt;
				ans = b[n - 1][j];
			}
		}	
		cout << "Case #" << c << ": ";
		if (cnt == 1)
			cout << ans << endl;
		else if (cnt == 0)
			cout << "Volunteer cheated!" << endl;
		else
			cout << "Bad magician!" << endl;
		
	}
	
	//system("pause");
	return 0;	
}
