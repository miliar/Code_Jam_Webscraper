#include<fstream>
#include<iostream>
#include<string>

using namespace std;
const int ROW = 4;
const int COL = 4;
char mat[ROW][COL];
ifstream infile ("in.in");
ofstream outfile ("out.out");

void fetchInput();
void printOutput();

void checkMat()
{
	bool empty_cell = false;
	int t_r = -1, t_c = -1;
	int r, c;

	//check if empty_cell and T exists
	for(r = 0 ; r < ROW; r++)
	{
		for(c = 0; c < COL; c++)
		{
			if(mat[r][c] == '.')
				empty_cell = true;
			else if(mat[r][c] == 'T')
			{
				t_r = r;
				t_c = c;
			}
		}
	}

	int x_chance = 0, o_chance = 0, t_chance = 0;
	//traverseRows
	for(r = 0; r < ROW; r++)
	{
		for(c = 0; c < COL; c++)
		{
			if(mat[r][c] == 'X')
				x_chance++;
			else if(mat[r][c] == 'O')
				o_chance++;
		}

		t_chance = (t_r == r ? 1 : 0);
		if((x_chance + t_chance) == 4)
		{
			outfile<<"X won";
			return;
		}
		else if((o_chance + t_chance) == 4)
		{
			outfile<<"O won";
			return;
		}
		x_chance = 0, o_chance = 0, t_chance = 0;
	}
	
	//traverseCols
	for(c = 0; c < COL; c++)
	{
		for(r = 0; r < ROW; r++)
		{
			if(mat[r][c] == 'X')
				x_chance++;
			else if(mat[r][c] == 'O')
				o_chance++;
		}

		t_chance = (t_c == c ? 1 : 0);
		if((x_chance + t_chance) == 4)
		{
			outfile<<"X won";
			return;
		}
		else if((o_chance + t_chance) == 4)
		{
			outfile<<"O won";
			return;
		}
		x_chance = 0, o_chance = 0, t_chance = 0;
	}

	//traverseDiags
	    // traverseLeftDiag
	    for(r = 0; r < ROW; r++)
		{
			if(mat[r][r] == 'X')
				x_chance++;
			else if(mat[r][r] == 'O')
				o_chance++;
			else if(mat[r][r] == 'T')
				t_chance++;
		}

		if((x_chance + t_chance) == 4)
		{
			outfile<<"X won";
			return;
		}
		else if((o_chance + t_chance) == 4)
		{
			outfile<<"O won";
			return;
		}
		x_chance = 0, o_chance = 0, t_chance = 0;

        // traverse Right Diagonal
		r = 0, c = COL-1;
		while(r < ROW)
		{
			if(mat[r][c] == 'X')
				x_chance++;
			else if(mat[r][c] == 'O')
				o_chance++;
			else if(mat[r][c] == 'T')
				t_chance++;
			r++;
			c--;
		}

		if((x_chance + t_chance) == 4)
		{
			outfile<<"X won";
		}
		else if((o_chance + t_chance) == 4)
		{
			outfile<<"O won";
		}
		else if(empty_cell == false)
		{
			outfile<<"Draw";
		}
		else
		{
			outfile<<"Game has not completed";
		}
}

int main()
{
	int numT;
	
	infile>>numT;
	
	int i = 1;
	while(true)
	{
		for (int r = 0; r < ROW; r++)
			for (int c = 0; c < COL; c++)
				infile >> mat[r][c];

		if(infile.eof())
			break;

		outfile << "Case #" << i++ << ": ";
		checkMat();
		outfile << endl;
	}

	return 0;
}
