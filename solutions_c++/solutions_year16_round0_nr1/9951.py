#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream fin;
	fin.open("A-large.in");
	ofstream fout;
	fout.open("output.txt");
	int digits[10] = { 0 };
	int z = 0;
	int n = 0;
	fin >> n;
	int temp = 9;
	int temp2;
	int l_digit = 0;
	int counter=0;
	int mul = 1;
	for (int i = 0; i < n;i++)
	{   
		mul = 1;
		fin >> z;
		temp = z;
		do
			{
				
				temp = z * mul;
				temp2 = temp;
				if (z != 0)
				{
					counter = 0;
					while (temp > 0)
					{

						l_digit = temp % 10;
						digits[l_digit] = -1;
						temp = temp / 10;
					}
					for (int j = 0; j < 10; j++)
					{
						if (digits[j] == -1)
							counter++;
					}
					mul++;
				}
		} while (counter != 10 && z != 0);
		if (counter == 10)
		{
			if(i==0)
			fout <<"Case #" << i + 1 << ": " << temp2 ;
			else
				fout <<endl<<"Case #" << i + 1 << ": " << temp2 ;
		}
		else if (z == 0)
		{
			if(i==0)
			fout <<"Case #" << i + 1 << ": " << "INSOMNIA";
			else
				fout <<endl<< "Case #" << i + 1 << ": " << "INSOMNIA" ;
		}
			for (int z = 0; z < 10; z++)
				digits[z] = 0;
	}

	return 0;
}