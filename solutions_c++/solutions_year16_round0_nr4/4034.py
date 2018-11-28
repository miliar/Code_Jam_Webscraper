#include <iostream>
#include <fstream>
#include <vector>
#define NMAX 200
using namespace std;
ifstream fin("date.in");
ofstream fout("date.out");
int uz[NMAX],cnt;
unsigned long long int T, n, k, c,s;
vector <unsigned long long int> pozitii;
int main()
{
	fin >> T;
	for (unsigned long long int test = 1; test <= T; test++)
	{
		fout << "Case #" << test << ": ";
		fin >> k >> c >> s;

		if (k <= s)
		{
			unsigned long long int copie = k;
			unsigned long long int sum = 1;
			for (unsigned long long int i = 1; i <= c - 1; i++)
			{
				sum += copie;
				copie *= k;
			}
			for (unsigned long long int i = 1; i <= k; i++)
			{
				fout << (i - 1)*sum + 1 << " ";
			}
			fout << '\n';
		}
		else
		{
			for (unsigned long long int i = 1; i <= k; i++)
			{
				uz[i] = 0;
			}
			cnt = 0;
			unsigned long long int copie = k;
			unsigned long long int sum = 1;
			for (unsigned long long int i = 1; i <= c - 1; i++)
			{
				sum += copie;
				copie *= k;
			}
			for (unsigned long long int i = 1; i <= k; i++)
			{
				pozitii.push_back((i - 1)*sum + 1 + (k - i - 1));
				if (uz[i] == 0) cnt++;
				uz[i] = 1;
				if (c != 1 && (k - i - 1) >= 0 && uz[k - i + 1] == 0)
					cnt++;
				uz[k - i + 1] = 1;
				if (cnt >= k)
					break;
			}
			if (cnt >= k)
			{
				vector<unsigned long long int>::iterator it;
				for (it = pozitii.begin(); it != pozitii.end(); it++)
					fout << *it << " ";
				fout << '\n';
			}
			else
				fout << "IMPOSSIBLE\n";

			pozitii.clear();



		}

		
	}
}