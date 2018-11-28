#include <cstdio>
#include <queue>
#include <iostream>
using namespace std;
string s;
deque<char> ans;

void findAns(){
	cin >> s;
	int l=s.length();
	ans.resize(0);
	ans.push_back(s[0]);
	for(int i=1;i<l;++i){
		if(s[i]>=ans.front())
			ans.push_front(s[i]);
		else
			ans.push_back(s[i]);
	}
}

int main(){
	int t;
	cin >> t;
	for(int i=1;i<=t;++i){
		findAns();
		cout << "Case #" << i << ": ";
		for (deque<char>::iterator it = ans.begin(); it != ans.end(); ++it)
			cout << *it;
		cout << endl;
	}
}

/*
7
CAB
JAM
CODE
ABAAB
CABCBBABC
ABCABCABC
ZXCASDQWE
*/