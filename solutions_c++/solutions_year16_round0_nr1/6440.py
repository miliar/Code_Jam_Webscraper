#include <iostream>
#include <fstream>
#include <stdio.h>

using namespace std;

int test, index;
int price[2005];
int digit[10] = {0};
long long number;
long long calNum;
bool isOk(long long num);
int main()
{
cin >> test;
int i, j;

for ( i =1; i<= test; i++)
{
	cin >> number ;
	index = 1;
	if (number == 0)
	{
		cout << "Case #" << i << ": INSOMNIA"<< endl;
	}
	else
	{
		// init digit array
		for (j=0 ; j <10 ; j++)
		{
			digit[j] = 0;
		}
		calNum = number;
		while (!isOk(calNum))
		{
			index++;
			calNum =index* number;
		}
		cout << "Case #" << i << ": " << calNum << endl;
	}		
}
return 0;
}

bool isOk(long long num)
{
	while (num)
	{
		digit[num%10] = 1;
		num/=10;
	}
	int sum = 0;
	for (int i =0; i< 10; i++)
	{
		sum+= digit[i];
	}
	//cout << "sum " << sum << endl;
	return sum == 10;
}