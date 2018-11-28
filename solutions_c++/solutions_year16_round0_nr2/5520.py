#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <map>
#include <queue>
using namespace std;

int main() {
	int t;
	cin >> t;
	for(int tt=1;tt<=t;tt++) {
		map<string, int> f;
		string s;
		cin >> s;
		int n = s.size();
		queue<string> q;
		q.push(s);
		f[s] = 0;
		while(!q.empty()) {
			string cur = q.front();q.pop();
			for(int i=0;i<n;i++) {
				string tmp;
				for(int j=0;j<=i;j++) {
					if(cur[j] == '+')tmp.push_back('-');
					else tmp.push_back('+');
				}
				reverse(tmp.begin(), tmp.end());
				for(int j=i+1;j<n;j++) {
					tmp.push_back(cur[j]);
				}
				//cout << tmp << " ";
				if(f.find(tmp) == f.end())
						f[tmp] = f[cur] + 1, q.push(tmp);
			}
		}
		string res;
		for(int i=0;i<n;i++)res.push_back('+');
		cout << "Case #" << tt << ": " << f[res] << "\n";
	
	}
	return 0;
}