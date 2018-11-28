#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;
int main()
{
	fstream input;
	fstream output;
	input.open("A-small-attempt2.in", ios::in);
	output.open("a.out", ios::out);
	int a[4];
	int b[4];
	int cas, T, line, i, j, t, count, num;
	
		input >> T;
		//cout<<T<<endl;
		for (cas = 1; cas <= T; cas++) {
			input >> line;
			for (i = 1; i <= 4; i++)
				for (j = 0; j < 4; j++) {
					input >> t;
					if (i == line)
						a[j] = t;
				}
			input >> line;
			for (i = 1; i <= 4; i++)
				for (j = 0; j < 4; j++) {
					input >> t;
					if (i == line)
						b[j] = t;
				}
			count = 0;
			for (i = 0; i < 4; i++)
				for (j = 0; j < 4; j++)
					if (a[i] == b[j]) {
						count++;
						num = a[i];
					}
			output << "Case #" << cas << ": ";
			if (count == 1)
				output << num << endl;
			else if (count > 1)
				output << "Bad magician!" << endl;
			else
				output << "Volunteer cheated!" << endl;
		}
	return 0;
}
