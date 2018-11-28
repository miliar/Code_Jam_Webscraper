#include <iostream>
#include <fstream>
using namespace std;

int num[10] = {};

void fill_number(long long int n)
{
	while (n)
	{
		int get = n % 10;
		num[get] = 1;
		n /= 10;
	}
}

bool check()
{
	int i;
	for (i = 0; i<10; ++i)
	{
		if (!num[i]) return true;
	}
	return false;
}

int main()
{
    fstream fin,fout;
    fin.open("A-large.in",ios::in);
    fout.open("out.txt",ios::out);
	int t, i, m;
	fin >> t;
	m = t;
	while (t--)
	{
		for (i = 0; i<10; ++i) num[i] = 0;
		long long int n;
		int tim = 1;
		fin >> n;
		fout << "Case #" << m - t << ": ";
		if (n == 0)
		{
			fout << "INSOMNIA\n";
			continue;
		}
		while (check())
		{
			fill_number(n);
			n /= tim++;
			n *= tim;
		}
		n /= tim--;
        n *= tim;
		fout << n << endl;
	}
	return 0;
}
