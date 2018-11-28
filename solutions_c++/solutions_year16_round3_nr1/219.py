#include <iostream>
#include <vector>
#include <string>

using namespace std;

char g(vector <int> &v) {
	int i = 0;
	for(int j=1; j<v.size(); j++)
		if(v[j] > v[i])
			i = j;
	if(v[i] == 0) return 0;
	else {
		v[i]--;
		return 'A' + i;
	}
}

void f(vector <int> &v, vector <string> &ans) { 
	char ch1 = g(v);
	char ch2 = g(v);
	if(ch1 != 0) {
		string s = "";
		s += ch1;
		if(ch2 != 0) s += ch2;
		ans.push_back(s);
		if(ch2 != 0) f(v, ans);
	}
}

int main() {
	int T;
	cin >> T;
	for(int caso=1; caso<=T; caso++) {
		int n;
		cin >> n;
		vector <int> v(n);
		for(int i=0; i<n; i++) {
			cin >> v[i];
		}
		vector <string> x;
		f(v, x);
		cout << "Case #" << caso << ":";
		int sz = x.size();
		if(sz >= 2 && x[sz-1].size() == 1) {
			swap(x[sz-1], x[sz-2]);
		}
		for(int i=0; i<x.size(); i++)
			cout << " " << x[i];
		cout << endl;
	}
	return 0;
}