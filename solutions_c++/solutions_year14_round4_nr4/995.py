#include <iostream>
#include <fstream>
#include <vector>
#include <assert.h>
#include <cmath>
#include <set>

using namespace std;

string s[10];
int m, n;

int assign[10];

int biggest = -1;
int total = 0;

void compute()
{
	int t = 0;
	for (int i = 0; i < n; i++)
	{
		set<string> hit;
		for (int k = 0; k < m; k++)
			if (assign[k] == i)
			{
				string a = "";
				hit.insert(a);
				for (int j = 0; j < s[k].length(); j++)
				{
					a += s[k][j];
					hit.insert(a);
				}
			}
		t += hit.size();
	}

	if (t == biggest)
		total++;
	if (t > biggest)
	{
		biggest = t;
		total = 1;
	}
}

void recur(int depth)
{
	if (depth == m)
	{
		compute();
		return;
	}
	// depth < m

	for (int i = 0; i < n; i++)
	{
		assign[depth] = i;
		recur(depth + 1);
	}

}

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");

	int t; fin >> t;
	for (int test = 0; test < t; test++)
	{
		cout << test << endl;
		biggest = -1;
		total = 0;
		
		fin >> m >> n;

		for (int i = 0; i < m; i++)
		{
			fin >> s[i];
		}

		recur(0);


		fout << "Case #" << test + 1 << ": " << biggest << " " << total << endl;
	}
}