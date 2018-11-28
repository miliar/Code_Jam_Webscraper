#include<iostream>
using namespace std;
int main()
{
//	freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);
	long long values[10];
	long long  a,value,value1;
	long long t,i,j,k;
	cin >> t;
	i = 1;
	while (t--)
	{
		
		cin >> a;
		for (j = 0; j < 10; j++)
			values[j] = 0;
		j = 1;
		while (1)
		{
			if (a == 0)
			{
				cout << "Case #" << i << ": " << "INSOMNIA" << endl;
				break;
			}
			value = j*a;
			while(value!=0)
			{
				value1 = value % 10;
				value /= 10;
				values[value1 ] = 1;
			}
			value1 = 0;
			for (k=0; k < 10; k++)
			{
				if (values[k] == 0)
				{
					value1 = 1;
					break;
				}
			}
			if (value1 == 0)
			{
				cout << "Case #" << i << ": " << j*a << endl;
				break;
			}
			j++;

		}
		i++;
	}
}