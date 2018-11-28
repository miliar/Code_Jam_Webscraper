#include <iostream>
#include <conio.h>
#include <fstream>
#define SIZE 4
int main()
{
	char a[SIZE][SIZE] = {0};
	int T, x = 0, i, j, count = 0; 
	std::ifstream in;
	std::ofstream out;
	in.open("A-small-attempt0.in");
	out.open("A-small-attempt0.out");
	if(in.is_open() && out.is_open())
	{
		in>>T;
			while(T--)
			{
				x = 0;
				count++;
	for(i = 0; i < SIZE; i++)
		for(j = 0; j < SIZE; j++)
			in>>a[i][j];
	//in>>c;
	
	for(i = 0; i < SIZE; i++)
	{
		for(j = 0; j < SIZE; j++)
			{
				if(a[i][j] == 'X' || a[i][j] == 'T')
					continue;
				else
					break;
			}
		if(j == SIZE)
		{
			out<<"Case #"<<count<<": X won"<<"\n";
			x = 1;
			break;
		}
	}

	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			for(j = 0; j < SIZE; j++)
				{
					if(a[j][i] == 'X' || a[j][i] == 'T')
						continue;
					else
						break;
				}
			if(j == SIZE)
			{
				out<<"Case #"<<count<<": X won"<<"\n";
				x = 1;
				break;
			}
		}
	}

	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			if(a[i][i] == 'X' || a[i][i] == 'T')
				continue;
			else
				break;
		}
		if(i == SIZE)
		{
			out<<"Case #"<<count<<": X won"<<"\n";
			x = 1;
		}
	}

	if(x == 0)
	{
		for(i = 0, j = SIZE-1; i <SIZE && j > -1; i++, j--)
		{
			if(a[i][j] == 'X' || a[i][j] == 'T')
				continue;
			else
				break;
		}
		if(j == -1)
		{
			out<<"Case #"<<count<<": X won"<<"\n";
			x = 1;
		}
	}

	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			for(j = 0; j < SIZE; j++)
				{
					if(a[i][j] == 'O' || a[i][j] == 'T')
						continue;
					else
						break;
				}
			if(j == SIZE)
			{
				out<<"Case #"<<count<<": O won"<<"\n";
				x = 1;
				break;
			}
		}
	}
	
	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			for(j = 0; j < SIZE; j++)
				{
					if(a[j][i] == 'O' || a[j][i] == 'T')
						continue;
					else
						break;
				}
			if(j == SIZE)
			{
				out<<"Case #"<<count<<": O won"<<"\n";
				x = 1;
				break;
			}
		}
	}

	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			if(a[i][i] == 'O' || a[i][i] == 'T')
				continue;
			else
				break;
		}
		if(i == SIZE)
		{
			out<<"Case #"<<count<<": O won"<<"\n";
			x = 1;
		}
	}

	if(x == 0)
	{
		for(i = 0, j = SIZE-1; i < SIZE && j > -1; i++, j--)
		{
			if(a[i][j] == 'O' || a[i][j] == 'T')
				continue;
			else
				break;
		}
		if(j == -1)
		{
			out<<"Case #"<<count<<": O won"<<"\n";
			x = 1;
		}
	}

	if(x == 0)
	{
		for(i = 0; i < SIZE; i++)
		{
			for(j = 0; j < SIZE; j++)
			{
				if(a[i][j] == '.')
					break;
				else
					continue;
			}
			
		}
		if(i == SIZE && j == SIZE)
			out<<"Case #"<<count<<": Draw"<<"\n";
		else
			out<<"Case #"<<count<<": Game has not completed"<<"\n";
	}
	
	}
	}

	getch();
}

