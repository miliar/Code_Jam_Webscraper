#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main()
{
	int ncases;
	int temp;
	long int v[10];
	long int letters[26];
	string s;

	//Input - Output
	ifstream in;
	ofstream out;
	in.open("A/A-large.in");
	out.open("A/A-large-results.out");

	in >> ncases;
	for (int t = 1; t <= ncases; t++)
	{
		memset(letters, 0, sizeof(long int) * 26);
		memset(v, 0, sizeof(long int) * 10);
		out << "Case #" << t << ": ";
		in >> s;
		for (int i = 0; i < s.length(); i++)
		{
			letters[int(s.at(i)) - 65]++;
		}

		//eight
		temp = letters[6];
		if (temp > 0)
		{
			v[8] = temp;
			letters[7] -= temp;
			letters[8] -= temp;
		}
		//three
		temp = letters[7];
		if (temp > 0)
		{
			v[3] = temp;
		}
		//zero
		temp = letters[25];
		if (temp > 0)
		{
			v[0] = temp;
		}
		//two
		temp = letters[22];
		if (temp > 0)
		{
			v[2] = temp;
		}
		//four
		temp = letters[20];
		if (temp > 0)
		{
			v[4] = temp;
			letters[5] -= temp;
		}
		//five
		temp = letters[5];
		if (temp > 0)
		{
			v[5] = temp;
			letters[21] -= temp;
			letters[8] -= temp;
		}
		//seven
		temp = letters[21];
		if (temp > 0)
		{
			v[7] = temp;
			letters[13] -= temp;
		}
		//six
		temp = letters[23];
		if (temp > 0) {
			v[6] = temp;
			letters[8] -= temp;
		}
		//nine 
		temp = letters[8];
		if (temp > 0)
		{
			v[9] = temp;
			letters[13] -= (2 * temp);
		}
		//one
		temp = letters[13];
		if (temp > 0)
		{
			v[1] = temp;
		}

		for (int i = 0; i < 10; i++) {
			if (v[i] > 0)
			{
				for (int k = 0; k < v[i]; k++)
				{
					out << i;
				}
			}
		}
		if (t < ncases)
			out << endl;
	}

	in.close();
	out.close();
	return 0;
}