#include<fstream>
#include<string>
using namespace std;

ifstream fin("a.in");
ofstream fout("a.out");

int main()
{
	int t;
	fin >> t;
	for (int j = 1; j <= t;j++)
	{
		int v[1005];
		int smax;
		fin >> smax;
		string s;
		fin >> s;
		for (int i = 0; i <= smax; i++)
		{
			int x;
			v[i] = x=s[i]-'0';
		}
		int sum = 0;
		int crt=0;
		for (int i = 0; i <= smax; i++)
		{
			if (crt < i&&v[i]>0)
			{
				sum += i - crt;
				crt = i + v[i];
			}
			else
			{
				crt += v[i];
			}
		}
		fout << "Case #" << j << ": " << sum << '\n';
	}

}