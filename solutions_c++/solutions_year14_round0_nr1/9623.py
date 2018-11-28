#ifdef _MSC_VER
#define _CRT_SECURE_NO_WARNINGS
#endif
#include<iostream>
#include<vector>
#include<fstream>
#include<algorithm>
#include<string>
using namespace std;
int T;
int first, second;
int mas[5][5];
int mas2[5][5];

void print2d(vector< vector<int> >vec) {
	for (int i = 0; i < vec.size(); i++) {
		cout << i << ":   ";
		for (int j = 0; j < vec[i].size(); j++){
			cout << vec[i][j] << " ";
		}
		cout << endl;
	}
}

void print(vector<int>vec) {
	for (int i = 0; i < vec.size(); i++)
		cout << i << ": " << vec[i] << endl;
}

int readInt() {
	bool minus = false;
	int result = 0;
	char ch;
	ch = getchar();
	while (true) {
		if (ch == '-') break;
		if (ch >= '0' && ch <= '9') break;
		ch = getchar();
	}
	if (ch == '-') minus = true; else result = ch - '0';
	while (true) {
		ch = getchar();
		if (ch < '0' || ch > '9') break;
		result = result * 10 + (ch - '0');
	}
	if (minus)
		return -result;
	else
		return result;
}

int main() {
	freopen("Text.txt", "r", stdin);
	ofstream ofs("output.in");
	cin >> T;
	int cases = 1;
	while (T--)
	{
		bool badMagician = false;
		bool cheater = true;
		int counter = 0;
		int myCard;

		cin >> first;
		for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			cin >> mas[i][j];

		cin >>second;

		for (int i = 1; i <= 4; i++)
		for (int j = 1; j <= 4; j++)
			cin >> mas2[i][j];

		for (int i = 1; i <= 4; i++)
		{
			for (int j = 1; j <= 4; j++)
			{
				if (mas[first][i] == mas2[second][j])
				{
					cheater = false; counter++; myCard = mas[first][i];
				}
			}
		}
		if (counter > 1) badMagician = true;

		if (badMagician) ofs << "Case #" << cases << ": " << "Bad magician!" << endl;
		else if (cheater) ofs << "Case #" << cases << ": " << "Volunteer cheated!" << endl;
		else ofs << "Case #" << cases << ": " << myCard << endl;

		cases++;
	}

	return 0;
}