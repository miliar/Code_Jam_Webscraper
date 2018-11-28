#include<iostream>
using namespace std;

int arr[10];

void seen(int n)
{
	while(n != 0)
	{
		int temp = n % 10;
		n = n / 10;
		arr[temp] = 1;
	}
}

bool all_seen()
{
	for(int i = 0; i < 10; i++)
	{
		if(arr[i] == 0)
		{
			return false;
		}
	}
	return true;
}

int main()
{
	int tc;
	int n;
	int orig ;
	cin >> tc;
	for(int t = 1; t<=tc; t++)
	{
		for(int i = 0; i < 10; i++)
			arr[i] = 0;
		cin >> n;
		orig = n;
		int count = 2;

		if(n == 0)
		{
			cout <<"Case #"<<t<<":"<<" "<<"INSOMNIA"<<endl;
		}
		else
		{
			while(1)
			{
				seen(n);
				if(all_seen())
				{
					cout <<"Case #"<<t<<":"<<" "<< n << endl;
					break;
				}
				n = count * orig;
				count++;
			}
		}
	}
	return 0;
}