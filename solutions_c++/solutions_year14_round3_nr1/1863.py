#include <iostream>
#include <cmath>
#include <iomanip>
#include <string>
#include <map>

using namespace std;

long long power(long long num, int times)
{
	long long temp = 1;
	for (int i = 1; i <= times; i++)
	{
		temp = temp *num;
	}
	return temp;
}

int main()
{
	freopen("output.txt", "w", stdout);
	//int a, b;
	int T;
	long long  P, Q;
	char sep;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		int count = 1;
		cin >> P >> sep >> Q;
		if (Q % 2)
		{
			cout << "Case #"<<i << ": impossible" << endl;
			continue;
		}
		int res = 0;
		bool first = true;
		while (count <= 40 && P!=0)
		{
			while ( P*power(2, count) >= Q  &&P != 0 )
			{
				if (first)
				{
					first = false;
					res = count;
				}
				if (Q % power(2, count) != 0)
				{
					P = P *power(2, count);
					Q = Q * power(2, count);
				}
				P = P - Q / power(2, count);
			}
			count++;
		}
		if (count > 40 || P != 0)
		{
			cout << "Case #" << i << ": impossible" << endl;
		}
		else
		{
			cout << "Case #" << i << ": " << res<< endl;
		}
		

	}
	
	
	return 0;
}