#include<iostream>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<deque>
#include<unordered_set>
#include<unordered_map>
#include<string>
#include<string.h>
#include<cmath>
#include<algorithm>
#include<utility>
#include<fstream>
#include<unordered_map>
using namespace std;
string mapping[256];
void build(int depth, char val, string& builder, int n){
	if(depth == n - 1){
		builder += mapping[val];
		return;
	}
	string next = mapping[val];
	build(depth + 1, next[0], builder, n);
	build(depth + 1, next[1], builder, n);
}
bool can(const string& str, int p, int r, int s){
	for(int i = 0; i < str.size(); ++ i){
		if(str[i] == 'P')
			p --;
		else if(str[i] == 'R')
			r --;
		else s --;
	}
	if(p != 0 || r != 0 || s != 0)
		return false;
	return true;
}
void sortIt(string& s, int len){
	if(len >= s.size())
		return;
	string builder;
	for(int i = 0; i < s.size() - len*2 + 1; i += len*2){
		string first = s.substr(i, len), second = s.substr(i + len, len);
		//cout << len << ' ' << first << ' ' << second << endl;	
		if(first <= second){
			builder += first;
			builder += second;
		}
		else{
			builder += second;
			builder += first;
		}
	}
	if(builder.size() == 0)
		return;
	s = builder;
	sortIt(s, len*2);
}
int main(){
	mapping['R'] = "RS";
	mapping['P'] = "PR";
	mapping['S'] = "PS";
	int t, n, r, p, s;
	cin >> t;
	char arr[3] = {'P', 'R', 'S'};
	for(int z = 1; z <= t; ++ z){
		cin >> n >> r >> p >> s;
		cout << "Case #" << z << ": ";
		vector<string> v;
		for(int i = 0; i < 3; ++ i){
			string builder;
			build(0, arr[i], builder, n);
			sortIt(builder, 2);
			v.push_back(builder);
			//cout << builder << endl;
		}
		sort(v.begin(), v.end());
		string ret = "IMPOSSIBLE";
		for(int i = 0; i < v.size(); ++ i){
			if(can(v[i], p,r,s)){
				ret = v[i];
				break;
			}
		}
		cout << ret << endl;
	}
	return 0;
}