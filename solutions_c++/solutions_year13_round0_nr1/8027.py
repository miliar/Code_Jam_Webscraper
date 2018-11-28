#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

char board[4][5];
bool notComp;

bool check(char* arr, char c) {

	for (int i = 0 ; i < 4; i ++) {

		if (arr[i] == '.') {
			notComp = true;
			return false;
		}

		if ((arr[i] != 'T' && arr[i] != c))
			return false;
	}

	return true;
}

bool isWon(char c) {

	for (int i = 0; i < 4; i ++)
		if (check(board[i], c))
			return true;

	char arr[5];
	for (int i = 0; i < 4; i ++) {

		for (int j = 0; j < 4; j ++)
			arr[j] = board[j][i];

		if (check(arr, c))
			return true;
	}

	for (int i = 0; i < 4; i ++)
		arr[i] = board[i][i];

	if (check(arr, c))
		return true;

	for (int i = 0; i < 4; i ++)
		arr[i] = board[i][3 - i];

	if (check(arr, c))
		return true;

	return false;
}

int main() {

	freopen ("A-small-attempt1.in","r",stdin);
	freopen ("output.out","w",stdout);
	int t, idx = 1;
	cin >> t;

	while (t --) {

		notComp = false;

		for (int i = 0; i < 4; i ++)
			cin >> board[i];

		cout << "Case #" << idx;
		if (isWon('X') && !isWon('O'))
			cout << ": X won";

		else if (!isWon('X') && isWon('O'))
			cout << ": O won";

		else if (!isWon('X') && !isWon('O')) {
			if (notComp)
				cout << ": Game has not completed";
			else
				cout << ": Draw";
		}

		cout << endl;
		idx ++;
	}

	fclose(stdin);
	fclose(stdout);

	return 0;
}
