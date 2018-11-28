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
bool checkB(vector<int> line)
{
	for (int i = 1; i < line.size(); ++i)
	{
		if(line[i] > line[i - 1])
			return false;
	}
	return true;
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
	vector<vector<bool> > isPossible(n, vector<bool> (m, false));
	int total = n * m;
	for (int i = 0; i < n; ++i)
	{

		if(checkB(lawn[i]))
		{
			for (int j = 0; j < m; ++j)
			{
				if (isPossible[i][j] == false)
				{
					--total;
					isPossible[i][j] = true;
				}
			}
		}
	}
	for (int i = 0; i < n; ++i)
	{
		reverse(lawn.begin(), lawn.end());
		if(checkB(lawn[i]))
		{
			for (int j = 0; j < m; ++j)
			{
				if (isPossible[i][j] == false)
				{
					--total;
					isPossible[i][j] = true;
				}
			}
		}
		reverse(lawn.begin(), lawn.end());
	}

	for (int j = 0; j < m; ++j)
	{
		vector<int> col(n);
		
		for (int i = 0; i < n; ++i)
		{
			col[i] = lawn[i][j];
		}
		if(checkB(col))
		{
			for (int i = 0; i < n; ++i)
			{
				if (isPossible[i][j] == false)
				{
					--total;
					isPossible[i][j] = true;
				}
			}
		}
		reverse(col.begin(), col.end());
		if(checkB(col))
		{
			for (int i = 0; i < n; ++i)
			{
				if (isPossible[i][j] == false)
				{
					--total;
					isPossible[i][j] = true;
				}
			}
		}
	}
	if (total == 0)
	{
		return "YES";
	}
	else if(total > 0)
	{
		return "NO";
	}
	else
	{
		return "WEIRD";
	}
}
bool isPalindrome(long long a)
{
	char _Buf[14];
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
vector<int> fs;
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
	int A, B;
	cin >> A >> B;
	vector<int>::iterator dA = upper_bound(fs.begin(), fs.end(), A - 1);
	vector<int>::iterator dB = upper_bound(fs.begin(), fs.end(), B);
	int nA = 0;
	if(dA != fs.end())
		nA = dA - fs.begin();
	int nB = 0;
	if(dB != fs.end())
		nB = dB - fs.begin();
	return nB - nA;
}
int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt.", "w", stdout);
	prepareC();
	int t; cin >> t;
	for (int test = 0; test < t; ++test)
	{
		cout << "Case #" << test + 1 << ": " << solveC() << endl;
	}
}