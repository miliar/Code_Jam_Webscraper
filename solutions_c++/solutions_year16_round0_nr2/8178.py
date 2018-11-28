#include <vector>
#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void strip(string &s){
	int i = 0;
	for(i = s.length()-1; i>=0; i--){
		if(s[i] == '-')
			break;
	}
	s = s.substr(0, i+1);
}
int getPSeq(const string& s, int start){
	while(start < s.length() && s[start] == '+'){
		start++;
	}
	return start;
}
int solve(string s){
	strip(s);
	if(s.length() == 0)
		return 0;
	int cnt = 0;
	int startP = 0;
	int endP = 0;
	for(int i = 0 ; i < s.length(); ++i){
		bool found = false;
		if(s[i] == '+'){
			found = true;
			startP = i;
			endP = getPSeq(s, i);
		}
		if(found){
			if(startP == 0){
				cnt ++;
			} else{
				cnt += 2;
			}
			i = endP-1;
		}
	}
	return cnt+1;
}

int main(){

	int T;
	cin >> T;
	cin.ignore();
	for(int i =0; i < T; ++i){
		string s;
		getline(cin, s);
		printf("Case #%d: %d\n",i+1, solve(s));
	}
}