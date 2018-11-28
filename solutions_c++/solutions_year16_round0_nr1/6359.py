#include<bits/stdc++.h>

using namespace std;

bool arr[10] = {0};
int count_digit;

int sum(int n)
{
	int i = 2;
	int temp = n;
	int tempo;
	while(count_digit<10)
	{
		tempo = temp;
		while(temp != 0)
		{
			int r = temp % 10;
			if(!arr[r])
			{
				arr[r] = true;
				count_digit++;
				if(count_digit == 10)
				{
					return tempo;
				}
			}
			temp/=10;
		}
		temp=n*i;
		i++;
	}
	return tempo;
}

int main() {
	int t,n;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
		memset(&arr, 0, sizeof(arr));
		count_digit = 0;
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
		}
		else
		{
			cout<<"Case #"<<i<<": "<<sum(n)<<endl;
		}
	}
	return 0;
}
