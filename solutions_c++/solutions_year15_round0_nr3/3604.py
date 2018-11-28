#include <bits/stdc++.h>
using namespace std;

int table[4][4] = {
	{0, 1, 2, 3},
	{1, 0, 3, 2},
	{2, 3, 0, 1},
	{3, 2, 1, 0}
};
bool neg[4][4] = {
	{0, 0, 0, 0},
	{0, 1, 0, 1},
	{0, 1, 1, 0},
	{0, 0, 1, 1}
};
int toInt['z'];
int T, L, X;
string s;

int main(){
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);
	toInt['1'] = 0;
	toInt['i'] = 1;
	toInt['j'] = 2;
	toInt['k'] = 3;
	cin >> T;
	for(int t=1; t<=T; ++t){
		cin >> L >> X >> s;
		int let = 1;
		bool n = false;
		int num = 0;
		for(int i=0; i<X; ++i){
			for(char c : s){
				int v = toInt[c];
				n ^= neg[num][v];
				num = table[num][v];
				if(!n && let==num){
					++let;
					num = 0;
				}
			}
		}
		cout << "Case #" << t << ": ";
		if(let==4 && num==0 && !n) cout << "YES\n";
		else cout << "NO\n";
	}
}
