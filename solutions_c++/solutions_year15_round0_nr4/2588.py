#include <iostream>
#include <fstream>

using namespace std;

int main()
{	

	fstream file;
	file.open("D-small-attempt3.in");
	
	fstream fout;	
	fout.open ("output.txt" , ios::out);

	int R = 0;
	int C = 0;
	int X = 0;
	int length;

	file >> length;

	for ( int i = 1; i < length+1; i++ )
	{
		file >> X;
		file >> R;
		file >> C;

		if ( !(X == 4 && R*C == 8) )
		{
			if ( (R*C > X && X > 2) || (R*C >= X && X <= 2) )
			{
				int remaining = R*C;
				while ( remaining != 0 )
				{
					remaining -= X;
					if ( remaining < 0 )
					{
						break;
					}
				}
				if ( remaining < 0 )
				{
					fout << "Case #" << i << ": " << "RICHARD\n";
				}
				else
				{
					fout << "Case #" << i << ": " << "GABRIEL\n";
				}
			}
			else
			{
				fout << "Case #" << i << ": " << "RICHARD\n";
			}
		}
		else
		{
			fout << "Case #" << i << ": " << "RICHARD\n";
		}
	}

	file.close();

}