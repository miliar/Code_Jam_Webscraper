#include <iostream>
#include <math.h>
#include <sstream>
#include <fstream>

char Board[4][4];

std::string glue(int _case, std::string value)
{
	std::stringstream ss;
	ss << "Case #" << _case << ": " << value;
	return ss.str();
}

bool EmptySpaces()
{
	bool es = false;
	for(int x = 0;x < 4;x++)
	{
		for(int y = 0;y < 4;y++)
		{
			es = (Board[x][y] == '.');
			if(es)
				break;
		}
		if(es)
			break;
	}
	return es;
}

bool CheckIf4(char c)
{
	bool e = true;
	for(int X = 0;X < 4;X++)
	{
		e = true;
		for(int Y = 0;Y < 4;Y++)
		{
			if (Board[X][Y] != c && Board[X][Y] != 'T')
			{
				e = false;
				break;
			}
		}
		if(e)
			return true;
	}
	e = true;
	for(int Y = 0;Y < 4;Y++)
	{
		e = true;
		for(int X = 0;X < 4;X++)
		{
			if (Board[X][Y] != c && Board[X][Y] != 'T')
			{
				e = false;
				break;
			}
		}
		if(e)
			return true;
	}
	e = true;
	for(int XY = 0;XY < 4;XY++)
	{
		if(Board[XY][XY] != c && Board[XY][XY] != 'T')
		{
			e = false;
			break;
		}
	}
	if(e)
		return true;
	e = true;
	for(int XY = 3;XY >= 0;XY--)
	{
		if(Board[XY][XY] != c && Board[XY][XY] != 'T')
		{
			e = false;
			break;
		}
	}
	if(e)
		return true;
	return false;
}



std::string Status()
{
	if(CheckIf4('O'))
		return "O won";
	else if(CheckIf4('X'))
		return "X won";
	else if(EmptySpaces())
		return "Game has not completed";
	else
		return "Draw";
}


int toint(std::string a)
{
	return atoi(a.c_str());
}

void solve()
{
	std::ifstream file;
	std::ofstream output;
	file.open("sa.in",std::ios::binary);
	output.open("output.txt");
	std::string T;
	char a = '\0';
	while(a != '\n')
	{
		file.read(&a,1);
		if(a != '\n')
			T.push_back(a);
	}
	int Lines = toint(T);
	for(int cycle = 0;cycle < Lines;cycle++)
	{
		a = '\0';
		for(int rows = 0;rows < 4;rows++)
		{
			a = '\0';
			int Count = 0;
			while(a != '\n')
			{
				file.read(&a,1);
				if(a != '\n')
				{
					Board[Count][rows] = a;
					Count ++;
				}
			}

		}
		for(int Y = 0;Y < 4;Y++)
			{
				for(int X = 0;X < 4;X++)
				{
					std::cout << Board[X][Y];
				}
				std::cout << "\n";
			}
		//std::cin.get();
		file.read(&a,1);
		a = '\0';
		output << glue(cycle+1,Status()) << "\n";

					


	}
	output.close();
}

int main()
{
	solve();
}
		