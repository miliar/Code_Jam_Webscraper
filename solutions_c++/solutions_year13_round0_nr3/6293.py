#include <iostream>
#include <math.h>
#include <sstream>
#include <fstream>

bool IsFair(int n)
{
	char* sre = new char[64];
	itoa(n,sre,10);
	int size = strlen(sre);
	bool isfair = true;
	for(int offset = 0;offset < size;offset++)
	{
		isfair = (sre[offset] == sre[size-(offset+1)]);
		if(!isfair)
			break;
	}
	delete[] sre;
	return isfair;
}
bool IsSquare(int n)
{
	double square_root = sqrt(double(n));
	if(square_root != double(int(square_root)))
		return false;
	return IsFair(int(square_root));
}

#define IsSF(a) IsFair(a) && IsSquare(a)

std::string glue(int _case, int value)
{
	std::stringstream ss;
	ss << "Case #" << _case << ": " << value;
	return ss.str();
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
		std::string min,max;
		a = '\0';
		while(a != ' ')
		{
			file.read(&a,1);
			if(a != ' ')
				min.push_back(a);
		}
		while(a != '\n')
		{
			file.read(&a,1);
			if(a != '\n')
				max.push_back(a);
		}
		int imin,imax;
		imin = toint(min);
		imax = toint(max);
		int totalfs = 0;
		for(int current = imin;current <= imax;current++)
		{
			if(IsSF(current) == true)
				totalfs++;
		}
		output << glue(cycle+1,totalfs) << "\n";
	}
	output.close();
		
}



int main()
{
	solve();
	std::cin.get();
}