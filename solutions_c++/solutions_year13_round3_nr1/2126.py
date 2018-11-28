// test1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// test1.cpp : Defines the entry point for the console application.
//


#include <iostream>
#include <iterator>
#include <string>
#include <map>
#include <vector>
#include <sstream>
#include <algorithm>
#include <climits>
#include <fstream>
#include <set>
#include <math.h>

using namespace std; 

class solution {
public:
	void parse_testcase(){
		string line;
		cin >> s >> n;
		getline(cin, line);
	}

	bool is_vow(char a){
		if(a == 'a') return true;
		if(a == 'e') return true;
		if(a == 'i') return  true;
		if(a == 'o') return true;
		if(a == 'u') return true;
		return false;
	}

	long long solve(){
		int last_en = -1;
		int last_vow = -1, end = 0;
		long long count = 0;
		int ssize = s.size();
		s.push_back('a');
		for(int i = 0; i <= ssize; ++i){
			if(!is_vow(s[i])){
				continue;
			}
			if(i - last_vow - 1 < n) {
				last_vow = i;
				continue;
			}
			count += (last_vow - last_en + 1) * (ssize - last_vow - n);
			for(int j = last_vow + n + 2; j <= i; ++j)
				count += ssize - j + 1;
			last_en = i - n;
			last_vow = i;
		}
		return count;

	}
private:
	string s;
	int    n;
};

class em{
public:
	void parse_testcases(){
		string line;
		getline(cin, line);
		stringstream sline(line);
		sline >> _count;
		for(int i = 0; i < _count; ++i){
			solution tc;
			tc.parse_testcase();
			_tcs.push_back(tc);
		}	
	}
	void solve(){
		int i = 0;
		for(i = 0; i < _count; ++i){
			cout <<"Case #" << i + 1 <<": " << _tcs[i].solve() << endl;
		}
	}

private:
	vector<solution> _tcs;
	int _count;
};

int _tmain(int argc, char* argv[])
{
	em o;

	o.parse_testcases();
	o.solve();
	return 0;
}



