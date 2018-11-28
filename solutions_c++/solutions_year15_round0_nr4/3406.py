#include<iostream>
#include<string>
using namespace std;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t, x, r, c, f,max,min;

	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		f = 1;
		cin >> x >> r >> c;
		if(r > c)
		{
			max = r;
			min = c;
		}
		else
		{
			max = c;
			min = r;
		}
		if((r*c) % x)
		{
			f = 0;
		}
		else if(ceil(x / 2.0) > max || ceil(x / 2.0) > min ||x>max||x>=7||x-1>min)
		{
			f = 0;

		}

		if(f == 0)
		{
			cout << "Case #" << i << ": RICHARD" << endl;
		}
		else
		
			{
				cout << "Case #" << i << ": GABRIEL" << endl;
			}
		
		

	}





	return 0;
}
