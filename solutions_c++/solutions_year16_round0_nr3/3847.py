#include <iostream>
#include <cmath>

using namespace std;

long baseconvert(int *arr,int size, int base)
{
	long value = 0;
	for(int i = 0; i < size; ++i)
	{
		value = value + arr[i]*pow(base,i);
	}
	return value;
}
void dectobin(int arr[], long num, int size)
{
	int i = 0;
	long x = 1;
	while(i < size)
	{
		if(num & x)
			arr[i] = 1;
		else 
			arr[i] = 0;
		i++;
		x*=2;
	}
}
long checkprime(long t)
{
	for(long i = 2; i < sqrt(t); ++i)
		if(t%i == 0)
			return i;
	return 0;
}

int main(int argc, char const *argv[])
{
	int t, j, arr[50],count,i,n;
	long temp, temp1,divisor[50];
	cin>>t;
	while(t--)
	{
		cin>>n>>j;
		long start = 1 + pow(2,n-1);
		count = 0;
		cout<<"Case #1:\n";
		while(count != j)
		{
			i = 0;
			dectobin(arr,start,n);
			while(i < 9)
			{
				temp = baseconvert(arr,n,i+2);
				temp1 = checkprime(temp);
				if(temp1!=0)
					divisor[i++] = temp1;
				else
					break;
			}
			if(i < 9)
				start = start + 2;
			else
			{
				count++;
				for(int i = n-1; i >= 0 ; i--)
					cout<<arr[i];
				for(int j = 0; j < 9; ++j)
					cout<<" "<<divisor[j];
				cout<<endl;
				start = start + 2;
			}
		}
	}
	return 0;
}