#include<iostream>
using namespace std;

FILE* pF;
FILE* pAnsF;
int countarr[10];

int N;

typedef unsigned long long ull;

int nDigitCount;

bool process(ull num)
{
	ull nDigit;
	while (num)
	{
		nDigit = num % 10;
		if (countarr[nDigit] == 0)
		{
			nDigitCount++;
			if (nDigitCount == 10)
				return true;
			countarr[nDigit] = 1;
		}
		num = num / 10;
	}
	return false;
}
void init()
{
	nDigitCount = 0;
	for (int i = 0; i < 10; i++)
	{
		countarr[i] = 0;
	}
}
int main()
{
	freopen_s(&pF, "Text.txt", "r", stdin);
	freopen_s(&pAnsF, "OutputGCJALarge.txt", "w", stdout);

	int C;

	cin >> C;

	for (int c = 1; c <= C; c++)
	{
		init();
		cin >> N;
		ull num = N;
		ull day = 2;
		while (num && process(num) == false)
		{
			num = N * day;
			day++;
		}
		if (num == 0)
		{
			cout << "Case #" << c << ": " << "INSOMNIA"<<endl;
		}
		else
		{
			cout << "Case #" << c << ": " << num << endl;
		}
	}
	
	return 0;
}