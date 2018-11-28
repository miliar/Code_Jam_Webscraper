#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int N = 4;
char field[N][N];

char check_rows()
{
	for(int i = 0; i < N; i++)
	{
		
		int x = 0, o = 0, t = 0;
		for(int j = 0; j < N; j++)
			if( field[i][j] == 'X') x++;
			else if( field[i][j] == 'O' ) o++;
			else if( field[i][j] == 'T' ) t++;
		if( x == 4 || (x == 3 && t == 1) ) return 'X';
		else if( o == 4 || (o == 3 && t == 1) ) return 'O';
	}
	return 'N';
}

char check_col()
{
        for(int i = 0; i < N; i++)
        {
		int x = 0, o = 0, t = 0;
                for(int j = 0; j < N; j++)
                        if( field[j][i] == 'X') x++;
                        else if( field[j][i] == 'O' ) o++;
                        else if( field[j][i] == 'T' ) t++;
                if( x == 4 || (x == 3 && t == 1) ) return 'X';
                else if( o == 4 || (o == 3 && t == 1) ) return 'O';
        }
        return 'N';
}

char check_diag()
{
	int x = 0, o = 0, t = 0;
        for(int i = 0; i < N; i++)
        {
		 if( field[i][i] == 'X') x++;
                 else if( field[i][i] == 'O' ) o++;
                 else if( field[i][i] == 'T' ) t++;
        }
	if( x == 4 || (x == 3 && t == 1) ) return 'X';
        else if( o == 4 || (o == 3 && t == 1) ) return 'O';
	x = 0, o = 0, t = 0;
	for(int i = N-1, j = 0; i >= 0 && j < 4; i--, j++)
	{
		if( field[i][j] == 'X') x++;
                else if( field[i][j] == 'O' ) o++;
                else if( field[i][j] == 'T' ) t++;
	}
	if( x == 4 || (x == 3 && t == 1) ) return 'X';
        else if( o == 4 || (o == 3 && t == 1) ) return 'O';
        return 'N';
}
bool check(int test)
{
	char r = check_rows();
	if( r == 'X')
	{
		cout << "Case #" << test << ": X won" << endl;
		return true;
	}
	else if( r == 'O')
	{
		cout << "Case #" << test << ": O won" << endl;
                return true;
	}
	r = check_col();
	if( r == 'X')
        {
                cout << "Case #" << test << ": X won" << endl;
                return true;
        }
        else if( r == 'O')
        {
                cout << "Case #" << test << ": O won" << endl;
                return true;
        }
	r = check_diag();
	if( r == 'X')
        {
                cout << "Case #" << test << ": X won" << endl;
                return true;
        }
        else if( r == 'O')
        {
                cout << "Case #" << test << ": O won" << endl;
                return true;
        }
	return false;
}

int main()
{

	int t;
	cin >> t;
	for(int test_case = 0; test_case < t; test_case++)
	{
		char ch;
		bool dot = false;
		for(int i = 0; i < N; i++)
			for(int j = 0; j < N; j++)
			{
				cin >> ch;
				field[i][j] = ch;
				if( ch == '.' ) dot = true;
			}
		if( !check(test_case + 1) )
		{
			if( dot )  cout << "Case #" << test_case + 1 << ": Game has not completed" << endl;
			else cout << "Case #" << test_case + 1 << ": Draw" << endl;
		}	
	}
	return 0;
}
