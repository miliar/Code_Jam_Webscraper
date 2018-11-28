#include <algorithm>
#include <bitset>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
#include <fstream>   
using namespace std;

string doit(int L, int X, string p)
{
	string s = "";

	for (int i = 0; i < X; i++)
		s += p;

	char wanted = 'i';

	char cur = '1';
	int sign = 0;
	for (int i = 0; i < s.size(); i++)
	{	
		if (cur == '1')
		{
			cur = s[i];
		}
		else if (cur == 'i')
		{
			if (s[i] == 'i')
			{
				cur = '1';
				sign = (sign + 1) % 2;
			}
			else if (s[i] == 'j')
			{
				cur = 'k';
			}
			else
			{
				cur = 'j';
				sign = (sign + 1) % 2;;
			}
		}
		else if (cur == 'j')
		{
			if (s[i] == 'i')
			{
				cur = 'k';
				sign = (sign + 1) % 2;
			}
			else if (s[i] == 'j')
			{
				cur = '1';
				sign = (sign + 1) % 2;
			}
			else
			{
				cur = 'i';
			}
		}
		else
		{
			if (s[i] == 'i')
			{
				cur = 'j';
			}
			else if (s[i] == 'j')
			{
				cur = 'i';
				sign = (sign + 1) % 2;
			}
			else
			{
				cur = '1';
				sign = (sign + 1) % 2;
			}
		}

		if (cur == wanted)
		{
			cur = '1';
			wanted++;
		}
	}

	if (wanted == 'l' && cur == '1' && sign == 0)
		return "YES";
	else
		return "NO";
}

int main(void)
{
	freopen("d:\\output.txt", "w", stdout);
	freopen("d:\\input.txt", "r", stdin);

	int T;
	cin >> T;
	
	int L, X;

	string p;
	for (int i = 0; i < T; i++)
	{
		cin >> L >> X>>p;


		cout << "Case #"<<i+1<<": " << doit(L,X,p) << endl;
	}
}