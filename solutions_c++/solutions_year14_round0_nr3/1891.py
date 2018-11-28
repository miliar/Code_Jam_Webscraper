#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdlib>
#include <vector>
#include <cmath>
#include <functional>
#include <numeric>
#include <iomanip>
using namespace std;


void init_grid (const int R, const int C , vector<vector<char> > & grid)
{
	grid.reserve(R);
	for(int i = 0; i < R; i++)
	{
		grid[i].reserve(C);
		for(int j = 0; j < C ; j++)
		{
			grid[i][j] = '.';
		}
	}
}

bool hack_solution(const int R, const int C, const int M , 
		vector<vector<char > > & grid)
{
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < C ; j++)
		{
			grid[i][j] = '*';
		}
	}


	for(int a = 0 ; a < 3 ; ++a)
	{
		for(int b = 0; b < 3; ++b)
		{
			grid[a][b] = '.';
		}
	}
	//	If R >= 4:
	if ( R >= 4)
	{
		grid[3][0] = '.';
		grid[3][1] = '.';
		grid[0][0] = 'c';
	}

	else
	{
		grid[0][3] = '.';
		grid[1][3] = '.';
		grid[0][0] = 'c';
	}

	return true;
}
//	One straight line.
bool single_solution(const int R, const int C, const int M , 
		vector<vector<char > > & grid)
{
	if( R == 1 ) 
	{
		if ( M < C - 1 )
		{
			for(int a = 0; a < M; ++a)
			{
				grid[0][a] = '*';
			}

			return true;
		}
		else
		{
			return false;
		}
	}

	else if( C == 1 ) 
	{
		if ( M < R - 1 )
		{
			for(int a = 0; a < M; ++a)
			{
				grid[a][0] = '*';
			}
			return true;
		}
		else
		{
			return false;
		}
	}
}


//	2 by X
bool double_solution(const int R, const int C, const int M , 
		vector<vector<char > > & grid)
{
	if(R == 2)
	{
		if(( M % 2 == 0) && (M != R * C - 2))
		{
			for(int a = 0; a < M / 2; ++a)
			{
				grid[0][a] = '*';
				grid[1][a] = '*';
			}
			return true;
		}
		else 
			return false;
	}


	else if (C == 2)
	{
		if(( M % 2 == 0) && (M != R * C - 2))
		{
			for(int a = 0; a < M / 2; ++a)
			{
				grid[a][0] = '*';
				grid[a][1] = '*';
			}
			return true;
		}
		return false;
	}
	else 
		return false;
}


bool simple_solution_cols(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	cout << "running  simple cols\n" << endl;;
	cout << R<< C << M << endl;;
	int a = 0; int b = 0; int mines  = 0;
	while( mines < M)
	{
		while(b < C && mines < M)
		{
			a = 0;
			while(a < R && mines < M)
			{
				grid[a][b] = '*';
				a++;
				mines++ ;
			}
			b++;
		}
	}
	return true;
}


bool simple_solution_rows(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	cout << "running  simple cols\n" << endl;;
	cout << R<< C << M << endl;;
	int a = 0; int b = 0; int mines  = 0;
	while( mines < M)
	{
		while(a < R && mines < M)
		{
			b = 0;
			while(b < C && mines < M)
			{
				grid[a][b] = '*';
				b++;
				mines++ ;
			}
			a++;
		}
	}
	return true;
}


bool complex_solution_cols(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	for (int a = 0; a < R; ++a)
	{
		for (int b = 0; b < C -2 ; ++b)
		{
			grid [ a][b] = '*';
		}
	}
	int mines_left = M - R * ( C - 2);
	int rows_left = mines_left / 2;

	for(int a = 0 ; a < rows_left; ++a)
	{
		grid [a][C-2 ] = '*';
		grid [a][C-1 ] = '*';
	}
	return true;
}
bool complex_solution_rows(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	for (int a = 0; a < R- 2; ++a)
	{
		for (int b = 0; b < C ; ++b)
		{
			grid [ a][b] = '*';
		}
	}
	int mines_left = M - (R-2) * C ;
	int cols_left = mines_left / 2;

	for(int a = 0 ; a < cols_left; ++a)
	{
		grid [R-1][a] = '*';
		grid [R-2][a] = '*';
	}
	return true;
}


bool double_simple_solution(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	cout << "double simple";
	int mines = 0;
	for(int a = 0; a < R - 2; a++)
	{
		for (int b = 0 ; b < C - 2; b++)
		{
			grid[a][b] = '*';
			mines ++;
			if(mines == M)
				return true;
		}
	}
}


