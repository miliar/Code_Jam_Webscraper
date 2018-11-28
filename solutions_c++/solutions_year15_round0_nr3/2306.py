#include <vector>
#include <tuple>
#include <set>
#include <algorithm>
#include <math.h>
#include <iomanip>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;
char mult(char a, char b, int*sign)
{
	*sign = 1;
	if (a == '1') return b;
	if (b == '1') return a;
	if (a == 'i' && b == 'j') return 'k';
	if (a == 'k' && b == 'i') return 'j';
	if (a == 'j' && b == 'k') return 'i';
	*sign = -1;
	if (a == b) return '1';
	if (a == 'j' && b == 'i') return 'k';
	if (a == 'i' && b == 'k') return 'j';
	//if (a == 'k' && b == 'j') 
		return 'i';
}
int main()
{
	ifstream fin;
	fin.open("C-small-attempt1.in");
	if (fin.is_open())
	{
		ofstream fout;
		fout.open("C-small-attempt1.out");
		int T;
		fin >> T;
		for (int i = 0; i < T; i++)
		{
			int L,X;
			fin >> L>>X;
			string str;
			getline(fin,str);
			getline(fin, str);
//			fout << str << endl;
			char last = '1';
			int sign = 1;
			string res ="NO";
			string wanted = "ijk";
			int cur = 0;
			char repeat='1';
			for (int j = 0; j < X; j++)
			{
				for (int k = 0; k < L; k++)
				{
					int newsign = 1;
					last = mult(last, str[k], &newsign);
					sign *= newsign;
					if (cur<wanted.length() && last == wanted[cur])
					{
						cur++;
						last = '1';
						repeat = '1';
					}
				}
			}
				if (cur == wanted.length() && last == '1' && sign == 1)
					{
						res = "YES";
					}
			/*	else
				{
					if (repeat == '1')
					{
						repeat = last;
					}
					else
						if (repeat == last)
						{
							break;
						}
				
				
			}*/
			fout << "Case #" << i + 1 << ": " << res << endl;
		}
		fin.close();
		fout.close();
	}
	return 0;
}