#include<iostream>
#include<fstream>
#include<vector>
#include<ctime>

long long unsigned int conversion(long long unsigned int num, int base)
{
	int a;
	long long unsigned int result = 0, count = 0, temp = 1, i = 0;
	while (num > 0)
	{
		a = num % 10;
		num /= 10;
		if( i>0 )temp *= base;
		result += (temp * a);
		i++;
	}
	return result;
}

bool primeCheck(long long unsigned int num, int & obj)
{
	long long unsigned int a = sqrt(num);
	for (long long unsigned int i = 2; i <= a; i++)
	{
		if (num%i == 0)
		{
			obj = i;
			return true;
		}
	}
	return false;
}

int main()
{
	int cases, n, j, div = 0;
	long long int unsigned num = 1;
	long long unsigned int converted = 0;
	std::vector<long long unsigned int> divisors, prev;
	bool flag = true;
	srand(time(NULL));
	std::ifstream fin;
	std::ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	fin >> cases;
	for (int i = 0; i < cases; i++)
	{
		fin >> n;
		fin >> j;
		fout << "Case #" << i+1 << ":\n";
		for (int l = 0; l < j; l++)
		{
			divisors.clear();
			num = 1;
			flag = true;
			for (int m = 0; m < n-2; m++)
			{
				num *= 10;
				num += rand() % 2;
			}
			num *= 10;
			num += 1;
			for (int m = 0; m < prev.size(); m++)
			{
				if (prev[m] == num)flag = false;
			}
			for (int m = 2; m <= 10 && flag; m++)
			{
				converted = conversion(num, m);
				flag = primeCheck(converted, div);
				divisors.push_back(div);
			}
			if (flag)
			{
				fout << num << " ";
				prev.push_back(num);
				for (int m = 0; m < divisors.size(); m++)
				{
					fout << divisors[m] << " ";
				}
				fout << "\n";
			}
			else l--;
		}
	}
}