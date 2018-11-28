#include <iostream>
#include <cstdio>
#include <string>
#include <unordered_map>
#include <queue>
using namespace std;

bool check(const string& s) 
{
	for(int i = 0; i < (int)s.size(); ++i) {
		if(s[i] == '-') return false;
	}
	
	return true;
}

string compress(const string& s)
{
	string res;
	res += s[0];
	
	for(int i = 1; i < (int)s.size(); ++i) {
		if(s[i] != res.back()) {
			res += s[i];
		}
	}
	
	return res;
}

void problem()
{
	string s;
	cin >> s;
	
	s = compress(s);
	
	unordered_map<string, int> d;
	queue<string> que;
	d[s] = 0;
	que.push(s);
	
	
	while(!que.empty()) {
		auto cur = que.front(); que.pop();
		
		if(check(cur)) {
			cout << d[cur] << endl;
			return;
		}
		
		for(int i = 0; i < (int)cur.size(); ++i) {
			string t = cur;
			for(int j = 0; j <= i; ++j) {
				t[j] = (cur[i-j] == '+' ? '-' : '+');
			}
			
			t = compress(t);
			
			if(d.count(t)) continue;
			
			d[t] = d[cur] + 1;
			que.push(t);
		}
	}
}

int main() {
	
	int t;
	cin >> t;
	
	for(int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		problem();
	}
	
	return 0;
}