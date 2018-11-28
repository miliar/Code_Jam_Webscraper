#include <iostream>

using namespace std;

char map[4][4];

bool tilt1(char type) {
	int x = 0;
	int y = 0;
	for(int i = 0; i < 4; i++) {
		if(map[y][x] != type && map[y][x] != 'T') return false;
		++x;
		++y;
	}
	return true;
}

bool tilt2(char type) {
	int x = 3;
	int y = 0;
	for(int i = 0; i < 4; i++) {
		if(map[y][x] != type && map[y][x] != 'T') return false;
		--x;
		++y;
	}
	return true;
}

bool row(int x,char type) {
	for(int y = 0; y < 4; y++) {
		if(map[y][x] != type && map[y][x] != 'T') return false;
	}
	return true;
}

bool line(int y,char type) {
	for(int x = 0; x < 4; x++) {
		if(map[y][x] != type && map[y][x] != 'T') return false;
	}
	return true;
}

bool isWin(char type) {
	for(int x = 0; x < 4; x++) {
		if(row(x,type)) return true;
	}
	for(int y = 0; y < 4; y++) {
		if(line(y,type)) return true;
	}
	if(tilt1(type)){
		return true;
	}
	if(tilt2(type)){
		return true;
	}

	return false;
}

int main() {
	int T;
	cin >> T;

	for(int i = 0; i < T; i++) {
		getchar();

		for(int y = 0; y < 4; y++) {
			for(int x = 0; x < 4; x++) {
				map[y][x] = getchar();
			}
			getchar();
		}

		if(isWin('X')) {
			cout << "Case #" << i+1 << ": X won" << endl;
			continue;
		}
		if(isWin('O')) {
			cout << "Case #" << i+1 << ": O won" << endl;
			continue;
		}

		bool completeFlag = true;
		for(int y = 0; y < 4; y++) {
			for(int x = 0; x < 4; x++) {
				if(map[y][x] == '.') completeFlag = false;
			}
		}
		if(!completeFlag) {
			cout << "Case #" << i+1 << ": Game has not completed" << endl;
			continue;
		}

		cout << "Case #" << i+1 << ": Draw" << endl;
	}

	return 0;
}