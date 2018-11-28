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


string solve(string& s) {
	int l = s.size();
	string a;
	rep(i,l){
		if (a+s[i] > s[i]+a)
			a += s[i];
		else
			a = s[i] + a;
	}
	return a;
}

int main(){
  int _T; cin>>_T; // 1-100
  rep(_t,_T){
  	string S; cin >> S;
 answer:
    cout << "Case #" << (1+_t) << ": " << solve(S) << endl;
  }
}
