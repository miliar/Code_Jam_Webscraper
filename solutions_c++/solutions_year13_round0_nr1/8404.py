/* Author:
 * d4n1l0d
 *
 * E-mail:
 * danilod100 at gmail.com
 * 04/13/2013 00:30:00
 * */

#include <iostream>

using namespace std;



int main(void)
{

	int totalcases;
	int casenum = 1;
	
	cin >> totalcases;

	while(totalcases > 0)
	{

		bool winner = false,emptyspace = false;

		char tmp;
		int r,c;

		char lastelem;
		char mat[4][4];

		//read data
		for(r = 0; r < 4; r++)
			for(c = 0; c < 4; c++)
				cin >> mat[r][c];


		//lines
		r = c = 0;
		while( !winner && r < 4)
		{
			lastelem = mat[r][0];
			if(lastelem != '.')
			{
				winner = true;
				for(c = 1; c < 4; c++)
				{
					if(mat[r][c] == 'T')
						continue;
					if(mat[r][c] == '.')
						emptyspace = true;
					if(mat[r][c] != lastelem)
					{
						winner = false;
						break;
					}
				}
				
			} else 
			{
				emptyspace = true;
			}
			
			r++;
		}
				
		//col
		c = 0;
		while (!winner && c < 4)
		{
			lastelem = mat[0][c];
			if(lastelem != '.')
			{
				winner = true;
				
				for(r = 1; r < 4; r++)
				{
				
					if(mat[r][c] == 'T')
						continue;
					if(mat[r][c] == '.')
						emptyspace = true;
					if(mat[r][c] != lastelem)
					{
						winner = false;
						break;
					} 
				}
			} else 
			{
				emptyspace = true;
			}
				
			c++;
		}

		//diag1
		if(!winner)
		{
			lastelem = mat[0][0];
			if(lastelem != '.')	
			{
				winner = true;
				for(c =1; c < 4; c++)
				{

					if(mat[c][c] == 'T')
						continue;
					if(mat[c][c] == '.')
						emptyspace = true;
					if(mat[c][c] != lastelem)
					{
						winner = false;
						break;
					}
				}
	
			} else 
			{
				emptyspace = true;
			}
		}

		//diag2
		if(!winner)
		{
			lastelem = mat[0][3];
			if(lastelem != '.')
			{
				winner = true;
				for(c =1; c < 4; c++)
				{
	
					if(mat[c][3-c] == 'T')
						continue;
					if(mat[c][3-c] == '.')
						emptyspace = true;
					if(mat[c][3-c] != lastelem)
					{
						winner = false;
						break;
					}
				}
			} else 
			{
				emptyspace = true;
			}
		}
		//results
		cout << "Case #" << casenum << ": ";
		if(!winner)
		{
			if(emptyspace)
				cout << "Game has not completed";
			else
				cout << "Draw";
		} else
			cout << lastelem  <<" won";

		cout << endl;

		//go to next case
		totalcases--;
		casenum++;	

	}

	return 0;
}

