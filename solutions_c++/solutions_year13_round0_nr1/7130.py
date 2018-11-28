#include <iostream>
#include <fstream>

using namespace std;

string output[4] = { "X won", 
					 "O won",
					 "Game has not completed",
					 "Draw" 
				   };

int s(string s[]) 
{
	int count = 0;
	
	for (int i = 0; i < 4 ; ++i )
	{
		count = 0 ;
		for (int j = 0; j < 4 ; ++j )
			if (s[i][j] == 'X' || s[i][j] == 'T')
				count++;
		if (count == 4)
			return 0;
	}

	for (int i = 0; i < 4 ; ++i )
	{
		count = 0 ;
		for (int j = 0; j < 4 ; ++j )
			if (s[i][j] == 'O' || s[i][j] == 'T')
				count++;
		if (count == 4)
			return 1;
	}

	for (int i = 0; i < 4 ; ++i )
	{
		count = 0 ;
		for (int j = 0; j < 4 ; ++j )
			if (s[j][i] == 'X' || s[j][i] == 'T')
				count++;
		if (count == 4)
			return 0;
	}
	
	count = 0 ;
	for (int i = 0, j = 0; i < 4 ; ++i, ++j )
	{
		if (s[j][i] == 'X' || s[j][i] == 'T')
				count++;
	}

	if(count == 4)
		return 0;
	
	count = 0 ;
	for (int i = 3, j = 0; i >= 0 ; --i, ++j )
	{
		if (s[i][j] == 'X' || s[i][j] == 'T')
				count++;
	}

	if(count == 4)
		return 0;
	
	count = 0 ;
	for (int i = 0, j = 0; i < 4 ; ++i, ++j )
	{
		if (s[j][i] == 'O' || s[j][i] == 'T')
				count++;
	}

	if(count == 4)
		return 1;
	
	count = 0 ;
	for (int i = 3, j = 0; i >= 0 ; --i, ++j )
	{
		if (s[i][j] == 'O' || s[i][j] == 'T')
				count++;
	}

	if(count == 4)
		return 1;
	

	for (int i = 0; i < 4 ; ++i )
	{
		count = 0 ;
		for (int j = 0; j < 4 ; ++j )
			if (s[j][i] == 'O' || s[j][i] == 'T')
				count++;
		if (count == 4)
			return 1;
	}
	
	for (int i = 0; i < 4 ; ++i )
	{
		for (int j = 0; j < 4 ; ++j )
			if (s[i][j] == '.')
				return 2;
	}

	return 3;
}




void solve() 
{
	int T = 0 , x = 0;
	//fstream in, out ;
	//in.open("a.txt"); out.open("out.txt");

	string input[4];
	cin >> T;
	
	while(T-- > 0)
	{
		for (int i = 0; i < 4; i++)
			cin >> input[i]; 
		
		x += 1; 
		cout << "Case #" << x << ": " << output[s(input)] << endl;
		
	}
	
}

int main() 
{
	solve();
	return 0;
}