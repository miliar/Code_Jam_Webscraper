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

vector<int>ve;
int al[30];

string wo[10] = {"ZERO","ONE", "TWO", "THREE", "FOUR", "FIVE",
					"SIX", "SEVEN", "EIGHT", "NINE"};
int tot[10][30] = {};
int add[10];

int search(){
	int ok = 0;
	for(int i = 0; i < 30; ++i) if(al[i]) {ok = 1; break;}
	if(!ok) {
		for(int i = 0; i < 10; ++i) 
			for(int j = 0; j < add[i]; ++j)
				ve.pb(i);
		return 1;
	}
	for(int i = 0; i < 10; ++i){
		int fl = 0;
		for(int j = 0; j < 30; ++j) if(al[j] < tot[i][j]) {fl = 1; break;}
		if(fl)continue;
		for(int j = 0; j < 30; ++j) al[j] -= tot[i][j];
		add[i]++;
		if(search())return 1;
		for(int j = 0; j < 30; ++j) al[j] += tot[i][j];
		add[i]--;
	}
	return 0;
}


int main () {
	for(int i = 0; i <= 9; ++i){
		for(int j = 0; j < wo[i].length(); ++j)
			tot[i][wo[i][j]-'A']++;
	}
	int n;
	cin >> n;
	string s;
	for(int tt = 1; tt <= n; ++tt){
		memset(add, 0, sizeof(add));
		ve.clear();
		memset(al, 0, sizeof(al));
		cin >> s;
		int ze = 0, ei = 0, six = 0, two = 0;
		for(int i = 0; i < s.length(); ++i){
			al[s[i]-'A']++;
			if(s[i] == 'Z') { ze++; ve.pb(0);}
			if(s[i] == 'G') { ei++; ve.pb(8); }
			if(s[i] == 'X') {six++; ve.pb(6);}
			if(s[i] == 'W') {two++; ve.pb(2);}
		}
		for(int i : ve){
			for(int j = 0; j < 30; ++j) 
				al[j] -= tot[i][j];
		}
		search();
		sort(ve.begin(), ve.end());
		printf("Case #%d: ", tt);
		for(int i = 0; i < ve.size(); ++i){
			cout << ve[i] ;
		}
		puts("");
	}	
}