#include <iostream>
#include <vector>
using namespace std;

string generateans(char x, int n)
{
	if (n == 1 && x == 'R')
	{
		return "RS";
	}
	else if (n == 1 && x == 'P')
	{
		return "PR";
	}
	else if (n == 1 && x == 'S')
	{
		return "PS";
	}
	else if (x == 'R')
	{
		string string1 = generateans('R', n-1);
		string string2 = generateans('S', n-1);
		if (string1 < string2)
		{
			return string1 + string2;
		}
		else
		{
			return string2 + string1;
		}
	}
	else if (x == 'P')
	{
		string string1 = generateans('R', n-1);
		string string2 = generateans('P', n-1);
		if (string1 < string2)
		{
			return string1 + string2;
		}
		else
		{
			return string2 + string1;
		}
	}
	else 
	{
		string string1 = generateans('P', n-1);
		string string2 = generateans('S', n-1);
		if (string1 < string2)
		{
			return string1 + string2;
		}
		else
		{
			return string2 + string1;
		}
	}
}

int main()
{
	// we get the quantities for a S win, P win, and R win
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int N, R, P, S;
		cin >> N >> R >> P >> S;

		int Stry[3][N+1];
		int Rtry[3][N+1];
		int Ptry[3][N+1];

		Stry[0][0]=0;
		Stry[1][0]=0;
		Stry[2][0]=1;
		Rtry[0][0]=1;
		Rtry[1][0]=0;
		Rtry[2][0]=0;
		Ptry[0][0]=0;
		Ptry[1][0]=1;
		Ptry[2][0]=0;

		for (int j = 1; j < N+1; j++)
		{
			Rtry[0][j] = Rtry[0][j-1]+Rtry[1][j-1];
			Rtry[1][j] = Rtry[2][j-1]+Rtry[1][j-1];
			Rtry[2][j] = Rtry[0][j-1]+Rtry[2][j-1];
			Stry[0][j] = Stry[0][j-1]+Stry[1][j-1];
			Stry[1][j] = Stry[2][j-1]+Stry[1][j-1];
			Stry[2][j] = Stry[0][j-1]+Stry[2][j-1];
			Ptry[0][j] = Ptry[0][j-1]+Ptry[1][j-1];
			Ptry[1][j] = Ptry[2][j-1]+Ptry[1][j-1];
			Ptry[2][j] = Ptry[0][j-1]+Ptry[2][j-1];
		}

		if (Rtry[0][N] == R && Rtry[1][N] == P && Rtry[2][N] == S)
		{
			cout << "Case #" << i+1 << ": " << generateans('R', N) << endl;
		}
		else if (Ptry[0][N] == R && Ptry[1][N] == P && Ptry[2][N] == S)
		{
			cout << "Case #" << i+1 << ": " << generateans('P', N) << endl;
		}
		else if (Stry[0][N] == R && Stry[1][N] == P && Stry[2][N] == S)
		{
			cout << "Case #" << i+1 << ": " << generateans('S', N) << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << "IMPOSSIBLE" << endl;
		}


	}

}