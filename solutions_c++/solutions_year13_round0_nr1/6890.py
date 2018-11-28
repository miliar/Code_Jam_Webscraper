#include <iostream>
#include <string>
using namespace std;
  
string checkWin(string s[]);
int checkRow(string s);
int checkElement(char c1, char c2, char c3, char c4);

int main() {

	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

    int cases;
	string temp;
	cin >> cases;
	getline(cin, temp);
	for(int i = 0; i < cases; i++) {
		
		string s[5];
		for(int k = 0; k < 4; k++)
			getline(cin, s[k]);
		string result = checkWin(s);
		cout << "Case #" << i+1 << ": " << result << endl;

		getline(cin, temp);
	}
    return 0;  
}

string checkWin(string s[]) {
	for(int i = 0; i < 4; i++) {
		int r = checkRow(s[i]);
		switch (r)
		{
		case 0:
			return "X won";
		case 1:
			return "O won";
		}
		r = checkElement(s[0][i], s[1][i], s[2][i], s[3][i]);
		switch (r)
		{
		case 0:
			return "X won";
		case 1:
			return "O won";
		}
		r = checkElement(s[0][0], s[1][1], s[2][2], s[3][3]);
		switch (r)
		{
		case 0:
			return "X won";
		case 1:
			return "O won";
		}
		r = checkElement(s[0][3], s[1][2], s[2][1], s[3][0]);
		switch (r)
		{
		case 0:
			return "X won";
		case 1:
			return "O won";
		}
	}
	int a = 0;
	for(int i = 0; i < 4; i++)
		for(int j = 0; j < 4; j++)
			if(s[i][j] == 'O' || s[i][j] == 'X' || s[i][j] == 'T')
				a++;
	if(a == 16)
		return "Draw";
	return "Game has not completed";
}

int checkRow(string s) {
	int o = 0, x = 0;
	for(int i = 0; i < 4; i++) {
		switch (s[i])
		{
		case 'O':
			o++;
			break;
		case 'X':
			x++;
			break;
		case 'T':
			o++;
			x++;
			break;
		}
	}
	if(x == 4) return 0;
	if(o == 4) return 1;
	return 2;	// draw
}

int checkElement(char c1, char c2, char c3, char c4) {
	int o = 0, x = 0;
	char t[4] = {c1, c2, c3, c4};
	for(int i = 0; i < 4; i++) {
		switch(t[i]) {
		case 'O':
			o++;
			break;
		case 'X':
			x++;
			break;
		case 'T':
			o++;
			x++;
			break;
		}
	}
	if(x == 4) return 0;
	if(o == 4) return 1;
	return 2;
}