#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main()
{
	ifstream infile("B-large.in");
	ofstream outfile("output.in");
	int T, count;
	char c1, c2;
	string str1;
	infile >> T;
	for (int i = 0; i < T; i++)
	{
		count = 0;
		infile >> str1;
		c1 = str1[0];
		for (int g = 1; str1[g] != '\0'; g++)
		{
			c2 = str1[g];
			if (c2 != c1)
				count++;
			c1 = c2;
		}
		if (str1.back() == '-')
			count++;
		outfile << "Case #" << i + 1 << ": " << count << endl;
	}
}