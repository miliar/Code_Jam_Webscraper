#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cmath>
#define MAXN 101000

using namespace std;

void solve()
{
	string s;
	cin >> s;
	vector<char> v;
	int result = 0;
	for (int i = 0; i < s.size(); ++i){
		int top = v.size();
		if (top > 0){
			--top;
			if(v[top] == s[i]){
				v.pop_back();
				result += 10;
				continue;
			}
		}
		v.push_back(s[i]);
	}
	result += v.size() / 2 * 5;
	cout << result << endl;
}


int main()
{
	ios::sync_with_stdio(false);
	int t;
	cin >> t;
	for(int i = 1; i <= t; ++i){
		cout << "Case #" << i << ": ";
		solve();
	}
	return 0;
}
