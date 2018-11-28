#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

bool the_winner_is(char c , vector<string> &V)
{
	int won_diagonal1 = 1 , won_diagonal2 = 1;
	for(int i = 0; i < 4; ++i)
	{
		int won_horizontal = 1 , won_vertical = 1;
		for(int j = 0; j < 4; ++j)
		{
			if(V[i][j] != c && V[i][j] != 'T')
				won_horizontal = 0;
			if(V[j][i] != c && V[j][i] != 'T')
			{
				won_vertical = 0;
			}
		}
		if(won_horizontal || won_vertical)return true;
		
		if(V[i][i] != c && V[i][i] != 'T')
			won_diagonal1 = 0;
		if(V[i][3-i] != c && V[i][3-i] != 'T')
			won_diagonal2 = 0;
	}
	return won_diagonal1 || won_diagonal2;
}

bool is_palindrome(int i)
{
	char number[10];
	sprintf(number,"%d",i);
	string A = number;
	string B = A;
	reverse(B.begin(),B.end());
	return A == B;
}

int main()
{
	int T;
	cin >> T;
	for(int tc = 1 ; tc<=T ; ++tc)
	{
		int A,B;
		cin >> A >> B;
		int cnt = 0;
		for(int i = A; i <= B; ++i)
		{
			int sq = sqrt(i);
			if(sq*sq != i)continue;
			if(is_palindrome(i) && is_palindrome(sq))
				cnt++;
		}
		cout << "Case #" << tc <<": ";
		cout << cnt << endl;
	}
	
}


// A * 1001 + B * 0110

// A*A * 1001^2 + 2*A*B*1001*0110 + B*B*0110^2


/*
6
XXXT
....
OO..
....

XOXT
XXOO
OXOX
XXOO

XOX.
OX..
....
....

OOXX
OXXX
OX.T
O..O

XXXO
..O.
.O..
T...

OXXX
XO..
..O.
...O


*/

