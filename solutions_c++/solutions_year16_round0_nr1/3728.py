#include <fstream>
#include <iostream>
using namespace std;

int main()
{
	int t;

	cin >> t;

	long long n, temp;

	bool digits[10];

	fstream fout;
	fout.open("a_output.out", ios::out);

	bool done;

	for(int i=1; i<=t; i++)
	{
		cin >> n;

		if(n == 0)
		{
			fout << "Case #" << i << ": INSOMNIA" << endl;
		}
		else
		{
			//initialise
			done = false;
			for(int j=0; j<10; j++)
			{
				digits[j] = false;
			}		

			//run through counter
			for(int j=1; true; j++)
			{
				temp = j*n;
				while(temp > 0)
				{
					digits[temp % 10] = true;
					temp/=10;
				}		
				//assume done
				done = true;
				for(int k=0; k<10; k++)
				{
					if(!digits[k])
					{
						done = false;
						break;
					}
				}		
				if(done)
				{
					fout << "Case #" << i << ": " << j*n << endl;
					break;
				}
			}
		}
	}
	return 0;
}
