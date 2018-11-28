#include <iostream>
#include <fstream>

using namespace std;
int main ()
{
	ifstream in ("A.in");
	ofstream out ("A.txt");
	
	int t;
	in >> t;
	
	for (int i = 0; i < t; i++)
	{
		int r1;
		int r2;
		in >> r1;
		
		int buf;
		int a[4];
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (j == r1-1)
				{
					in >> a[k];
				}
				else
				{
					in >> buf;
				}
			}
		}
		
		in >> r2;
		int b[4];
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (j == r2-1)
				{
					in >> b[k];
				}
				else
				{
					in >> buf;
				}
			}
		}
		
		int overlap = 0;
		int num = 0;
		
		for (int j = 0; j < 4; j++)
		{
			int cur = a[j];
			for (int k = 0; k < 4; k++)
			{
				if (b[k] == cur)
				{
					overlap++;
					num = cur;
				}
			}
		}
		
		out << "Case #" << (i+1) << ": ";
		if (overlap == 1)
		{
			out << num;
		}
		else if (overlap == 0)
		{
			out << "Volunteer cheated!";
		}
		else
		{
			out << "Bad magician!";
		}
		
		if (i < t-1)
		{
			out << endl;
		}
	}
}
