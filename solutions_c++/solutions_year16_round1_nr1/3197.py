#include <bits/stdc++.h>

using namespace std;
std::vector<char> pre, pos;

int main(){
	
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int test;

	scanf("%d\n", &test);
	string s, res;

	for (int i =1; i <= test; i++){
		res = "";
		getline(cin, s);
		pre.clear(); pos.clear();
		pre.push_back(s[0]);
		for (int j =1; j < s.length(); j++){
			if (s[j] >= pre[pre.size()-1]){
				pre.push_back(s[j]);
			} else {
				pos.push_back(s[j]);
			}
		}
		for (int j = pre.size() - 1; j >= 0; j--)
			res += pre[j];
		
		for (int j = 0; j < pos.size(); j++)
			res += pos[j];

		printf("Case #%d: %s\n", i, res.c_str());
	}
}