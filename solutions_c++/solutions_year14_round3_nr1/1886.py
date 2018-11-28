#include <iostream>
#include <fstream>
using namespace std;

void minimize(int &x, int &y)
{
	for (int i = 2; i <= x; i++)
		if(x%i == 0 & y %i==0)
		{
			x = x/i;
			y = y/i;
			i = 2;
		}
}

int Solve(int x, int y)
{
	if (x == y)
		return 1;
	int yt = y;
	{
		while (yt > 1)
		{
			if (yt %2 != 0)
				return -1;
			yt/=2;
		}
	}
	int i = 1;
	while (1 <= 40)
	{
		y /= 2;
		if (x >= y)
			return i;
		i++;
		
	}
	return -1;

}
void main()
{
	int nTest;
	fstream f, f2;
	f.open("A-small-attempt2.in", ios:: in);
	f2.open("output.txt", ios::out);
	f >> nTest;
	for(int i = 0; i<nTest; i++)
	{
		int x, y;
		char temp;
		f >> x;
		f >> temp;
		f >> y;
		minimize(x, y);
		int result = Solve(x, y);
		if (result == -1)
			f2 << "Case #" << i+1 << ": impossible\n";
		else
			f2 << "Case #" << i+1 << ": " << result<< endl;	
	}
}