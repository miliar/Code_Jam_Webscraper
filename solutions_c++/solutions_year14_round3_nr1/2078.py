#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>

#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

using namespace std;

long long gcd(long long a, long long b){
	if(b == 0) return a;
	return gcd(b, a%b);
}

long long parse(string v){
	long long ret = 0;
	for(int i = 0; i < v.length(); i++){
		ret = ret*10 + v[i]-'0';
	}
	return ret;
}

int main(){
	int t, count = 1, ret;
	long long p, q, g;
	string s;
	
	cin >> t;
	while(t--){
		cin >> s;
		int bar = 0;
		for(int i = 0; i < s.length(); i++){
			if(s[i] == '/') {
				bar = i;
				break;
			}
		}
		
		p = parse(s.substr(0, bar));
		q = parse(s.substr(bar+1));
		
		ret = 0;

		g = gcd(max(p,q), min(p,q));
		p /= g; q /= g;
		
		int i;
		for(i = q; i%2 == 0; i /= 2);
		if(i != 1) ret = -1;
		else{
			ret = 0;
			do {
				q /= 2;
				ret++;
			} while(p < q);
		}
		
		cout << "Case #" << count++ << ": ";
		if(ret > 0) cout << ret << endl;
		else cout << "impossible" << endl;
	}
	
	return 0;
}

