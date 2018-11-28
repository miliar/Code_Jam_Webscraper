#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {
	freopen("out.txt", "w", stdout);
	freopen("in.txt", "r", stdin);
	int tc, t = 1;
	cin >> tc;
	while (tc--){
		int n, x = 4, y, index = -1;
		int a[20] = { 0 };
		bool ok = 0;
		cin >> n;
		for (int i = 1; i <= 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> y;
				if (i == n)a[y]++;
			}
		}
		cin >> n;
		for (int i = 1; i <= 4; i++){
			for (int j = 0; j < 4; j++){
				cin >> y;
				if (i == n)a[y]++;
			}
		}
		for (size_t i = 0; i < 20; i++){
			if (!ok && a[i] > 1)index = i, ok=1;
			else if (ok == 1 && a[i] > 1){
				ok = 0;
				break;
			}
		}
		cout << "Case #" << t++ << ": ";
		if (ok == 0 && index != -1)cout << "Bad magician!\n";
		else if (index == -1)cout << "Volunteer cheated!\n";
		else cout << index << endl;
	}

}

