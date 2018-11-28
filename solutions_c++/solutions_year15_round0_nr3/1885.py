#include <iostream>
#include <string>
#include <fstream>
using namespace std;
typedef int element;
element mularray[5][5] = { {0,0,0,0,0},{ 0, 1, 2, 3, 4 }, { 0, 2, -1, 4, -3 }, { 0, 3, -4, -1, 2 }, { 0, 4, 3, -2, -1 } };
inline element mul(element x, element y)
{
	int option = x*y < 0 ? -1 : 1;
	x = x < 0 ? -x : x;
	y = y < 0 ? -y : y;
	return mularray[x][y] * option;
}

inline element pwr(element x, int c)
{
	element result = 1;
	for (int i = 0; i != c % 4; i++)
	{
		result = mul(result, x);
	}
	return result;
}
inline element getProduct(string s)
{
	element result = 1;
	for (int i = 0; i != s.length(); i++)
	{
		element tmp;
		switch (s[i])
		{
		case 'i':tmp = 2; break;
		case 'j':tmp = 3; break;
		case 'k':tmp = 4; break;
		default:
			break;
		}
		result = mul(result, tmp);
	}
	return result;
}
inline int productStarti(string s)
{
	element result = 1;
	for (int i = 0; i != s.length(); i++)
	{
		element tmp;
		switch (s[i])
		{
		case 'i':tmp = 2; break;
		case 'j':tmp = 3; break;
		case 'k':tmp = 4; break;
		default:
			break;
		}
		result = mul(result, tmp);
		if (result == 2) return i;
	}
	return -1;
}
inline int productEndk(string s)
{
	element result = 1;
	for (int i = s.length()-1; i >= 0; i--)
	{
		element tmp;
		switch (s[i])
		{
		case 'i':tmp = 2; break;
		case 'j':tmp = 3; break;
		case 'k':tmp = 4; break;
		default:
			break;
		}
		result = mul(tmp, result);
		if (result == 4) return i;
	}
	return -1;
}

int main()
{
	int T;
	ifstream fin("C-small-attempt1.in");
	ofstream fout("output.txt");
	fin >> T;
	for (int TT = 1; TT <= T; TT++)
	{
		int L, X;
		string Pass;
		string s;
		fin >> L >> X;
		fin >> s;
		element product = getProduct(s);		
		if (pwr(product,X) == getProduct("ijk"))
		{
			if (X > 8)
			{
				string ss;
				for (int i = 0; i != 4; i++) ss += s;
				if (productStarti(ss)>=0 && productEndk(ss)>=0) Pass = "YES"; else Pass = "NO";
			}
			else
			{
				string ss;
				for (int i = 0; i != X; i++) ss += s;
				int l = productStarti(ss);
				int r = productEndk(ss);
				if (l < 0 || r < 0 || l >= r) Pass = "NO"; else Pass = "YES";
			}
		}
		else Pass = "NO";		
		fout << "Case #" << TT<<": " << Pass << endl;
	}
}