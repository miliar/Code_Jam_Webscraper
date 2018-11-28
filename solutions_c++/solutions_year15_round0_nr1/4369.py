#include <algorithm>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main (int argc, char const* argv[])
{
	int T, t, S, i, count, no_of_p;
	char str[1010];
	ifstream fin;
	ofstream fout;

	fin.open("input.txt");
	fout.open("output.txt");
	t = 0;
	fin >> T;
	while (++t <= T)
	{
		fin >> S;
		fin >> str;
		i = strlen(str)-1;
		while (str[i] == '0') i--;
		str[i+1]='\0';
		count = 0;
		no_of_p = 0;
		for (i=0 ; i<strlen(str) ; ++i)
		{	if (no_of_p >= i)
			{
				no_of_p += (str[i]-'0');
				//cout << no_of_p << "\n";	
			}
			else
			{
				count += (i-no_of_p);
				//cout << "\t" << count << "\n";
				no_of_p += (i-no_of_p + (str[i]-'0'));
				//cout << "\t" << no_of_p << "\n";
			}
		}
		fout << "Case #" << t << ": " << count << "\n";
	}
	fin.close();
	fout.close();
	return 0;
}
