#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int r, c;
string s[101];
int check(int i, int j, char c1){
	int x = i, y = j;
	char c2 = s[i][j];
	s[i][j] = '.';
	while(i < r && j < c && i >= 0 && j >= 0){
		if(s[i][j] != '.'){
			s[x][y] = c2;
			return 1;
		}
		if(c1 == '>')
			j++;
		else if(c1 == '<')
			j--;
		else if(c1 == '^')
			i--;
		else if(c1 == 'v')
			i++;
	}
	s[x][y] = c2;
	return 0;
}

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t;
	cin >> t;
	for(int i = 0; i < t; i++){
		cin >> r >> c;
		for(int i = 0; i < r; i++)
			cin >> s[i];
		int ans = 0;
		for(int i = 0; i < r && ans >= 0; i++){
			for(int j = 0; j < c && ans >= 0; j++){
				if(s[i][j] == '.')
					continue;
				if(check(i, j, s[i][j]))
					continue;
				int k = 0;
				if(check(i, j, '>'))
					k++;
				if(check(i, j, '<'))
					k++;
				if(check(i, j, '^'))
					k++;
				if(check(i, j, 'v'))
					k++;
				if(k > 0)
					ans++;
				else
					ans = -1;
			}
		}
		cout << "Case #" << i + 1 << ": ";
		if(ans == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;

	}

	return 0;
}