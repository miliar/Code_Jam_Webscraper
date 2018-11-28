#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	ifstream fin;
	
	fin.open("input.txt");
	
	int N;
	fin >> N;
	fin.ignore();
	
	vector<vector<string> > games;
	
	for(int i=0; i<N; i++)
	{
		vector<string> lines;
		
		for(int j=0; j<5; j++)
		{
			char line_chars[20];
			string line;
			fin.getline(line_chars, 20);
			line = line_chars;
			
			if(j<4) lines.push_back(line);
		}
		
		games.push_back(lines);
	}
	
	fin.close();
	
	for(int i=0; i<N; i++)
	{
		bool unfinished = false;
		for(int j=0; j<4; j++)
		{
			unfinished = unfinished || (games[i][j].find('.')!=-1);
		}
		
		bool four_x_in_row = false;
		bool four_O_in_row = false;
		bool four_x_in_diag =  false;
		bool four_O_in_diag =  false;
		bool four_x_in_col =  false;
		bool four_O_in_col =  false;
		
		for(int j=0; j<4; j++)
		{
			four_x_in_row = four_x_in_row || ((count(games[i][j].begin(), games[i][j].end(), 'X') + count(games[i][j].begin(), games[i][j].end(), 'T'))==4); 
		}
		
		for(int j=0; j<4; j++)
		{
			four_O_in_row = four_O_in_row || ((count(games[i][j].begin(), games[i][j].end(), 'O') + count(games[i][j].begin(), games[i][j].end(), 'T'))==4); 
		}
		
		bool temp0 = true;
		bool temp1 = true;
		bool temp2 = true;
		bool temp3 = true;
		for(int j=0; j<4; j++)
		{
			temp0 = temp0 && (games[i][j][0] == 'X' || games[i][j][0] == 'T');
			temp1 = temp1 && (games[i][j][1] == 'X' || games[i][j][1] == 'T');
			temp2 = temp2 && (games[i][j][2] == 'X' || games[i][j][2] == 'T');
			temp3 = temp3 && (games[i][j][3] == 'X' || games[i][j][3] == 'T');
		}
		four_x_in_col = temp0 || temp1 || temp2 || temp3;
		
		temp0 = true;
		temp1 = true;
		temp2 = true;
		temp3 = true;
		for(int j=0; j<4; j++)
		{
			temp0 = temp0 && (games[i][j][0] == 'O' || games[i][j][0] == 'T');
			temp1 = temp1 && (games[i][j][1] == 'O' || games[i][j][1] == 'T');
			temp2 = temp2 && (games[i][j][2] == 'O' || games[i][j][2] == 'T');
			temp3 = temp3 && (games[i][j][3] == 'O' || games[i][j][3] == 'T');
		}
		four_O_in_col = temp0 || temp1 || temp2 || temp3;
		
		
		
		bool temp = true;
		for(int j=0; j<4; j++)
		{
			temp = temp && (games[i][j][j] == 'X' || games[i][j][j] == 'T');
		}
		if(temp) four_x_in_diag = true;
		
		temp=true;
		for(int j=0; j<4; j++)
		{
			temp = temp && (games[i][j][3-j] == 'X' || games[i][j][3-j] == 'T');
		}
		if(temp) four_x_in_diag = true;
		
		
		temp = true;
		for(int j=0; j<4; j++)
		{
			temp = temp && (games[i][j][j] == 'O' || games[i][j][j] == 'T');
		}
		if(temp) four_O_in_diag = true;
		
		temp=true;
		for(int j=0; j<4; j++)
		{
			temp = temp && (games[i][j][3-j] == 'O' || games[i][j][3-j] == 'T');
		}
		if(temp) four_O_in_diag = true;
		
		
		
		
		bool x_won = four_x_in_row || four_x_in_diag || four_x_in_col;
		bool O_won = four_O_in_row || four_O_in_diag || four_O_in_col;
		
		
		if(x_won)
		{
			cout << "Case #" << (i+1) << ": X won" << endl;
		}
		else if(O_won)
		{
			cout << "Case #" << (i+1) << ": O won" << endl;
		}
		else if(unfinished)
		{
			cout << "Case #" << (i+1) << ": Game has not completed" << endl;
		}
		else
		{
			cout << "Case #" << (i+1) << ": Draw" << endl;
		}
	}
	
	return 0;
}