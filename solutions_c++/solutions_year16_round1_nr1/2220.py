#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>
#include <string>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include<functional>
#include <fstream>
#define ii pair<int,int>
#define INF 1000000000
using namespace std;
int main()
{
	freopen("output.txt","w",stdout);
	int t, l;
	cin >> t;
	for (l = 0; l < t; l++) {
		string s,ans;
		cin >> s;
		ans += s[0];
		for (int i = 1; i < s.size(); i++) {
			if (s[i] < ans[0]) {
				ans += s[i];
			}
			else {
				string tmp = ans;
				ans.clear();
				ans += s[i];
				ans += tmp;
			}
		}
		cout <<"Case #"<<l+1<<": "<< ans << endl;
	}
	return 0;
}
