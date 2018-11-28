#include <iostream>
#include <cstdlib>
#include <vector>
#include <string>

using namespace std;

int round(double x)
{
	if(x > (double) (int) x + 0.5) return ((int) x) + 1;
	else return (int) x;
}

int main()
{
	int testcases;
	cin >> testcases;

	for(int i = 0; i < testcases; i++)
	{
		int result = 0;
		int size;
		cin >> size;

		string temp1;
		string temp2;

		cin >> temp1 >> temp2;

		double ave = 0;
		int p1 = 0, p2 = 0;
		char c1 = temp1.at(0), c2 = temp2.at(0);
		do
		{
			if(c1 != c2)
			{
				result = -1;
				break;
			}

			char t1 = c1, t2 = c2;
			int a1 = 0, a2 = 0;

			while(t1 == c1)
			{
				p1++;
				a1++;
				if(p1 >= temp1.length())
				{
					c1 = 0;
					break;
				}
				c1 = temp1.at(p1);
			}
			
			while(t2 == c2)
			{
				p2++;
				a2++;
				if(p2 >= temp2.length())
				{
					c2 = 0;
					break;
				}
				c2 = temp2.at(p2);
			}

			if(a1 != a2) result += abs(a1 - a2);
		}
		while(c1 || c2);

		cout << "Case #" << i + 1 << ": ";
		if(result != -1) cout << result << endl;
		else cout << "Fegla Won" << endl;
	}
}