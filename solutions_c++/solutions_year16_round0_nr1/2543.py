#include <iostream>
#include <cstdio>

using namespace std;

int digits[10];
int countD;

void getDigits(long long int num)
{
	while(num > 0)
	{
		int dig = num%10;
		num/=10;
		if(digits[dig] == 0)
			countD++, digits[dig]++;
	}
}


int main()
{
	int t; cin >> t;
	for(int i=1;i<=t;i++)
	{
		cout << "Case #" << i << ": ";

		countD = 0; long long int num, val; cin >> val;
		fill(digits, digits+10, 0); num = val;

		if(val == 0)
		{
			cout << "INSOMNIA" << endl;
			continue;
		}

		while(true)
		{
			getDigits(num);
			if(countD == 10)
				break;
			num += val;
		}
		cout << num << endl;
	}
	return 0;
}