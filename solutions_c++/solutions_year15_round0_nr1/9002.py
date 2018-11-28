#include <stdio.h>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void)
{
	fstream in_file, out_file;
	in_file.open("A-large.in", ios_base::in);
	out_file.open("out_1.txt", ios_base::out);

	int testcases = 0;

	in_file >> testcases;

	for (int cs = 1; cs <= testcases; ++cs)
	{
		int max_shyness = 0;
		in_file >> max_shyness;

		string aud = "";
		in_file >> aud;

		int stood_up = 0;
		int friends_needed = 0;

		for (int c = 0; c <= max_shyness; ++c)
		{
			char digit = aud[c];
			if (c > stood_up)
			{
				friends_needed += (c - stood_up);
				stood_up += (c - stood_up);
			}

			stood_up += atoi(&digit);
		}

		out_file << "Case #" << cs << ": " << friends_needed << endl;
	}

	in_file.close();
	out_file.close();

	return 0;
}