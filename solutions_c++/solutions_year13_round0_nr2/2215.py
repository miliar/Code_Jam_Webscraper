#include <functional>
#include <algorithm>
#include <iostream>
#include <memory.h>
#include <utility>
#include <numeric>
#include <iomanip>
#include <cstdlib>
#include <sstream>
#include <fstream>
#include <vector>
#include <bitset>
#include <cstdio>
#include <queue>
#include <cmath>
#include <stack>
#include <ctime>
#include <list>
#include <map>
#include <set>
using namespace std;
int a[101][101];
bool mi[101], mj[101];
bool ti[101], tj[101];
int main(){
	int T, n, m;
	cin >> T;
	for (int t = 0;t < T;++t){
		cin >> n >> m;
		for (int i = 0;i < n;++i)
			for (int j = 0;j < m;++j)
				cin >> a[i][j];
		bool ok = true;
		memset(mi, false, sizeof mi);
		memset(mj, false, sizeof mj);
		memset(ti, false, sizeof ti);
		memset(tj, false, sizeof tj);
		for (int k = 100;k > 0;--k){
			for (int i = 0;i < n;++i)
				for (int j = 0;j < m;++j)
					if (a[i][j] == k){
						if (!mi[i] || !mj[j]){
							ti[i] = true;
							tj[j] = true;
						} else {
							ok = false;
						}
					}
			for (int i = 0;i < 101;++i){
				mi[i] = ti[i];
				mj[i] = tj[i];
			}
		}
		cout << "Case #" << t + 1 << ": ";
		if (ok == false) cout << "NO" << endl;
		else cout << "YES" << endl;
	}
	return 0;
}