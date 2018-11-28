#include <iostream>  
#include <fstream>
#include <string>
#include <math.h>
using namespace std;  

int isPrime(unsigned long long num)
{
	if (num <= 1)
		return -1;
	else if (num == 2)
		return 2;
	else if (num % 2 == 0)
		return 2;
	else
	{
		bool prime = true;
		int divisor = 3;
		double num_d = static_cast<double>(num);
		int upperLimit = static_cast<int>(sqrt(num_d) + 1);

		while (divisor <= upperLimit)
		{
			if (num % divisor == 0)
				return divisor;
			divisor += 2;
		}
		return -1;
	}
}
void converttobinary(int a[], int n, int size)
{
	for (int i = size; i >= 0; i--)
	{
		a[i] = n % 2;
		n = n / 2;
	}
}
unsigned long long converttobase(int a[], int base, int size)
{
	unsigned long long num = 0;
	for (int i = 0; i <= size ; i++)
	{
		num += a[size - i] * pow(base, i);
	}
	return num;
}

void main() 
{
	ofstream myfile;
	ifstream inputfile("C-small-attempt0.in");
	int t, n, m;
	int a[16];
	unsigned long long b[9];
	int c[9];
	inputfile >> t;
	myfile.open("example.txt");
	for (int i = 1; i <= t; ++i) 
	{
		myfile << "Case #" << i << ": " << endl;
		inputfile >> n >> m; 
		n = 16;
		m = 50;
		int count = 0;
		int startnum = pow(2, n - 1) + 1;
		int endnum = pow(2, n) - 1;
		for (int i = startnum; i <= endnum; i++)
		{
			converttobinary(a, i, n-1);
			bool flag = true;
			if (a[n - 1] == 0)
			{
				continue;
			}
			for (int j = 2; j <= 10; j++)
			{
				b[j-2] = converttobase(a, j, n - 1);
				if (isPrime(b[j - 2]) == -1)
					flag = false;
				else
					c[j - 2] = isPrime(b[j - 2]);
			}
			
			if (flag == true)
			{
				count++;
				for (int j = 0; j < n; j++)
				{
					myfile << a[j];
				}
				myfile << " ";
				for (int j = 0; j <= 8; j++)
				{
					myfile << c[j] << " ";
				}
				myfile << endl;
			}
			if (count == m)
				break;
		}
	}
	myfile.close();
	inputfile.close();
	getchar();
}