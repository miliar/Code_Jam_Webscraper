#include <bits/stdc++.h>
using namespace std;
int main()
{
	int test, TEST=1;
	cin>>test;

	while(test--)
	{
		int arr[10] = {0};
		long long int num;
		cin>>num;

		if(num==0)
		{
			cout<<"Case #" << TEST << ": " <<"INSOMNIA"<<endl;
		}
		else
		{
			int m=1, flag=1;
			while(1)
			{
				long long int tmp = num * m;
				while(tmp)
				{
					int digit = tmp%10;
					tmp /=10;
					arr[digit] ++;
				}
				flag=1;
				for(int i=0; i<10; i++)
				{
					if(arr[i]==0)
					{
						flag=0;
						break;
					}
				}
				if(flag==1)
				{
					cout<<"Case #" << TEST << ": " << num*m<<endl;
					break;
				}
				else
				{
					m++;
				}
			}
		}
		TEST++;
	}
	return 0;
}