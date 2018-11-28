#include <iostream>
using namespace std;

int main() {
	// your code goes here
	int testcase;
	cin >> testcase;
	for (int test = 1; test <= testcase; test ++)
	{
		int n;
		cin >> n;
		if (n == 0)
		{
			cout << "Case #"<<test<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			bool check[10];
			int count = 0;
			for (int q = 0; q <= 9; q++) check[q] = false;
			int q = 1;
			do
			{
				int temp = n * q;
				while (temp > 0)
				{
					int unit = temp %10;
					if(check[unit] == false)
					{
						check[unit] = true;
						count++;
						if (count == 10)
							break;
					}
					temp = temp /10;
				}
				if (count == 10)
				{
					cout << "Case #"<<test<<": "<<(q*n)<<endl;
					break;
				}
				q++;
			} while (count < 10);
		}
	}
	return 0;
}