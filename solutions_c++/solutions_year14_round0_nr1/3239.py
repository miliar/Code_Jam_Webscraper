#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <cstring>
#define BIG 1000000000
#define LL long long
using namespace std;

int ntest;
int row1, row2;
set<int> set1, set2;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> ntest;
	for (int test = 1; test <= ntest; test++) {
		set1.clear();
		set2.clear();
		cin >> row1;
		row1--;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++) {
				int x;
				cin >> x;
				if (i == row1) set1.insert(x);
			}
		cin >> row2;
		row2--;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++) {
				int x;
				cin >> x;
				if (i == row2) set2.insert(x);
			}
		vector<int> ans;
		for (int i = 1; i <= 16; i++)
			if (set1.find(i) != set1.end() && set2.find(i) != set2.end())
				ans.push_back(i);
		cout << "Case #" << test << ": "; 
		if (ans.size() == 1)
			cout << ans[0] << endl;
		if (ans.size() == 0)
			cout << "Volunteer cheated!" << endl;
		if (ans.size() > 1)
			cout << "Bad magician!" << endl;
	}	
}

