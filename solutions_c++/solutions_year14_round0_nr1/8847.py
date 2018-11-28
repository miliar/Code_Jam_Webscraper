#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <stack>
#include <algorithm>
#include <cmath>
#include <queue>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <bitset>
#include <sstream>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios_base::sync_with_stdio(false);
	int test;
	cin >> test;
	for (int t = 0; t < test; ++t) {
		int first;
		cin >> first;
		--first;
		vector<int> count(16);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int x;
				cin >> x;
				--x;
				if (i == first)
					++count[x];
			}
		int second;
		cin >> second;
		--second;
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j) {
				int x;
				cin >> x;
				--x;
				if (i == second)
					++count[x];
			}
		vector<int> united;
		for (int i = 0; i < 16; ++i)
			if (count[i] == 2)
				united.push_back(i + 1);
		cout << "Case #" << t + 1 << ": ";
		if (united.size() == 1)
			cout << united.front();
		else
			if (united.empty())
				cout << "Volunteer cheated!";
			else
				cout << "Bad magician!";
		cout << endl;
	}
	return 0;
}