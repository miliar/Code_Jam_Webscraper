#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
char check(string line)
{
	int X = 0, O = 0, T = 0;
	for (int i = 0; i < line.length(); ++i)
	{
		if (line[i] == 'X')
			++X;
		if(line[i] == 'O')
			++O;
		if(line[i] == 'T')
			++T;
	}
	if(X == 4 || (X == 3 && T == 1))
	{
		return 'X';
	}
	if(O == 4 || (O == 3 && T == 1))
	{
		return 'O';
	}
	if(X + O + T != 4)
	{
		return '.';
	}
	return '*';
}
string solveA()
{
	vector<string> board(4);
	for (int i = 0; i < 4; ++i)
	{
		cin >> board[i];
	}

	char ans = '*';
	for (int i = 0; i < 4; ++i)
	{
		char res = check(board[i]);
		if(res == 'X' || res == 'O')
		{
			ans = res;
			break;
		} else if(res == '.') 
		{
			ans = res;
		}
		string col = "....";
		for (int j = 0; j < 4; ++j)
		{
			col[j] = board[j][i];
		}
		res = check(col);
		if(res == 'X' || res == 'O')
		{
			ans = res;
			break;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	string diag1 = "....";
	string diag2 = "....";
	for (int i = 0; i < 4; ++i)
	{
		diag1[i] = board[i][i];
		diag2[i] = board[i][3 - i];
	}
	if(ans != 'X' && ans != 'O')
	{
		char res = check(diag1);
		if (res == 'X' || res == 'O')
		{
			ans = res;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	if(ans != 'X' && ans != 'O')
	{
		char res = check(diag2);
		if (res == 'X' || res == 'O')
		{
			ans = res;
		} else if(res == '.') 
		{
			ans = res;
		}
	}
	if (ans == '.') {
		return "Game has not completed";
	} else if(ans == '*')
	{
		return "Draw";
	} else if(ans == 'X')
	{
		return "X won";
	} else
	{
		return "O won";
	}
}
int k;
bool checkRow(vector<vector<int> >& lawn, int row)
{
	for (int i = 0; i < lawn[row].size(); ++i)
	{
		if(lawn[row][i] == -2)
			continue;
		if(lawn[row][i] != k)
			return false;
	}
	return true;
}
void markRow(vector<vector<int> >& lawn, int row)
{
	for (int i = 0; i < lawn[row].size(); ++i)
	{
		lawn[row][i] = -2;
	}
}
bool checkCol(vector<vector<int> >& lawn, int col)
{
	for (int i = 0; i < lawn.size(); ++i)
	{
		if(lawn[i][col] == -2)
			continue;
		if(lawn[i][col] != k)
			return false; 
	}
	return true;
}
void markCol(vector<vector<int> >& lawn, int col)
{
	for (int i = 0; i < lawn.size(); ++i)
	{
		lawn[i][col] = -2;
	}
}
string solveB()
{
	int n, m; cin >> n >> m;
	vector<vector<int> > lawn(n, vector<int> (m, 0));
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
			cin >> lawn[i][j];
	}
	for (k = 1; k < 101; ++k)
	{
		for (int i = 0; i < n; ++i)
		{
			if(checkRow(lawn, i) )
			{
				markRow(lawn, i);
			}
		}
		for (int i = 0; i < m; ++i)
		{
			if(checkCol(lawn, i) )
			{
				markCol(lawn, i);
			}
		}
	}
	for (int i = 0; i < n; ++i)
	{
		for (int j = 0; j < m; ++j)
		{
			if (lawn[i][j] != -2)
				return "NO";
		}
	}
	return "YES";
}
bool isPalindrome(long long a)
{
	char _Buf[20];
    sprintf(_Buf, "%d", a);
	string num = string(_Buf);
	int n = num.length();
	for (int i = 0; i < n / 2; ++i)
	{
		if(num[i] != num[n - i - 1])
			return false;
	}

	return true;
}
vector<long long> fs;
void prepareC()
{
	fs.reserve(10000);
	for (long long i = 1; i < 1e7; ++i)
	{
		if(isPalindrome(i) && isPalindrome(i * i))
			fs.push_back(i * i);
	}
}
int solveC()
{
	long long A, B;
	cin >> A >> B;
	vector<long long>::iterator dA = upper_bound(fs.begin(), fs.end(), A - 1);
	vector<long long>::iterator dB = upper_bound(fs.begin(), fs.end(), B);
	long long nA = 0;
	if(dA != fs.end())
		nA = dA - fs.begin();
	else
		nA = fs.size();
	long long nB = 0;
	if(dB != fs.end())
		nB = dB - fs.begin();
	else
		nB = fs.size();
	return nB - nA;
}
int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("out.txt.", "w", stdout);

	int t; cin >> t;
	for (int test = 0; test < t; ++test)
	{
		cout << "Case #" << test + 1 << ": " << solveB() << endl;
	}
}