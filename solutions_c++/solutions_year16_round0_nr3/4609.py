#include <iostream>
#include <cmath>
using namespace std;
unsigned long long isPrime(unsigned long long number)
{
	unsigned long long start;
	for(start = 2; start <= sqrt(number); start++)
		if(number % start == 0) return start;
	return -1;
}
unsigned long long numberInBaseX(unsigned long long number, unsigned long long base)
{
	//cout << "Number is " << number << " and base is " << base << endl;
	unsigned long long temp = number, count = 1, rem, value = 0;
	while(temp>0)
	{
		rem = temp % 2;
		value = value + (rem * count);
		count = count * base;
		temp = temp/2;
	}
	return value;
}
int main()
{
	unsigned long long T, i, n, j, jamcoinbase, jamcoinend, l, k, h, count1, jamcoinmiddle, temp1;
	cin>>T;
	for(i=0;i<T;i++)
	{
		cin>>n>>j;
		jamcoinbase = (1 << 0) | ( 1<<(n-1));
		jamcoinend = ~(-1 << n);
		count1 = 0;
		jamcoinmiddle = 0;
		cout << "Case #" << i + 1 << ":\n";
		for(l = jamcoinbase;l<=jamcoinend;)
		{
			unsigned long long nontrivialdiv[9], count = 0;
			for(k=0;k<9;k++) nontrivialdiv[k] = 0;
			for(k=2;k<=10;k++)
			{
				h = numberInBaseX(l, k);
				if(isPrime(h) != -1)
				{
					nontrivialdiv[k-2] = isPrime(h);
					count++;
				}
			}
			if(count == 9)
			{
				count1++;
				cout << h << " ";
				for(k=0;k<9;k++) cout << nontrivialdiv[k] << " ";
				cout << endl;
			}
			if(count1 == j)
				break;
			if(l == jamcoinend) break;
			temp1 = (++jamcoinmiddle << 1);
			l = jamcoinbase | temp1;
		}
	}
}