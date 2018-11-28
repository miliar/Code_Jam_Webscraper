#include <iostream>
#include <fstream>
#include <string.h>

#define ll long long
using namespace std;

ll counting_sheep(ll n)
{
	int count[10];
	int remain = 10;
	memset(count, 0, sizeof(count));
	ll cur;
	int i = 1;
	while (remain > 0)
	{
		cur = n*i;
		i++;
		while (cur)
		{
			if (count[cur % 10] == 0)
			{
				count[cur % 10]--;
				remain--;
				if (remain == 0)
					break;
			}
			cur /= 10;
		}
	}
	return n*(i - 1);
};

int main(void)
{
	fstream input, output;
	input.open("A-large.in", ios::in);
	output.open("output.txt", ios::out);
	int t;
	input >> t;
	int i = 1;
	while (t--)
	{
		ll num;
		input >> num;
		if (num == 0)
			output <<"Case #"<<i<<": "<< "INSOMNIA" << endl;
		else
			output << "Case #" << i << ": " << counting_sheep(num) << endl;
		i++;
	}

	return 0;
}