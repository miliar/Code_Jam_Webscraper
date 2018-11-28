#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	
	ofstream write;
	write.open("out.expect");
	int arr[10];
	int T, count,x,a,tmp,save;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> a;
		count = 0;
		save = a;
		if (a == 0)
		{
			write << "Case #" << i + 1 << ": INSOMNIA" << endl;
			cout << "Case #" << i + 1 << ": INSOMNIA" << endl;
			continue;
		}
		for (int j = 0; j < 10; j++)
		{
			arr[j] = -1;
		}
		while (count != 10)
		{
			x = 0;
			tmp = a;
			while (tmp/10 !=0)
			{
				if (arr[tmp%10] != 1)
				{
					count++;
					arr[tmp%10] = 1;
				}
				tmp = tmp / 10;
			}
			if (arr[tmp % 10] != 1)
			{
				count++;
				arr[tmp % 10] = 1;
			}
			if (count == 10)
			{
				break;
			}
			a += save;
		}
		cout << "Case #" << i + 1 << ": " << a << endl;
		write << "Case #" << i + 1 << ": " << a << endl;
	}
	return 0;
}