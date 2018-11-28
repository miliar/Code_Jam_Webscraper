#include<iostream>
#include<sstream>
#include<string>
#include<array>
#include<vector> // vector
#include<map>
#include<utility> //pair
#include<queue> // priority_queue
#include<algorithm>

#include<cstdio>
#include<cmath>
#include<cstring>
#include<functional> // greater

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t; cin >> t;
	for (int i = 1; i <= t; ++i){
		int n;
		string s;
		cin >> n >> s;
		int clappers = 0;
		int ans = 0;
		for (int j = 0; j < s.size(); ++j){
			clappers += (s[j] - '0');
			// 이 상태에서 clappers가 j+1 이상이 되어야 다음으로 넘어갈수 있다
			if (j < s.size() - 1 && clappers <= j){
				int friends = j + 1 - clappers;
				ans += friends;
				clappers = j + 1;
			}
		}
		cout << "Case #" << i << ": "<< ans <<"\n";
	}
	return 0;
}