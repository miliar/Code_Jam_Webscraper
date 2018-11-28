#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string str("");
int grid[4][4] = {{1, 2, 3, 4}, {2, -1, 4, -3}, {3, -4, -1, 2}, {4, 3, -2, -1}};

int res[10000][10000];

int convert(char c)
{
	int res;
	switch (c) {
	case '1':
		res = 1;
		break;
	case 'i':
		res = 2;
		break;
	case 'j':
		res = 3;
		break;
	case 'k':
		res = 4;
		break;
	}
	return res;
}

bool valid(string s, int c)
{
	int sign = 1;
	int res = 1;
	for (int i = 0, len = s.size(); i < len; i++) {
		if (res < 0) {
			sign = -sign;
			res = -res;
		}
		res = grid[res - 1][convert(s[i]) - 1];
	}
	if ((res < 0 && sign < 0 && -res == c) || (res >0 && sign > 0 && res == c))
		return true;
	return false;
}

int main()
{
	ifstream infile("C-small-attempt0.in");
	//ifstream infile("A-large.in");
	ofstream outfile("C-small.out");
	streambuf *oldinbuf = cin.rdbuf(infile.rdbuf());
	streambuf *oldoutbuf = cout.rdbuf(outfile.rdbuf());
	int n = 0, l = 0, x = 0, index = 0;
	bool flag = true;

	cin >> n;
	while (index < n) {
		cin >> l >> x;
		cin >> str;
		string s(str);
		for (int i = 0; i < x - 1; i++)
			str += s;
		flag = false;


		for (int i = 0, len = str.size(); i < len; i++) {
			for (int j = i; j < len; j++) {
				if (i != j) {
					if (res[i][j - 1] < 0) {
						res[i][j] = -grid[-res[i][j - 1] - 1][convert(str[j]) - 1];
					} else {
						res[i][j] = grid[res[i][j - 1] - 1][convert(str[j]) - 1];
					}
				} else {
					res[i][j] = convert(str[j]);
				}
			}
		}
		for (int i = 0, len = str.size(); i < len - 1; i++) {
			for (int j = i + 1; j < len - 1; j++) {
				if (res[0][i] == 2 && res[i + 1][j] == 3 && res[j + 1][len - 1] == 4) {
					flag = true;
					break;
				}
			}
			if (flag)
				break;
		}
		if (flag)
			cout << "Case #" << index + 1 << ": YES" << endl;
		else
			cout << "Case #" << index + 1 << ": NO" << endl;
		index++;
	}
	cout.rdbuf(oldoutbuf);
	cin.rdbuf(oldinbuf);
	return 0;
}