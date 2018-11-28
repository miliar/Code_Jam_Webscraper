
#include<iostream>
#include<iomanip>
#include<fstream>

using namespace std;


void find_state(char grid[4][4], int case_number)
{
	
	// Checking row sum
		
	for(int i = 0 ; i < 4 ; i++)
	{
		int sum = 0;

		sum = grid[i][0] + grid[i][1] +  grid[i][2] + grid[i][3];
		
		
		if(sum == 4*88 || sum == (3*88 + 84))
		{
			cout<<"Case #"<<case_number<<":"<<" X won";
			return;
		}
		
		else if(sum == 4*79 || sum == (3*79 + 84))
		{
			cout<<"Case #"<<case_number<<":"<<" O won";
			return;
		}
		
		else
		{}
	}	
	
	
	// checking column sum
	
	for(int i = 0 ; i < 4 ; i++)
	{
		int sum = 0;
		
		sum = grid[0][i] + grid[1][i] +  grid[2][i] + grid[3][i];
		
		if(sum == 4*88 || sum == (3*88 + 84))
		{
			cout<<"Case #"<<case_number<<":"<<" X won";
			return;
		}
		
		else if(sum == 4*79 || sum == (3*79 + 84))
		{
			cout<<"Case #"<<case_number<<":"<<" O won";
			return;
		}
				
		else
		{}
	}
	
	
	
	// checking diagonal sum
	
	int diag_sum = grid[0][0] + grid[1][1] + grid[2][2] + grid[3][3]; 
	
	if(diag_sum == 4*88 || diag_sum == (3*88 + 84))
	{
		cout<<"Case #"<<case_number<<":"<<" X won";
		return;
	}
	
	else if(diag_sum == 4*79 || diag_sum == (3*79 + 84))
	{
		cout<<"Case #"<<case_number<<":"<<" O won";
		return;
	}
	
	else
	{}
	
	
	// checking anti_diagonal_sum
	
	int anti_diag_sum = grid[0][3] + grid[1][2] + grid[2][1] + grid[3][0];
	
	if(anti_diag_sum == 4*88 || anti_diag_sum == (3*88 + 84))
	{
		cout<<"Case #"<<case_number<<":"<<" X won";
		return;
	}
	
	else if(anti_diag_sum == 4*79 || anti_diag_sum == (3*79 + 84))
	{
		cout<<"Case #"<<case_number<<":"<<" O won";
		return;
	}
	
	else
	{}
	
	
	// checking for draw
	
	for(int i = 0 ; i < 4 ; i++)
	{
		for(int j = 0 ; j < 4 ; j++)
		{
			if(grid[i][j] == '.')
			{
				cout<<"Case #"<<case_number<<":"<<" Game has not completed";
				return;
			}
		}
	}
	
	cout<<"Case #"<<case_number<<":"<<" Draw";
	
	return;
}


	
int main()
{
	int cases;
	int count = 0;
	char grid[4][4];
		
	ifstream in("A-large.in");
	
	if(!in)
	{
		cout<<"Cannot open file..."<<endl;
		return 0;
	}
	
	in >> cases;
	
	while(++count <= cases && !in.eof())
	{	
		for(int i = 0 ; i < 4 ; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> grid[i][j];
			}
		}
		find_state(grid, count);
		cout<<endl;
	}
	
	in.close();

	return 0;
}
	
