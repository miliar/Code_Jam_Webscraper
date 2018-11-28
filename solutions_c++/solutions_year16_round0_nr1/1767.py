#include <fstream>
#include <iostream>

using namespace std;

int main()
{
	ifstream input;
	ofstream output;
	
	input.open("A-large.in");
	output.open("output.txt");
	
	int T;
	long long int N, n, temp;
	input >> T;
	
	for(int t = 1; t <= T; t++)
	{
		output << "Case #" << t << ": ";
		input >> N;
		if(N == 0)
		{
			output << "INSOMNIA" << endl;
		}
		else
		{
			bool digits[10];
			n = 0;
			for(int d = 0; d < 10; d++)
			{
				digits[d] = false;
			}
			while(!(digits[0]&&digits[1]&&digits[2]&&digits[3]&&digits[4]&&digits[5]&&digits[6]&&digits[7]&&digits[8]&&digits[9]))
			{
				n += N;
				temp = n;
				while(temp > 0)
				{
					digits[temp%10] = true;
					temp /= 10;
				}
			}
			output << n << endl;
		}
	}
	return 0;
}
