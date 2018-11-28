#include <iostream>
#include <cstring>
using namespace std;

int solve(int N)
{
	int left = 10;
	bool digit[10];
	memset(digit, true, 10);
	char temp[15];
	char tem;
	int i, j;
	int a;
	for(i = 1; ; i++)
	{
		_itoa_s(N * i, temp, 10);
		for (j = 0; temp[j] != '\0'; j++)
		{
			tem=temp[j];
			a = atoi(&tem);
			if(digit[a] == true)
			{
				digit[a] = false;
				left--;
				if(left==0)
				{
					break;
				}
			}
		}
		if(left==0)
		{
			break;
		}
	}
	return i*N;
}

int main()
{
	int T;
	cin>>T;
	int N;
	for(int t=0;t<T;t++)
	{
		cin>>N;
		if(N==0)
			cout<<"Case #"<<t + 1<<": INSOMNIA"<<endl;
		else
			cout<<"Case #"<<t + 1<<": "<<solve(N)<<endl;
	}

	system("pause");
	return 0;
}