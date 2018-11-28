#include <iostream>
using namespace std;

#define T_SIZE 4

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

bool DetermineWinningCase(char** table, char target)
{
	//determine row
	bool check;
	
	//vertical!
	for(int i = 0; i < T_SIZE; i++)
	{
		//vertical!
		check = true;
		for(int j = 0; j < T_SIZE; j++)
		{
			if(!(table[i][j] == 'T' || table[i][j] == target))
				check = false;
		}
		if(check)
			return true;
			
		//horizontal
		check = true;
		for(int j = 0; j < T_SIZE; j++)
		{
			if(!(table[j][i] == 'T' || table[j][i] == target))
				check = false;
		}
		if(check)
			return true;
	}
	
	//diagonal left->right
	check = true;
	for(int j = 0; j < T_SIZE; j++)
	{
		if(!(table[j][j] == 'T' || table[j][j] == target))
			check = false;
	}
	if(check)
		return true;
		
	//diagonal right->left
	check = true;
	for(int j = 0; j < T_SIZE; j++)
	{
		if(!(table[j][T_SIZE - 1 - j] == 'T' || table[j][T_SIZE - 1 - j] == target))
			check = false;
	}
	if(check)
		return true;
	
	return false;
}

bool CheckGameEnded(char** table)
{
	for (int i = 0; i < T_SIZE; i++)
	{
	    for (int j = 0; j < T_SIZE; j++)
	    {
	    	if(table[i][j] == '.')
				return false;
	    }
	}
	
	return true;
}

char** ReadCase()
{
	char** table = new char*[T_SIZE];
	
	for (int i = 0; i < T_SIZE; i++)
	{
	    table[i] = new char[T_SIZE];
	    for (int j = 0; j < T_SIZE; j++)
	    	cin >> table[i][j];
	}	
	
	return table;
}

int main(int argc, char** argv) {
	
	//read no of cases.
	int case_no = 0;
	cin >> case_no;
	
	
	bool x_win[case_no], o_win[case_no], game_finished[case_no];
	
	for(int i = 0; i < case_no; i++)
	{
		char** table;
		x_win[i] = false;
		o_win[i] = false; 
		game_finished[i] = true;
		
		//read each case line by line and store in the array.
		table = ReadCase();

		//check the winning condition of X
		x_win[i] = DetermineWinningCase(table, 'X');
				
		//check the winning condition of O
		o_win[i] = DetermineWinningCase(table, 'O');
				
		//check if the game is completely ended.
		if(!x_win[i] && !o_win[i])
		game_finished[i] = CheckGameEnded(table);
		
		//delete board!
		for(int i = 0; i < T_SIZE; i++)
			delete[] table[i];
		delete[] table;
	}
	
	for(int i = 0; i < case_no; i++)
	{
		//print out the result.
		cout << "Case #" << i+1 << ": ";
		if (!game_finished[i]) cout <<"Game has not completed";
		else if(x_win[i] && !o_win[i]) cout << "X won";
		else if(!x_win[i] && o_win[i]) cout << "O won";
		else cout << "Draw";
		
		cout << endl;
	}
	
	return 0;
}
