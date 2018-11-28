#include "stdafx.h"
#include <iostream>
#include <cstdio>
#include <string>
#include <sstream>
using namespace std;
int main(int argc, char** argv){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tt;
	scanf(" %d", &tt);
	for (int qq = 1; qq <= tt; qq++){
		string ss;
		cin >> ss;
		stringstream res;
		string st;
		st.push_back(ss[0]);
		res << st;
		for (int i = 1; i < ss.length(); i++){
			st = res.str();
			if (ss[i] >= st[0]){
				stringstream t;
				t = stringstream();
				st = "";
				st.push_back(ss[i]);
				t << st;
				st = res.str();
				t << st;
				res = stringstream();
				res << t.str();
			}
			else {
				st = "";
				st.push_back(ss[i]);
				res << st;
			}
		}
		string sres = res.str();
		printf("Case #%d: ", qq);
		cout << sres << endl;
	}
}