bool check_multiples(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	int mines_left = R*C - M;
	for ( int it_r_m = 2; it_r_m <= R; ++it_r_m)
	{
		if ((mines_left % it_r_m == 0) && 
				(mines_left / it_r_m > 1) && 
				(mines_left / it_r_m <= C))
		{
			for (int a = 0; a < R; ++a)
			{
				for(int b = 0; b< C; ++b)
				{
					grid[a][b] = '*';
				}
			}
			for(int a = 0; a < it_r_m; ++a)
			{
				for (int b = 0; b < mines_left / it_r_m; ++b)
				{
					grid[R - 1 - a][C - 1 - b] = '.';
				}
			}
			grid [R-1][C-1] = 'c';
			return true;
		}
	}

	for ( int it_r_m = 2; it_r_m <= C; ++it_r_m)
	{
		if ((mines_left % it_r_m == 0) && 
				(mines_left / it_r_m > 1) && 
				(mines_left / it_r_m <= R))
		{
			for (int a = 0; a < R; ++a)
			{
				for(int b = 0; b< C; ++b)
				{
					grid[a][b] = '*';
				}
			}
			for(int a = 0; a < it_r_m; ++a)
			{
				for (int b = 0; b < mines_left / it_r_m; ++b)
				{
					grid[R - 1 - a][C - 1 - b] = '.';
				}
			}
			grid [R-1][C-1] = 'c';
			return true;
		}
	}
	return false;
}
bool complex_solution(const int R, const int C, const int M, 
		vector< vector<char > > & grid)
{
	if((R-2) * ( C - 2) >= M)
	{
		return double_simple_solution(R,C,M,grid);
	}
	else if(R * ( C -2 ) >= M  && ((M%R) != R-1))
	{
		return simple_solution_cols(R, C, M, grid);
	}
	else if ((R-2) * C >= M && ((M%C)!=C-1))
	{
		return simple_solution_rows(R, C, M, grid);
	}

	else if ( (M - R * (C-2)) % 2 == 0)
	{
		return complex_solution_cols(R,C,M,grid);
	}
	else if ( (M - (R-2 ) * C) % 2 == 0)
	{
		return complex_solution_rows(R,C,M,grid);
	}
	else 
	{
		return check_multiples(R,C,M,grid);
	}
	return false;
}

int main(int argc, char * argv[])
{
	ifstream fin("input.txt"); 
	ofstream fout("output.txt");
	
	if(!fin.good())
	{
		cout << "opps" << endl;
	}

	string str;
	getline(fin, str);
	
	//	Number of test cases.
	const int T = atoi(str.c_str());

	//	Loop across each file.
	for( int aaa = 0; aaa < T ; aaa++)
	{
		getline(fin, str);
		istringstream iss(str);

		//	 Data
		int R, C, M;
		iss >> R >> C >> M;

		//	Init the grid.
		vector< vector< char > > grid(R);
		init_grid(R, C, grid);

		bool possible = true;

		int mines_left = R*C - M;

		if (M == 0)
		{
			possible = true;
			grid[R-1][C-1] = 'c';
		}

		else if (M == R * C -1)
		{
			for(int i = 0; i < R; i++)
			{
				for(int j = 0; j < C ; j++)
				{
					grid[i][j] = '*';
				}
			}
			grid[R-1][C-1] = 'c';
		}

		else if( R == 1 || C == 1) 
		{
			possible = single_solution(R, C, M, grid);
			grid [R-1][C-1] = 'c';
		}
		 
		else if (mines_left < 4)
		{
			possible = false;
		}

		
		else if(R== 2 || C == 2)
		{
			possible = double_solution(R,C,M,grid);
			grid [R-1][C-1] = 'c';
		}

		else if(R * C - M == 11)
		{
			possible = hack_solution(R,C,M,grid);
		}
		else
		{
			possible = complex_solution(R,C,M,grid);
			grid [R-1][C-1] = 'c';
		}

		fout << "Case #" << aaa+1 << ":" << endl;
		if (possible)
		{
			for( int i = 0 ; i < R; ++i)
			{
				for(int j = 0; j < C; ++j)
				{
					fout << grid[i][j] ;
				}
				fout << endl;
			}
		}
		else
		{
			fout << "Impossible"<<endl;
		}






		//fout << "Case #" << aaa+1 << ": " << fin_ans << endl;
		//fout << fixed << setprecision(10) << "Case #" << aaa+1 << ": " << setprecision(10) << static_cast<double>(prob)<< setprecision(10) <<  endl;

	}	

	fin.close(); fout.close();
	return 0;
}
