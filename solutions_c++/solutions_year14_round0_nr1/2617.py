#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<cstdio>
using namespace std;
int main(){
	freopen("MagicTrick.txt", "r", stdin);
	freopen("MagicTricout.txt", "w", stdout);
	int t, sq=1;
	cin >> t;
	while (t--){
		int g[5][5], g1[5][5], v, v1;
		
		cin >> v;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> g[i][j];
		
		cin >> v1;
		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
			cin >> g1[i][j];
		
		int guesscount = 0, guess;
		for (int i = 0; i<4; i++)
		for (int j = 0; j<4; j++){
			if (g[v - 1][i] == g1[v1 - 1][j]){
				guesscount++;
				guess = g[v - 1][i];
			}
		}

		if (guesscount == 1) printf("Case #%d: %d\n", sq++, guess);
		else if (guesscount>1) printf("Case #%d: Bad magician!\n", sq++);
		else printf("Case #%d: Volunteer cheated!\n", sq++);
	}
	return 0;
}