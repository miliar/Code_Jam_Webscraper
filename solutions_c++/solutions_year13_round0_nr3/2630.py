#include <iostream>
#include <cmath>
using namespace std;

bool IsPalin(unsigned long long val)
{
	unsigned long long rev = 0;
	unsigned long long actualval = val;

	while(val > 0)
	{
		rev = (rev * 10) + (val % 10);
		val /= 10;
	}

	if(actualval == rev)
		return true;
	else
		return false;
}

int main()
{
	int t;
	unsigned long long a;
	unsigned long long b;
	unsigned long long start;
	unsigned long long palincount;
	
	cin >> t;

	for(int i = 0; i < t; i++)
	{
		palincount = 0;

		cin >> a >> b;

		start = sqrt((long double)a);

		if(start * start < a)
			start++;

		for(unsigned long long j = start; j * j <= b; j++)
		{
			if(IsPalin(j) && IsPalin(j * j))
				palincount++;
		}

		cout << "Case #" << i + 1 << ": " << palincount << endl;
	}

	return 0;
}