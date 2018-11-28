#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <list>
#include <cstdio>
#include "stdlib.h"
using namespace std;
typedef int my_t;
typedef list<my_t> flows_t;
struct PART {
	char c;
	int num;
};
void init(PART& temp) {
  temp.c = '\0';
  temp.num = 0;
}
  
vector<PART> simplify(string s, vector<int>& mins, vector<int>& maxs) {
	vector<PART> v;
	PART temp;
	init(temp);
	for (unsigned int i=0; i < s.length(); ++i) {
//		cout << "Test " << i << ' ' << temp.c << ' ' << temp.num << endl;
		if (s[i] != temp.c) {
			if (i != 0) { 
//				cout << "MCHK " << temp.c << ' ' << v.size() << ' ' << mins[v.size()] << ' ' << maxs[v.size()] << endl; 
				if (temp.num < mins[v.size()]) { mins[v.size()] = temp.num; }
				if (temp.num > maxs[v.size()]) { maxs[v.size()] = temp.num; }
				v.push_back(temp);
				init(temp);
			}
			temp.c = s[i];
		} 
		temp.num++;
	}
				if (temp.num < mins[v.size()]) { mins[v.size()] = temp.num; }
				if (temp.num > maxs[v.size()]) { maxs[v.size()] = temp.num; }
	v.push_back(temp);
//	cout << "Vec" << v.size() << endl;
	return v;
}
void fail () {
	cout << "Fegla Won" << endl;
}
void compute(int N) {
    vector <int> mins (1000,1000);
	vector <int> maxs (1000, 0);
    vector< vector<PART> > lines;
	for (int i=0; i < N; ++i) {
		string s;
		cin >> s;
		lines.push_back(simplify(s, mins, maxs));	
//		cout << "FOO " << lines.size() << ' ' << lines[0].size() << ' ' << lines[lines.size()-1].size() << endl;
	}
	int tokens = lines[0].size();
//	cout << endl << tokens << endl;
    for (int i=1; i < lines.size(); ++i) {
		if (tokens != lines[i].size()) {
			fail(); return;
		}
		for (int j=0; j < tokens; ++j) {
			if (lines[0][j].c != lines[i][j].c) {
				fail(); return;
			}
		}
	}
	int diffs = 0;
	for (int i =0; i < tokens; ++i) {
		diffs += (maxs[i]-mins[i]) ;
	}
		cout << diffs << endl;
}
void do_something(int testnum) {
	int N;  // num strings
//	vector<string> s_vec;
    cin >> N;
	compute(N);

}

int main(int argc, char **argv)
{
	int tests;
	cin >> tests;

	for (int i=1; i <= tests; ++i) {
	  cout << "Case #" << i << ": ";
	  do_something(i);
	}
	return 0;
}
