#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
#include <string>
#include <queue>
#include <stack>
using namespace std;

#define S second
#define F first
#define mp make_pair
typedef pair<int, int> PII;
#define pb push_back
typedef long long ll;

string cc, jj;

string vc(int x, int y){
	string res = "";
	for(int i = x; i <= y; ++i) res += cc[i];
	return res;
}

string vj(int x, int y){
	string res = "";
	for(int i = x; i <= y; ++i) res += jj[i];
	return res;
}

string cal(int x, int len){
	string s = "";
	int cnt = 0;
	while(x){
		s = char((x%10)+'0') + s;
		cnt++;
		x/=10;
	}
	while(len > cnt++){
		s = '0' + s;
	}
	return s;
}

int main () {
	int n;
	cin >> n;
	for(int tt = 1; tt <= n; ++tt){
		cin >> cc >> jj;
		int up = 1;
		string ansx, ansy;
		int di = 10000;
		for(int i = 0; i < cc.length(); ++i) up *= 10;
		for(int i = 0; i < up; ++i){
			for(int j = 0; j < up; ++j){
				string a = cal(i, cc.length());
				string b = cal(j, cc.length());
				//cout << a << ' ' << b <<endl;
				int ok = 0;
				for(int k = 0; k < cc.length(); ++k) if(cc[k]!='?'){
					if(cc[k] != a[k]) {ok = 1; break;}
				}
				for(int k = 0; k < cc.length(); ++k) if(jj[k] !='?'){
					if(jj[k] != b[k]) {ok = 1; break;}
				}
				if(ok) continue;
				if(abs(i-j) < di){
					di = abs(i-j);
					ansx = a, ansy = b;
				}
			}
		}
		printf("Case #%d: ", tt);
		cout << ansx << ' ' << ansy <<endl;
	}	
}