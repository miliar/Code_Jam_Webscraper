#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <limits.h>
#include <math.h>
#include <time.h>
#include <iostream>
#include <functional>
#include <numeric>
#include <algorithm>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <map>
#include <set>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;
const lint inf = 1e16;

string s = "RPS";

string make(int n, int p){
	if(n == 1) return s.substr(p, 1);
	vector<string> v;
	for(int i=0; i<3; i++){
		if(i != p) v.push_back(make(n/2, i));
	}
	return min(v[0] + v[1], v[1] + v[0]);
}

int main(){
	sort(s.begin(), s.end());
	int t;
	cin >> t;
	for(int i=1; i<=t; i++){
		printf("Case #%d: ", i);
		int n, r, p, s;
		cin >> n >> r >> p >> s;
		vector<string> ret;
		for(int i=0; i<3; i++){
			ret.push_back(make(1<<n, i));
		}
		sort(ret.begin(), ret.end());
		string prnt = "IMPOSSIBLE";
		for(auto &i : ret){
			if(count(i.begin(), i.end(), 'R') == r && count(i.begin(), i.end(), 'P') == p && count(i.begin(), i.end(), 'S') == s){
				prnt = i;
				break;
			}
		}
		cout << prnt << endl;
	}
}