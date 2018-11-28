#include <iostream>
#include <cstdio>
using namespace std;

int judgeWin(char (* data)[5]) {
	bool flag;
	char base;
	for(int i = 1; i <= 4; i++) {
		flag = true;
		base = 0;
		for(int j = 1; j <= 4; j++) {
			if(data[i][j] == '.') {
				flag = false;
				break;
			}
			if(data[i][j] == 'T')
				continue;
			if(base == 0)
				base = data[i][j];
			else if(base == data[i][j]) {
				continue;
			} else {
				flag = false;
				break;
			}
		}
		if(flag) {
			if(base == 'X') {
				return 1;
			} else {
				return 2;
			}
		} 
	}

	for(int i = 1; i <= 4; i++) {
		flag = true;
		base = 0;
		for(int j = 1; j <= 4; j++) {
			if(data[j][i] == '.') {
				flag = false;
				break;
			}
			if(data[j][i] == 'T')
				continue;
			if(base == 0)
				base = data[j][i];
			else if(base == data[j][i]) {
				continue;
			} else {
				flag = false;
				break;
			}
		}
		if(flag) {
			if(base == 'X') {
				return 1;
			} else {
				return 2;
			}
		} 
	}

	flag = true;
	base = 0;
	for(int i = 1; i <= 4; i++) {
		if(data[i][i] == '.') {
			flag = false;
			break;
		}
		if(data[i][i] == 'T')
			continue;
		if(base == 0)
			base = data[i][i];
		else if(base == data[i][i]) {
			continue;
		} else {
			flag = false;
			break;
		}
	}

	if(flag) {
		if(base == 'X') {
			return 1;
		} else {
			return 2;
		}
	} 

	flag = true;
	base = 0;
	for(int i = 1; i <= 4; i++) {
		if(data[i][4 - i + 1] == '.') {
			flag = false;
			break;
		}
		if(data[i][4 - i + 1] == 'T')
			continue;
		if(base == 0)
			base = data[i][4 - i + 1];
		else if(base == data[i][4 - i + 1]) {
			continue;
		} else {
			flag = false;
			break;
		}
	}

	if(flag) {
		if(base == 'X') {
			return 1;
		} else {
			return 2;
		}
	} 

	for(int i = 1; i <= 4; i++) {
		for(int j = 1; j <= 4; j++) {
			if(data[i][j] == '.') {
				return 4;
			}
		}
	}

	return 3;
}

int main() {
	int numOfCasese;
	cin>>numOfCasese;
	freopen("out.txt", "w", stdout);
	for(int p = 1; p <= numOfCasese; p++) {
		char data[5][5];
		memset(data, '.', sizeof(data));
		for(int i = 1; i <= 4; i++) {
			getchar();
			for(int j = 1; j <= 4; j++) {
				scanf("%c", &data[i][j]);
			}
		}
		printf("Case #%d: ", p);
		switch(judgeWin(data)) {
			case 1:
				printf("X won\n");
				break;
			case 2:
				printf("O won\n");
				break;
			case 3:
				printf("Draw\n");
				break;
			case 4:
				printf("Game has not completed\n");
				break;
		}
		getchar();
	}
}