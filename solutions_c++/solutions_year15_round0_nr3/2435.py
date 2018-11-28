#include <bits/stdc++.h>
using namespace std; 

#define ALL(x) (x).begin(),(x).end() 

typedef long long ll;
const double eps = 1e-10;

int tab[][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};
int sgn[][4] = {
	{0, 0, 0, 0},
	{0, 1, 0, 1},
	{0, 1, 1, 0},
	{0, 0, 1, 1}
};

int L, X;
string s;
string solve(){
	map<char, int> mp;
	vector<int> f(L * X), fs(L * X), b(L * X), bs(L * X);
	if(L * X < 3) return "NO";
	string t = "";
	for(int i = 0; i < X; ++i)
		t = t + s;
	s = t;
	for(int i = 0; i < t.size(); ++i){
		s[i] -= 'h';
	}
	L = L * X;
	f[0] = s[0];
	for(int i = 1; i < t.size(); ++i){
		f[i] = tab[f[i-1]][s[i]];
		fs[i] = (fs[i-1] + sgn[f[i-1]][s[i]]) % 2;
	}
	b[L-1] = s[L-1];
	for(int i = L-2; i >= 0; --i){
		b[i] = tab[s[i]][b[i+1]];
		bs[i] = (bs[i+1] + sgn[s[i]][b[i+1]]) % 2;
	}
	for(int i = 0; i < L; ++i){
		if(f[i] != 1 || fs[i] != 0) continue;
		int x = 0, y = 0;
		for(int j = i+1; j < L-1; ++j){
			y = (y + sgn[x][s[j]]) % 2;
			x = tab[x][s[j]];
			if(x == 2 && y == 0 && b[j+1] == 3 && bs[j+1] == 0)
				return "YES";
		}
	}
	return "NO";
}
int main(){
	int T;
	cin >> T;
	for(int t=1;t<=T;++t){
		cin >> L >> X >> s;
		string r = solve();
		cout << "Case #" << t << ": " << r << endl;
	}
	return 0;
}
