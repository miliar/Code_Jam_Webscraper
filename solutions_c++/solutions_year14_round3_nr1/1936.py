#include <iostream>
#include <cstdlib>
#include <fstream>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <math.h>
#include <stack>
#include <queue>
#include <list>
#include <limits.h>
#include <time.h>
#include <iterator>

#pragma comment(linker, "/STACK:167772160")

using namespace std;

map <pair<long long, long long>, int> mp;


int ans ;
bool good(long long n) {
	for(int i=0; i<50; i++)
		if((1LL << (i*1LL)) == n) return true;
	return false;
}
int f(long long a, long long b) {
//	auto p = make_pair(a, b);
//	if(mp[p]) return mp
	//auto k = gcd(a, b);
	//a /= k;
	//b /= k;
	int cnt = 0;
	while((!(b & 1)) && (b > a)) cnt++, b /= 2;
	if(a == b) return cnt;
	if(a > b && good(b)) return cnt;
	//if(a > b) return f(a-b, b);
	 return -1;

}
int main(){
	ifstream cin("A-small-attempt3.in");
	ofstream cout("ans.txt");
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		string s;
		long long a = 0, b = 0;
		cin >> s;
		int pp ;
		for(int i=0; s[i] != '/'; i++) {
			a = a * 10 + s[i] - '0';
			pp = i;
		}
		for(int i=pp+2; i<s.length(); i++)
			b = b * 10 + s[i] - '0';

		//cout << a << " " << b << endl;
		auto ans = f(a, b);
		cout << "Case #" << t << ": " ;
		if(ans == -1) cout << "impossible" << endl; else cout << ans << endl;
	}
	return 0;
}
  