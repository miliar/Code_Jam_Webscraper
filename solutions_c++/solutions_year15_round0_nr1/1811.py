#include <iostream>
#include <vector>
#include <cstdio>
#include <sstream>
#include <map>
#include <string>
#include <algorithm>
#include <queue>
#include <cmath>
#include <set>
using namespace std;

long long solve(){
	long long S_max;
	cin >> S_max;
	string s;
	cin >> s;
	vector<int> v(s.size());
	for(int i=0; i<s.size(); i++){
		v[i] = s[i] - '0';
	}

	long long ans = 0;
	long long cnt = 0;
	for(int i=0; i<s.size(); i++){
		if(v[i] == 0) continue;
		if(i > cnt){
			ans += i-cnt;
			cnt = i;
		}
		cnt += v[i];
	}

	return ans;
}

int main(){
	int T;
	cin >> T;
	for(int t=1; t<=T; t++){
		cout << "Case #" << t << ": " << solve() << endl;
	}
	return 0;
}