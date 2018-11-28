#include<iostream>
using namespace std;

int main()
{
	int testCases;
	cin >> testCases;
	for (int i = 0; i < testCases; i++)
	{
		long int n;
		cin >> n;
		if (n == 0)
		{
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		
		int array[10] = {0}, count = 0, j = 2;
		long int temp= n;
		while(count < 10)
		{
			long int x = n;
			while(x > 0)
			{
				int y = x%10;
				if(array[y] == 0)
				{
					array[y] = 1;
					count++;
					if(count==10)
						break;
				}
				x = x/10;				
			}
			if(count >= 10)
				break;
			n = j *temp;
			j++;
		}
		cout << "Case #" << i+1 << ": " << n << endl;
	}
}
