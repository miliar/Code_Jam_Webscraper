#include <iostream>
#include <fstream>
#include <string>
#include<algorithm>
using namespace std;

ofstream fout("answer.txt");
ifstream fin("D-large.in");

int main()
{
	int t, a;
	fin >> t;
	for (a = 1; a <= t; a++)
	{
		int num, h, h1, h2;
		int num1, num2;
		double number1[1000], number2[1000];
		fin >> num;
		for (h = 0; h < num; h++)
		{
			fin >> number1[h];
		}
		for (h = 0; h < num; h++)
		{
			fin >> number2[h];
		}
		sort(number1, number1 + num);
		sort(number2, number2 + num);
		h1 = num - 1;
		h2 = num - 1;
		num2 = 0;
		num1 = 0;
		for (;;)
		{
			if (number1[h1] < number2[h2])
			{
				h1--;
				h2--;
			}
			else
			{
				h1--;
				num2++;
			}
			if (h1 < 0)
				break;
		}
		h1 = 0;
		h2 = 0;
		for (;;)
		{
			if (number1[h1] < number2[h2])
			{
				h1++;
			}
			else
			{
				h1++;
				h2++;
				num1++;
			}
			if (h1 == num)
				break;
		}
		fout << "Case #" << a << ": " << num1 << " " << num2 << endl;
	}
	return 0;
}