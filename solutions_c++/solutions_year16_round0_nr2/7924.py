#include <iostream>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define f(x, y) for(int x = 0; x < y; ++x)

void solve(string s);

int main(){
	unsigned int T;
	string S;

	cin >> T;

	f(x, T){
		cin >> S;
		cout << "Case #" << (x + 1) << ": ";
		solve(S);
	}

	return 0;
}

void solve(string s){
	vector<int> p;
	f(x, s.size()){
		p.push_back(s[x] == '-' ? 0 : 1);
	}
	
	vector<int>::iterator it = unique(p.begin(), p.end());
	p.resize(distance(p.begin(), it));
	cout << (p.size() - p.back()) << endl;
}
