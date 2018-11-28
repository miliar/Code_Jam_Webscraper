#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#include <stdio.h>
#include <vector>
#include <string>
#include <memory.h>
using namespace std;
typedef long long ll;
string a, b;
ll best, oo = 1ll << 60;
string resA, resB;
string conv(int d,int dd){
	string s = "";
	while (dd--){
		s += (char)(d % 10 + '0');
		d /= 10;
	}
	reverse(s.begin(), s.end());
	return s;
}
bool ok(string a, int d){
	string s = conv(d, a.size());
	for (int i = 0; i < a.size(); ++i){
		if (a[i] != s[i] && a[i] != '?')
			return 0;
	}
	return 1;
}
void check(string I, string J){
	int diff = 0;
	for (int i = 0; i < I.size(); ++i)
		diff = diff * 10 + I[i] - J[i];
	if (diff < 0)diff = -diff;
	if (diff < best || (diff == best && (I < resA || (I == resA && J < resB)))){
		resA = I; resB = J;
		best = diff;
	}
}
void calc(int i, string x, string y){
	if (i == a.size() * 2){
		check(x, y);
		return;
	}
	if (i >= a.size()){
		int I = i - a.size();
		if (b[I] == '?'){
			for (char j = '0'; j <= '9'; ++j){
				calc(i + 1, x , y + j);
			}
		}
		else calc(i + 1, x , y + b[I]);
	}
	else{
		if (a[i] == '?'){
			for (char j = '0'; j <= '9'; ++j){
				calc(i + 1, x + j, y);
			}
		}
		else calc(i + 1, x + a[i], y);
	}
}
int main(){
	freopen("src.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; ++k){
		cin >> a >> b;
		best = oo;
		resA.clear(); resB.clear();
		
		printf("Case #%d:", k);
		calc(0, "", "");
		cout << " " << resA << " " << resB << endl;
	}
}

// "THREE", , "SEVEN", , "NINE"