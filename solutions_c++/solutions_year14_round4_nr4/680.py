#include<iostream>
#include<algorithm>
#include<string>
#include<set>
#include<map>
#include<vector>
using namespace std;

map<int, int> ans;
vector<string> cnt[108];
string str[108];
int m, n;
void check(){
	set<string> s;
	int p = 0;
	for(int i = 0;i < n;i++){
		if(cnt[i].empty())return;
		s.clear();
		for(int j = 0;j < cnt[i].size();j++){
			string tmp = "";
			for(int k = 0;k < cnt[i][j].size();k++){
				tmp += cnt[i][j][k];
				s.insert(tmp);
			}
		}
		p += s.size();
	}
	ans[p + n]++;
}

void dfs(int x){
	if(x == m)check();
	else{
		for(int i = 0;i < n;i++){
			cnt[i].push_back(str[x]);
			dfs(x + 1);
			cnt[i].pop_back();
		}
	}
}

void solve(int t){
	cin >> m >> n;
	ans.clear();
	for(int i = 0;i < m;i++){
		cin >> str[i];
	}	
	dfs(0);
	map<int, int>::iterator it = ans.end();
	it--;
	cout << "case #" << t << ": " << it->first << " " << it->second << endl;
}

int main(){
	int t;
	cin >> t;
	for(int i = 1;i <= t;i++){
		solve(i);
	}
	return 0;
}