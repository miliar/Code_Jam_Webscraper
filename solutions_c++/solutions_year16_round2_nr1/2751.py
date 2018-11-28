#include <bits/stdc++.h>
using namespace std;

int ord[] = {0, 2, 4, 5, 6, 7, 8, 9, 1, 3};
char ind[] = {'Z', 'W', 'U', 'F', 'X', 'V', 'G', 'I', 'O', 'R'};
string s[] = {"ZERO", "TWO", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "ONE", "THREE"};

int fx[28], res[12];

int main(){
	freopen("out.txt", "w", stdout);
	freopen("A-large.in", "r", stdin);

	int t;
	cin >> t;
	for(int k = 1; k <= t; ++k){
		memset(fx, 0, sizeof(fx));
		memset(res, 0, sizeof(res));
		
		cout << "Case #" << k << ": ";
		string x;
		cin >> x;

		for(int i = 0; i < (int)x.size(); ++i){
			fx[x[i]-'A']++;
		}

		for(int i = 0; i < 10; ++i){
			int ks = fx[ind[i]-'A'];
			res[ord[i]] += ks; 
			for(int j = 0; j < (int)s[i].size(); ++j){
				fx[s[i][j] - 'A'] -= ks;
			}
		}

		for(int i = 0; i < 10; ++i){
			for(int j = 0; j < res[i]; ++j){
				cout << i;
			}
		}
		cout << '\n';
	}
}