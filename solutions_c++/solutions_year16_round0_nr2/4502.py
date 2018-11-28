#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

void flip(string& s) {
	char prev = s[0];
	int i=1;
	char rep = prev == '+'? '-': '+';
	s[0] = rep;
	while(s[i] == prev) {
		s[i] = rep;
		i++;
	}
}

bool isOver(string& s) {
	bool done = true;
	for(int i=0;i<s.length();++i) {
		if(s[i] == '-' ) {
			done = false;
			break;
		}
	}
	return done;
}

int getCount(string& s) {
	int ans = 0;
	while(!isOver(s)) {
		ans++;
		flip(s);
	}
	return ans;
}

int main() {
	int t;
	cin >> t;
	for(int i=1; i<=t; ++i) {
		string s;
		cin>>s;
		cout<<"Case #"<<i<<": ";
		cout<<getCount(s)<<"\n";
	}

	return 0;
}
