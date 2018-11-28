#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int n, r, p, s;
string ans;

char winner(char a, char b){
	if (a == 'R'&&b == 'P')return 'P';
	if (a == 'P'&&b == 'R')return 'P';
	if (a == 'R'&&b == 'S')return 'R';
	if (a == 'S'&&b == 'R')return 'R';
	if (a == 'S'&&b == 'P')return 'S';
	if (a == 'P'&&b == 'S')return 'S';
}

bool valid(string x){
	if (x.size() == 1)return 1;
	string y = "";
	for (int i = 0; i < x.size(); i += 2){
		if (x[i] == x[i + 1])return 0;
		y += winner(x[i], x[i + 1]);
	}
	return valid(y);
}

int main(){
	int T; cin >> T;
	int tc = 0;
	while (T--){
		tc++;
		cin >> n >> r >> p >> s;
		ans = "";
		while (p--)ans += 'P';
		while (r--)ans += 'R';
		while (s--)ans += 'S';
		do{
			if (valid(ans)){
				goto good;
			}
		} while (next_permutation(ans.begin(), ans.end()));
		cout << "Case #" << tc << ": " << "IMPOSSIBLE" << endl;

		continue;

		good:
		cout << "Case #" << tc << ": " << ans << endl;

	}
}