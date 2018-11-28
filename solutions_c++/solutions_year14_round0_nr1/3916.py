#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>
#include <iostream>

using namespace std;

#define INF (1<<29)
#define eprintf(...) fprintf(stderr,__VA_ARGS__)
#define TIMESTAMP(x) eprintf("["#x"] Time : %.3lf s.\n", clock()*1.0/CLOCKS_PER_SEC)

int main() {
	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t) {
		int a1, a2, a[4][4];
		set<int> all, ret;
		
		cin >> a1;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> a[i][j];
		for(int i = 0; i < 4; ++i)
			all.insert(a[a1-1][i]);
		
		cin >> a2;
		for(int i = 0; i < 4; ++i)
			for(int j = 0; j < 4; ++j)
				cin >> a[i][j];
		for(int i = 0; i < 4; ++i)
			if(all.find(a[a2-1][i]) != all.end())
				ret.insert(a[a2-1][i]);
		
		cout << "Case #" << t << ": ";
		if(ret.size() == 0)
			cout << "Volunteer cheated!";
		else if(ret.size() == 1)
			cout << *(ret.begin());
		else
			cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}
