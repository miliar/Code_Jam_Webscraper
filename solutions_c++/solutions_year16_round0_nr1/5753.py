#include <iostream>
using namespace std;

bool checkArray(int arr[10])
{
	for(int i = 0; i<10; i++)
	{
		if(arr[i] == 0)
		{
			return false;
		}
	}
	return true;
}

void countSheep(long unsigned int N)
{
	if (N == 0)
	{
		cout<<"INSOMNIA"<<endl;
		return;
	}
	int arr[10];
	int lastNum = 0;
	for(int i = 0; i< 10; i++)
	{
		arr[i] = 0;
	}
    long int originalN = N;
    for(int j = 2; checkArray(arr)!= true; j++)
	{
		long unsigned int digits = N;
		while(digits!=0)
		{
			arr[digits%10]++;
			digits = digits/10;
		}
		lastNum = N;
        N = originalN*j;
	}
	cout<<lastNum<<endl;
}

int main()
{
	int T;
	int N;
	cin>>T;
	long unsigned int* inputNumbers = new unsigned long int[T];
	for(int i = 1; i<=T; i++)
	{
		cin>>N;
		inputNumbers[i-1] = N;
	}
	for(int j = 0; j<T; j++)
	{
		cout<<"Case #"<<j+1<<": ";
		countSheep(inputNumbers[j]);
	}
	delete [] inputNumbers;
}