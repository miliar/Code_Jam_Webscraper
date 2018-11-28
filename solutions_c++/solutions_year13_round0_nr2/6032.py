#include <iostream>
#include <math.h>
#include <sstream>
#include <fstream>

int Lawn[100][100];


std::string glue(int _case, std::string value)
{
	std::stringstream ss;
	ss << "Case #" << _case << ": " << value;
	return ss.str();
}

int toint(std::string a)
{
	return atoi(a.c_str());
}

std::string possible(int a,int b)
{
	for(int c = 0;c < a;c++)
	{
		for(int d = 0;d < b;d++)
		{
			std::cout << Lawn[c][d] << " ";
		}
		std::cout << "\n";
	}
	for(int x = 0;x < a;x ++)
	{
		for(int y = 0;y < b;y ++)
		{
			//(bigger numbers can't be in a line that has 2 smaller numbers)
			//horizontal 
			int rc = Lawn[x][y];
			for(int xx = 0;xx < a;xx++)
			{
				if(Lawn[xx][y] < rc)
				{
					//vertical from here
					for(int yy = 0;yy < b;yy++)
					{
						if(Lawn[xx][yy] > Lawn[xx][y])
							return "NO";

					}
				}
			}
			//vertical
			for(int yy = 0;yy < b;yy ++)
			{
				if(Lawn[x][yy] < rc)
				{
					//horizontal from here
					for(int xx = 0;xx < a;xx++)
					{
						if(Lawn[xx][yy] > Lawn[x][yy])
							return "NO";

					}
				}
			}
			


				
		}
	}
	return "YES";
			
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
		int y,x;
		std::string sy,sx;
		a = '\0';
		while(a != ' ')
		{
			file.read(&a,1);
			if(a != ' ')
				sy.push_back(a);
		}
		while(a != '\n')
		{
			file.read(&a,1);
			if(a != '\n')
				sx.push_back(a);
		}
		x = toint(sx);
		y = toint(sy);
		for(int i = 0;i < y;i++)
		{
			for(int i2 = 0;i2 < x;i2++)
			{
				char cha;
				file.read(&cha,1);
				std::string scha;
				scha.push_back(cha);
				Lawn[i2][i] = toint(scha);
				file.read(&cha,1);
			}
		}

		//std::cin.get();
		output << glue(cycle+1,possible(x,y)) << "\n";

					


	}
	output.close();
}


int main()
{
	solve();


}