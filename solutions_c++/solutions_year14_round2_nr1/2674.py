#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;

ifstream in;
ofstream out;

int main() {
	in.open("A-small-attempt2.in");
	out.open("out.txt");
	int T;
	in >> T;
	for(int t=1; t<=T; t++) {
		int N;
		in >> N;
		vector <char> a[N];
		vector <int> _a[N];
		string s;
		for(int i=0; i<N; i++) {
			in >> s;
			a[i].push_back(s[0]);
			_a[i].push_back(1);
			for(int j=1; j<s.length(); j++) {
				if(s[j] == s[j-1]) {
					_a[i][_a[i].size()-1] ++;
				}
				else {
					a[i].push_back(s[j]);
					_a[i].push_back(1);
				}
			}
		}
		
		out << "Case #" << t << ": ";
		bool content_check = 1;
		for(int i=0; i<N-1; i++) if(a[i].size() != a[i+1].size()) { content_check = 0; break; }
		if(content_check) {
			for(int i=0; i<a[0].size(); i++) {
				for(int j=0; j<N-1; j++) if(a[j][i] != a[j+1][i]) { content_check = 0; break; }
				if(content_check == 0) break;
			}
		}
		
		if(content_check == 1) {
			int sum = 0;
			for(int i=0; i<a[0].size(); i++) {
				int calc = 0;
				for(int j=0; j<N; j++) calc += _a[j][i];
				calc /= N;
				for(int j=0; j<N; j++) if(_a[j][i] != calc) sum += abs(_a[j][i] - calc);
			}
			out << sum << endl;
		}
		else out << "Fegla Won" << endl;
	}
}
