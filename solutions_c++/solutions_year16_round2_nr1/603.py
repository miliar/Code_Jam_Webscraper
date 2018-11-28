#include <iostream>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <map>
#include <string>

using namespace std;

int l(char c)
{
	return c - 'A';
}



int main()
{
	int n;
	cin >> n;
	string num;
		getline(cin, num);
	for(int i = 1; i <= n; i++)
	{
		
		getline(cin, num);
		int cfrequencies[26] = {0};
		for(char c : num)
			cfrequencies[l(c)]++;
		int frequencies[10] = {0};
		//zero
		int z = cfrequencies[l('Z')];
		frequencies[0] = z;
		cfrequencies[l('Z')] -= z;
		cfrequencies[l('E')] -= z;
		cfrequencies['R'-'A'] -= z;
		cfrequencies['O'-'A'] -= z;
		//four
		int u = cfrequencies[l('U')];
		frequencies[4] = u;
		cfrequencies[l('F')] -= u;
		cfrequencies[l('O')] -= u;
		cfrequencies[l('U')] -= u;
		cfrequencies[l('R')] -= u;
		//two
		int w = cfrequencies[l('W')];
		frequencies[2] = w;
		cfrequencies[l('T')] -= w;
		cfrequencies[l('W')] -= w;
		cfrequencies[l('O')] -= w;
		//six
		int x = cfrequencies[l('X')];
		frequencies[6] = x;
		cfrequencies[l('S')] -= x;
		cfrequencies[l('I')] -= x;
		cfrequencies[l('X')] -= x;
		//five
		int f = cfrequencies[l('F')];
		frequencies[5] = f;
		cfrequencies[l('F')] -= f;
		cfrequencies[l('I')] -= f;
		cfrequencies[l('V')] -= f;
		cfrequencies[l('E')] -= f;
		//one
		int o = cfrequencies[l('O')];
		frequencies[1] = o;
		cfrequencies[l('E')] -= o;
		cfrequencies[l('N')] -= o;
		cfrequencies[l('O')] -= o;
		//eight
		int g = cfrequencies[l('G')];
		frequencies[8] = g;
		cfrequencies[l('E')] -= g;
		cfrequencies[l('I')] -= g;
		cfrequencies[l('G')] -= g;
		cfrequencies[l('H')] -= g;
		cfrequencies[l('T')] -= g;
		//seven
		int v = cfrequencies[l('V')];
		frequencies[7] = v;
		cfrequencies[l('S')] -= v;
		cfrequencies[l('E')] -= v;
		cfrequencies[l('V')] -= v;
		cfrequencies[l('E')] -= v;
		cfrequencies[l('N')] -= v;
		//three
		int t = cfrequencies[l('T')];
		frequencies[3] = t;
		cfrequencies[l('T')] -= t;
		cfrequencies[l('H')] -= t;
		cfrequencies[l('R')] -= t;
		cfrequencies[l('E')] -= t;
		cfrequencies[l('E')] -= t;
		//nine
		int e = cfrequencies[l('E')];
		frequencies[9] = e;
		
		cout << "Case #" << i << ": ";
		for(int j = 0; j < 10; j++)
		{
			for(int k = 0; k < frequencies[j]; k++)
				cout << j;
		}
		cout << endl;
	}
	return 0;
}