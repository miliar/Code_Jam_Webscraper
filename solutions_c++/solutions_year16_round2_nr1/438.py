#include <iostream>
#include <sstream>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <algorithm>
#include <string>
#include <vector>
#include <deque>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>

using namespace std;
#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)
#define found(s,e)  ((s).find(e)!=(s).end())

// #include "cout.h"

string solve(string& s) {
	vector<int> st(256, 0);
	rep(i, s.size()) {
		++st[s[i]];
	}
	//cout << st << endl;
	vector<int> ct(10, 0);
	int zero = st['Z'];
	if (zero) {
		ct[0] = zero;
		st['Z'] -= zero; st['E'] -= zero; st['R'] -= zero; st['O'] -= zero;
	}
	int two = st['W'];
	if (two) {
		ct[2] = two;
		st['T'] -= two; st['W'] -= two; st['O'] -= two;
	}
	int four = st['U'];
	if (four) {
		ct[4] = four;
		st['F'] -= four; st['O'] -= four; st['U'] -= four; st['R'] -= four;
	}
	int six = st['X'];
	if (six) {
		ct[6] = six;
		st['S'] -= six; st['I'] -= six; st['X'] -= six;
	}
	int eight = st['G'];
	if (eight) {
		ct[8] = eight;
		st['E'] -= eight; st['I'] -= eight; st['G'] -= eight; st['H'] -= eight; st['T'] -= eight;
	}
	int three = st['R'];
	if (three) {
		ct[3] = three;
		st['T'] -= three; st['H'] -= three; st['R'] -= three; st['E'] -= three*2;
	}
	int seven = st['S'];
	if (seven) {
		ct[7] = seven;
		st['S'] -= seven; st['E'] -= seven*2; st['V'] -= seven; st['N'] -= seven;
	}
	int five = st['V'];
	if (five) {
		ct[5] = five;
		st['F'] -= five; st['I'] -= five; st['V'] -= five; st['E'] -= five;
	}
	int one = st['O'];
	if (one) {
		ct[1] = one;
		st['O'] -= one; st['N'] -= one; st['E'] -= one;
	}
	int nine = st['E'];
	if (nine) {
		ct[9] = nine;
		st['N'] -= nine; st['I'] -= nine; st['N'] -= nine; st['E'] -= nine;
	}
	// cout << ct << endl;
	// cout << vector<int>(st.begin()+'A', st.begin()+'Z') << endl;
	stringstream ss;
	rep(i,10) {
		if (ct[i]) {
			rep(j,ct[i]) ss << i;
		}
	}

	return ss.str();
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  	string s; cin >> s;
 answer:
    cout << "Case #" << (1+_t) << ": " << solve(s) << endl;
  }
}
