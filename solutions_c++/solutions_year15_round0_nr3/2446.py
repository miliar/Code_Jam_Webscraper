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

#define all(c)  (c).begin(),(c).end()
#define rep(var,n)  for(int var=0;var<(n);var++)

//#include "cout11.h"

/*
0	0 1 2 3
1	1 4 3 6
2	2 7 4 1
3	3 2 5 4
*/
int xy[8][8] = {
	{0,1,2,3,4,5,6,7},
	{1,4,3,6,5,0,7,2},
	{2,7,4,1,6,3,0,5},
	{3,2,5,4,7,6,1,0},
	{4,5,6,7,0,1,2,3},
	{5,0,7,2,1,4,3,6},
	{6,3,0,5,2,7,4,1},
	{7,6,1,0,3,2,5,4},
	};

int main()
{
  map<char,int> mp;
  mp['1'] = 0;
  mp['i'] = 1;
  mp['j'] = 2;
  mp['k'] = 3;
  int _T; cin >> _T; // 1-100
  for (int _t=1; _t<=_T; ++_t) {
    int L, X; cin >> L >> X;
    string s1; cin >> s1;  // assert s1.length == L
    stringstream ss;
    rep(i, X) ss << s1;
    string s = ss.str();
    int M = L * X;
    // vector<int> c(M);
    // rep(i,M) c[i] = mp[s[i]];
    vector<int> d(M+1); d[0] = 0;
    bool fi = false, fij = false;
    for(int i=1; i<=M; ++i) {
    	d[i] = xy[ d[i-1] ][ mp[s[i-1]] ];
    	if (!fi) {
    		if (d[i] == 1) fi = true;
    	} else if (!fij) {
    		if (d[i] == 3) fij = true;
    	}
    }
    // cout << d << endl;
    bool ans = (fij && d[M]==4);
 answer:
    cout << "Case #" << _t << ": ";
    cout << (ans ? "YES" : "NO") << endl;
  }
}
