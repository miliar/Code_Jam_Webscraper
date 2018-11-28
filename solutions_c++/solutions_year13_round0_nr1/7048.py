#include <cstdio>
#include <vector>
#include <iostream>

using namespace std;

int main()
{
	int test_cases;
	scanf("%d",&test_cases);
	for (int test_case=1; test_case<=test_cases; test_case++) {
		bool game_completed = true,cont=false;
		vector<string> grid;
		for (int i=0; i<4; i++) {
			string s;
			cin >> s;
			grid.push_back(s);
		}
		for (int i=0; i<4; i++) {
			int cur=0;
			for (int j=0; j<4; j++) {
				if (grid[i][j]=='X') {
					cur++;
				} else if (grid[i][j]=='O') {
					cur--;
				} else if (grid[i][j]=='.') {
					game_completed=false;
					cur=100;
				}
			}
			if (cur==3 || cur==4) {
				printf("Case #%d: X won\n",test_case);
				cont = true;
				break;
			}
			if (cur==-3 || cur==-4) {
				printf("Case #%d: O won\n",test_case);
				cont=true;
				break;
			}
		}
		if (cont) {
			continue;
		}
		for (int i=0; i<4; i++) {
			int cur=0;
			for (int j=0; j<4; j++) {
				if (grid[j][i]=='X') {
					cur++;
				} else if (grid[j][i]=='O') {
					cur--;
				} else if (grid[j][i]=='.') {
					game_completed=false;
					cur=100;
				}
			}
			if (cur==3 || cur==4) {
				printf("Case #%d: X won\n",test_case);
				cont = true;
				break;
			}
			if (cur==-3 || cur==-4) {
				printf("Case #%d: O won\n",test_case);
				cont = true;
				break;
			}
		}
		if (cont) {
			continue;
		}
		int cur=0;
		for (int i=0; i<4; i++) { 
			if (grid[i][i]=='X') {
				cur++;
			} else if (grid[i][i]=='O') {
				cur--;
			} else if (grid[i][i]=='.') {
				game_completed=false;
				cur=100;
			}
		}
		if (cur==3 || cur==4) {
			printf("Case #%d: X won\n",test_case);
			continue;
		}
		if (cur==-3 || cur==-4) {
			printf("Case #%d: O won\n",test_case);
			continue;
		}
		cur=0;
		for (int i=0; i<4; i++) { 
			if (grid[i][3-i]=='X') {
				cur++;
			} else if (grid[i][3-i]=='O') {
				cur--;
			} else if (grid[i][3-i]=='.') {
				game_completed=false;
				cur=100;
			}
		}
		if (cur==3 || cur==4) {
			printf("Case #%d: X won\n",test_case);
			continue;
		}
		if (cur==-3 || cur==-4) {
			printf("Case #%d: O won\n",test_case);
			continue;
		}
		if (game_completed) {
			printf("Case #%d: Draw\n",test_case);
		} else {
			printf("Case #%d: Game has not completed\n",test_case);
		}
	}
	return 0;
}
