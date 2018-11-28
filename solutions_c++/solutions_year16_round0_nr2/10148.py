//pancakes
//irvin gonzalez

#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

void solve() {
	string cakes;
	cin >> cakes;
	
	int ret = 0; 
	while(cakes.find("-") != string::npos) {
		if(cakes[0] == '+') {
			int i = 0;
			while(cakes[i] == '+') {
				++i; }
			string flip = cakes.substr(0, i);
			string rest = cakes.substr(i,cakes.size()); 
			reverse(flip.begin(), flip.end());
			for(int a = 0; a < flip.size(); ++a) {
				if(flip[a] == '-') flip[a] = '+';
				else flip[a] = '-'; }
			cakes = flip + rest; }
		else {
			int last = cakes.size() - 1;
			while(cakes[last] != '-') {
				--last; }
			string flip = cakes.substr(0, last+1);
			string rest = cakes.substr(last+1,cakes.size());
			reverse(flip.begin(), flip.end());
			for(int a = 0; a < flip.size(); ++a) {
				if(flip[a] == '-') flip[a] = '+';
				else flip[a] = '-'; }
			cakes = flip + rest; } 
	++ret;}
	cout << ret; }

				
			
int main() {
	int T;
	cin >> T;
	for( int i = 1; i <= T; ++i) {
		cout << "Case #" << i << ": ";
		solve();
		cout << endl; }

}
