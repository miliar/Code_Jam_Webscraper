#include <assert.h>
#include <cstring>
#include <iostream>
#include <fstream>
#include <climits>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
using namespace std;


int f[4][4];

int main() {
	int cases;
	cin >> cases;
	for (int t = 1; t <= cases; t++)
	{
		int a, b;
		cin >> a;
		a--;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++) 
			{
				cin >> f[i][j];
			}
		unordered_map<int, int> hash;
		for (int i = 0; i < 4; i++) hash[f[a][i]] = 1;

		cin >> b;
		b--;
		for (int i = 0; i < 4; i++) 
			for (int j = 0; j < 4; j++) 
			{
				cin >> f[i][j];
			}
		for (int i = 0; i < 4; i++) 
		{
			if (hash.count(f[b][i]) != 0) hash[f[b][i]]++;
			else hash[f[b][i]] = 1;
		}

		int count = 0;
		int result;

		for (auto x : hash)
		{
			if (x.second == 2) {
				count ++;
				result = x.first;
			}
		}

		cout << "Case #" << t << ": ";
		if (count == 0) cout << "Volunteer cheated!" << endl;
		else if (count > 1) cout << "Bad magician!" << endl;
		else cout << result << endl;
	}
	return 0;
}