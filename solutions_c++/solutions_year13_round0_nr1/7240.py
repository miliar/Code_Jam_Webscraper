// Jai Mata Di
#include<iostream>
#include<vector>
using namespace std;
class TicTac
{
public:
	vector<vector<char> > b;
	char winner;
	bool isGameIncomplete;
	TicTac()
	{
		winner = '?';
		isGameIncomplete = false;
	}
	void Input()
	{
		for(int i=0;i<4;i++)
		{
			vector<char> v;
			for(int j=0;j<4;j++)
			{
				char c;
				cin>>c;
				v.push_back(c);
			}
			b.push_back(v);
		}
	}
	void Print()
	{
		cout<<endl;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cout<<b[i][j]<<" ";
			}
			cout<<endl;
		}
	}
	bool IsWinnerFoundInRows()
	{
		for(int i=0;i<4;i++)
		{
			bool isXPossible = true;
			bool isOPossible = true;
			for(int j=0;j<4;j++)
			{
				if(b[i][j] == 'X')
				{
					isOPossible = false;
				}
				if(b[i][j] == 'O')
				{
					isXPossible = false;
				}
				if(b[i][j] == '.')
				{
					isXPossible = false;
					isOPossible = false;
					isGameIncomplete = true;
				}
			}
			if(isXPossible == true)
			{
				winner = 'X';
				return true;
			}
			if(isOPossible == true)
			{
				winner = 'O';
				return true;
			}
		}
		return false;
	}
	bool IsWinnerFoundInColumns()
	{
		for(int i=0;i<4;i++)
		{
			bool isXPossible = true;
			bool isOPossible = true;
			for(int j=0;j<4;j++)
			{
				if(b[j][i] == 'X')
				{
					isOPossible = false;
				}
				if(b[j][i] == 'O')
				{
					isXPossible = false;
				}
				if(b[j][i] == '.')
				{
					isXPossible = false;
					isOPossible = false;
					isGameIncomplete = true;
				}
			}
			if(isXPossible == true)
			{
				winner = 'X';
				return true;
			}
			if(isOPossible == true)
			{
				winner = 'O';
				return true;
			}
		}
		return false;
	}
	bool IsWinnerFoundInDiagonals()
	{
		bool isXPossible = true;
		bool isOPossible = true;
		for(int i=0;i<4;i++)
		{
			if(b[i][i] == 'X')
			{
				isOPossible = false;
			}
			if(b[i][i] == 'O')
			{
				isXPossible = false;
			}
			if(b[i][i] == '.')
			{
				isXPossible = false;
				isOPossible = false;
				isGameIncomplete = true;
			}
		}
		if(isXPossible == true)
		{
			winner = 'X';
			return true;
		}
		if(isOPossible == true)
		{
			winner = 'O';
			return true;
		}

		isXPossible = true;
		isOPossible = true;
		for(int i=0;i<4;i++)
		{
			if(b[i][3-i] == 'X')
			{
				isOPossible = false;
			}
			if(b[i][3-i] == 'O')
			{
				isXPossible = false;
			}
			if(b[i][3-i] == '.')
			{
				isXPossible = false;
				isOPossible = false;
				isGameIncomplete = true;
			}
		}
		if(isXPossible == true)
		{
			winner = 'X';
			return true;
		}
		if(isOPossible == true)
		{
			winner = 'O';
			return true;
		}

		return false;
	}
	
	void CheckWinner()
	{
		if(IsWinnerFoundInRows())
		{
			cout<<winner<<" won"<<endl;
		}
		else if(IsWinnerFoundInColumns())
		{
			cout<<winner<<" won"<<endl;
		}
		else if(IsWinnerFoundInDiagonals())
		{
			cout<<winner<<" won"<<endl;
		}
		else if(isGameIncomplete)
		{
			cout<<"Game has not completed"<<endl;
		}
		else
		{
			cout<<"Draw"<<endl;
		}
	}
};
int main()
{
	int noOfTestCases;
	cin>>noOfTestCases;
	for(int i=1;i<=noOfTestCases;i++)
	{
		TicTac t;
		t.Input();
///		t.Print();
		cout<<"Case #"<<i<<": ";
		t.CheckWinner();
	}
	return 0;
}
