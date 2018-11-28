#include <fstream>
#include <iostream>

using namespace std;

int main()
{

	fstream fout;
	fout.open("c_output.out", ios::out);

	fout << "Case #1:" << endl;

	/*
	 * consider numbers of the form [x^31 + x^28] + [x^(r1+3) + x^r1] + [x^(r2+3) + x^r2] + [x^(r3+3) + x^r3] + [x + 1]
	 * x+ 1 is a factor
	 * there must be around 32*32*32/6 = 5400 such rs, and even with all the numbers we can't really take we should be able to make 500
	 */

	int digits[35];

	for(int i=0; i<32; i++)
	{
		digits[i] = 0;
	}

	digits[0] = 1;
	digits[1] = 1;
	digits[31] = 1;
	digits[28] = 1;

	int count = 0;

	for(int r1=2; r1<28; r1++)
	{
		if(digits[r1]==1 || digits[r1+3]==1)
		{
			continue;
		}
		else
		{
			digits[r1] = 1;
			digits[r1+3] = 1;
		}

		for(int r2=r1+1; r2<28; r2++)
		{

			if(digits[r2]==1 || digits[r2+3]==1)
			{
				continue;
			}
			else
			{
				digits[r2] = 1;
				digits[r2+3] = 1;
			}

			for(int r3=r2+1; r3<28; r3++)
			{
				if(digits[r3]==1 || digits[r3+3]==1)
				{
					continue;
				}
				else
				{
					digits[r3] = 1;
					digits[r3+3] = 1;
					count ++;
					for(int i=31; i>=0; i--)
					{
						fout << digits[i];
					}
					for(int i=2; i<=10; i++)
					{
						fout << " " << i+1;
					}
					fout << endl;

					if(count == 500)
					{
						return 0;
					}
					//done, now restore digits
					digits[r3] = 0;
					digits[r3+3] = 0;
				}
			}

			//done, now restore digits
			digits[r2] = 0;
			digits[r2+3] = 0;
		}

		//done, now restore digits
		digits[r1] = 0;
		digits[r1+3] = 0;
	}

	return 0;
	 
}

