#include <iostream>
#include <string>
#include <fstream>

using namespace std;

void main()
{
	int T, X,R,C;
	bool B;

	ifstream in;
	ofstream out;
	in.open("D-small-attempt3.in");
	out.open("D-s.out");

	in >> T;

	for (int i = 0; i < T; i++)
	{
		in >> X >> R >> C;
		if (X == 1)
		{
			B = 1;
		}
		else if ((X>R) && (X>C))
		{
			B = 0;
		}
		else if (X == 2)
		{
			if (((R*C) % 2)==0)
			{
				B = 1;
			}
			else
			{
				B = 0;
			}
		}
		else if (X == 3)
		{
			if ((((R*C) % 3) == 0) && ((R != 1) && (C!=1)))
			{
				B = 1;
			}
			else
			{
				B = 0;
			}
		}
		else if (X == 4)
		{
			if ((R < 3) || (C < 3))
			{
				B = 0;
			}
			else
			{
				B = 1;
			}
		}
		out << "Case #" << i + 1 << ": ";
		if (B == 0)
		{
			out << "RICHARD" << endl;
		}
		else
		{
			out << "GABRIEL" << endl;
		}
	}

	in.close();
	out.close();
}