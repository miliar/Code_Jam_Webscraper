#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int factor(int P, int Q)
{
	if (P >= Q/2)
		return 1;
	else
		return 1 + factor(P, Q/2);
}
int main()
{
	int T;
	fstream fin("A.in");
	fstream fout("O.in");
	fin >> T;
	for (int i = 1; i <= T; i++)
	{
		int P = 0, Q = 0;
		string str;
		fin >> str;
		int j = 0;
		for (; str[j] != '/'; j++)
		{
			P = (P * 10) + ((int)str[j] - 48);
		}
		for (j = j + 1; str[j] != '\0'; j++)
		{
			Q = (Q * 10) + ((int)str[j] - 48);
		}
		int n = Q;
		bool flag = true;
		while (n >= 2)
		{
			if (n % 2 == 0)
				n /= 2;
			else
			{
				flag = false;
				break;
			}
		}
		if (flag == false)
			fout << "Case #" << i << ": impossible\n";
		else
		{
			int ans = factor(P, Q);
			if (ans > 40)
				fout << "Case #" << i << ": impossible\n";
			else
				fout << "Case #" << i << ": " << ans << endl;
		}
	}
	return 0;
}