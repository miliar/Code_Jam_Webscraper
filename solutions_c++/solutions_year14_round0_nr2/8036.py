#include <iostream>
#include <cstdio>

using namespace std;

int main(void)
{
	int test_size;
	double c, f, x, time = 0, rate = 2, cookies = 0;
	cin >> test_size;

	for(int counter = 1; counter <= test_size; counter++)
	{
		time = 0;
		cookies = 0;
		rate = 2;
		cin >> c >> f >> x;
		if( c >= x )
		{
			time = x / rate;
		}
		else
		{
			for(cookies = 0; cookies < x;)
			{
				if(cookies >= c)
				{
					if( (x - cookies) / rate <= (x - cookies + c) / (rate + f) )
					{
						time += (x - cookies) / rate;
						cookies = x;
					}
					else
					{
						cookies -= c;
						rate += f;
					}
				}
				else
				{
					time += (c - cookies) / rate;
					cookies = c;
				}
			}
		}
		//cout << "Case #" << counter << ": " << time << endl;
		printf("Case #%d: %.7f\n", counter, time);
	}
	return 0;
}
