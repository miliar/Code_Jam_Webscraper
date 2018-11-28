#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define cin fin
#define cout fout
ifstream fin("a.in");
ofstream fout("ans.txt");

bool u[12];
void work(int n)
{
	memset(u, 0, sizeof(u));
	int c = 0;
	int m = 0;
	while(c != 10)
	{
		m += n;
		//for(int i = 1; i <= m; i++)
		{
			int k = m;
			while(k != 0)
			{
				int t = k % 10;
				if(!u[t])
				{
					u[t] = true;
					c++;
				}
				k /= 10;
			}
		}
		if(m > 1000000000) cerr << "???" << endl;
	}
	cout << m << endl;
}

int main()
{
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++)
	{
		int n;
		cin >> n;
		cout << "Case #" << t << ": ";
		if(n == 0)
			cout << "INSOMNIA" << endl;
		else
		{
			work(n);
		}
	}
	return 0;
}

