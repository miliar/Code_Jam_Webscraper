#include <iostream>

using namespace std;

int main(void)
{
	int N, in;
	long long num, inc;
	bool complete;

	while(cin >> N)
	{
		in = 0;
		while(in++ < N)
		{
			cout << "Case #" << in << ": ";

			cin >> inc; 

			if(inc == 0)
			{
				cout << "INSOMNIA" << endl;
				continue;
			}

			complete = false;
			char digits[10] = {0};
			num = 0;
			while(!complete)
			{
				num += inc;
				long long tmp = num, divisor;
				int digit;
				while(tmp)
				{
					divisor = tmp / 10;
					digit = tmp - divisor * 10;
					tmp = divisor;
					digits[digit] = 1;
				}

				complete = digits[0] && digits[1] && digits[2] && digits[3] && digits[4] 
						&& digits[5] && digits[6] && digits[7] && digits[8] && digits[9];
			}

			cout << num << endl;
		}
	}

	return 0;
}