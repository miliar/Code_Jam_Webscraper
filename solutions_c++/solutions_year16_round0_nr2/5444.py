#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

using namespace std;

/*
int f(string str){
	if(m.count(str) == 1) return m[str];

	bool b = 1;
	for(int i = 0; i < len; i++) if(str[i] == '-') b = 0;

	if(b) return (m[str] = 0);

	int tren = 999999;

	for(int i = 1; i <= len; i++){
		string nov = str;

		reverse(nov.begin(), nov.begin() + i);
		for(int j = 0; j < i; j++){
			if(nov[j] == '+') nov[j] = '-';
			else nov[j] = '+';
		}
		tren = min(tren, f(nov));
	}

	m[str] = tren + 1;
	return (tren + 1);
}*/

vector<int> v;

int solve(string str){
	v.clear();
	int ans = 0;
	int len = str.length();
	if(str[0] == '+') v.push_back(1);
	else v.push_back(0);

	for(int i = 1; i < len; i++){ 	//vec zaporednih znakov je vseeno
		int tren = 1;
		if(str[i] == '-') tren = 0;
		if(tren != v.back()) v.push_back(tren);
	}
	if(v.back() == 1) v.pop_back();

	for(int i = 0; i < v.size(); i++){
		if(i == 0 && v[i] == 0) ans++;
		if(i > 0 && v[i] == 0) ans += 2;
	}
	return ans;
}

int main(){
	long long t;
	cin >> t;

	for(long long cnt = 1; cnt <= t; cnt++){
		cout << "Case #" << cnt << ": ";
		string str;
		cin >> str;
		cout << solve(str) << "\n";
	}
	return 0;
}