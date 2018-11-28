#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

long long int solve(char a[200],int N)
{
	long long int result = 0;
	long long int cnt = N - 1;
	char c = '+';
	while (cnt >= 0)
	{
		if (a[cnt] != c)
		{
			result += 1;
			while (a[cnt] != c)
				cnt--;
			if (c == '+')
				c = '-';
			else
				c = '+';
		}
		else
			cnt--;
	}
	return result;
}
int main()
{
	ofstream fout("out.txt");
	ifstream fin("in.txt");

	//	ofstream fout1("in.txt");
	//	fout1 << 1000000 << endl;
	//	for (int i = 0; i < 1000000; i++)
	//		fout1 << i << endl;
	int test_cases;
	fin >> test_cases;
	int num123 = 1;
	while (test_cases--)
	{
		char s[200];
		string a;
		long long int  result;
		fin >> s;
		result = solve(s,strlen(s));
		fout << "Case #" << num123 << ": " << result << endl;

		num123++;
	}
	return 0;
}