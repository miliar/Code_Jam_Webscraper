#include <iostream>
#include <string>
#include <set>
#include <algorithm>
#include <queue>
using namespace std;

string goal;
int solve(const string sstr) {
	set<string> cache;
	queue< pair<string,int> > que;

	que.push(make_pair(sstr,0));
	cache.insert(sstr);
	while(!que.empty()) {
		pair<string,int> top = que.front();
		que.pop();
		string str = top.first;
		int ntry = top.second;
		if( str == goal ) return ntry;
	
		for(int i = 0 ; i < str.size() ; ++i ) {
			string str2 = str.substr(0,i+1);
			for(int j=0;j<str2.size();++j) str2[j] = str2[j] == '+' ? '-' : '+';
			reverse(str2.begin(),str2.end());
			string now = str2 + str.substr(i+1);
			if(cache.find(now)!=cache.end()) continue;
			cache.insert(now);
			que.push(make_pair(now,ntry+1));
		}	
	}
	return -1;
}

int main() {
	int ncase;
	cin >> ncase;
	for(int caseno=1;caseno<=ncase;++caseno) {
		string str;
		cin >> str;
		goal = "";
		for(int i=0;i<str.size();++i) goal += "+";
		cout << "Case #" << caseno << ": " << solve(str) << endl;
	}
}
