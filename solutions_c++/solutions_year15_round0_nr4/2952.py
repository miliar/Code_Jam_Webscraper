#include<iostream>
using namespace std;
#include<fstream>
//
void combinations()
{



}
int main()
{
	fstream file;
	
	file.open("D-small-attempt5.in");
	int test;
	file >> test;

	int R=0;
	int C = 0;
		int X = 0;
	

	int	count = 1;
	fstream fout;

	fout.open("output.txt", ios::out);

	while (count <= test){

		file >> X;
		file >> R;
		file >> C;
		int remain = R*C;

		if ((X == 4 && R*C == 8))
		{
			fout << "Case #" << count << ": RICHARD" << endl;
		}
		else
		{
			if ((R*C > X && X > 2) || (R*C >= X && X <= 2))
			{
				while (remain != 0)
				{
					remain -= X;

					if (remain <= 0)
					{
						break;
					}
				}
				if (remain < 0)
				{
					fout << "Case #" << count << ": RICHARD" << endl;
				}
				else
				{
					fout << "Case #" << count << ": GABRIEL" << endl;
				}


			}
			else
			{
				fout << "Case #" << count << ": RICHARD" << endl;
			}
		}

		count++;
	}

}