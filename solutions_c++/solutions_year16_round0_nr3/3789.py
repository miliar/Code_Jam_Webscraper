// Jamcoin.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<iostream>
#include<fstream>

using namespace std;

long long getBaseValue(int base, long long num)
{
	int ar[16];
	int k = 0;
	long long num1 = 0;
	while (num != 0)
	{
		ar[k]=num%2;
		num = num / 2;
		k++;
	}
	k-- ;
	while (k >= 0)
	{
		num1 = num1*base + ar[k];
		k--;
	}
	return num1;
}
bool IsNotPrime(long long num, long int *arr, int i)
{
	if (num % 2 == 0)
	{
		arr[i] = 2;
		return true;
	}
	long int k = sqrt(num);
	if (k % 2 == 0)
		k--;
	while (k > 1)
	{
		if (num%k == 0)
		{ 
			break;
		}
		k -= 2;
	}
	if (k > 1)
	{
		arr[i] = k;
		return true;
	}
	return false;
}



int main()
{
	ifstream infile("C:\\Users\\NeerajB\\Desktop\\C-small-attempt2.in");
	ofstream outfile("C:\\Users\\NeerajB\\Desktop\\output.out");
	int t, n, j;
	outfile << "Case #1:\n";
	long int arr[8];
	infile >> t >> n >> j;
	int k = 0;
	long long up = pow(2, n);
	long long low = pow(2, n-1);
	for (long long i = low; i < up, j>0; i++)
	{
		if (i % 2 == 0)
			continue;
		bool flag = true;
		long long decimalValue = getBaseValue(10, i);
		flag = flag && IsNotPrime(i, arr, k++);
		for (int base = 3; base < 10;base++)
		{ 
			flag = flag && IsNotPrime(getBaseValue(base, i),arr,k++);
		}
		flag = flag && IsNotPrime(decimalValue, arr, k++);
		if (flag == true)
		{
			outfile << decimalValue;
			for (int j = 0; j <= 8; j++)
				outfile << " " << arr[j];
			outfile << "\n";
			j--;
		}
		k = 0;
	}

}

