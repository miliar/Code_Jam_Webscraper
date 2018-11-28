#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>
#include <vector>
#include <list>

using namespace std;



int main()
{
	FILE *in;
	if (fopen_s(&in, "A-large.in", "r+") != 0)
		printf("The in file was not opened\n");

	fstream out("A-large.out", ios::out);
	if (out.bad())
		printf("The out file was not opened\n");

	int T;
	fscanf_s(in, "%d", &T);

	for (int tc = 1; tc <= T; tc++)
	{
		int S;
		fscanf_s(in, "%d ", &S);

		int friends = 0;
		int people = 0;
		for (int i = 0; i <= S; i++)
		{
			char c;
			fscanf_s(in, "%c", &c);
			c -= 48;

			people += c;
			if (people <= i)
			{
				friends++;
				people++;
			}
		}

		cout << "Case #" << tc << ": " << friends << endl;
		out << "Case #" << tc << ": " << friends << endl;
	}

//	_ASSERT(Glass::getLevel(1) == 1);
//	cout << "Unit tests of Glass::getLevel() are OK" << endl;

	out.close();
	getchar();
}