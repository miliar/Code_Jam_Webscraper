#include <iostream>
using namespace std;
bool arr[10];
int main()
{
	unsigned int long long T, i, number, j, val, temp, k, count, lastseen, flag, rem;
	cin>>T;
	for(i=0;i<T;i++)
	{		
		cin>>number;
		lastseen = number;
		count = 0;
		flag = 0;
		for(k=0;k<10;k++)
			arr[k] = 0;
		if(number == 0)
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		else
		{
			for(j=1; j<=1000000;j++)
			{
				val = number * j;
				temp = val;
				while(temp>0)
				{
					rem = temp % 10;
					if(arr[rem] == 0)
					{
						count++;
						arr[rem] = 1;
					}
					temp = temp/10;
				}
				if(count == 10)
				{
					lastseen = val;
					flag = 1;
					break;
				}
			}
			if(flag == 1)
				cout << "Case #" << i+1 << ": " << lastseen << endl;
			else
				cout << "Case #" << i+1 << ": INSOMNIA" << endl;
		}
	}
}