#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <string>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <ctime>
#include <cassert>
#include <set>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <queue>

using namespace std;

typedef long long ll;

int t;
int s;
string nums;
vector<int> src;

int main()
{
	freopen("input", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for(int i = 0; i < t; i++) {
		cin >> s;
		src.clear();
		src.resize(s + 1, 0);
		cin >> nums;
		//cerr << nums << endl;
		for(int j = 0; j < (int)nums.size(); j++) {
			src[j] = nums[j] - '0';
		}
		int res = 0;
		int sum = 0;
		for(int j = 0; j <= s; j++) {
			//cerr << sum << " " << res << " " << j << endl;
			if(sum < j) {
				res += (j - sum);
				sum = j;
			}
			sum += src[j];
		}
		cout << "Case #" << (i + 1) << ": " << res << endl;
	}
	return 0;
}
