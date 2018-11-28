#include <iostream>
#include <fstream>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;


int main()
{
	ifstream in("D-small-attempt3.in");
	//ifstream in("test.txt");
	ofstream out("out.txt");
	stringstream buffer;

	//buffer << t.rdbuf();
	unsigned int T;		//test cases
	int X=0, R=0, C=0;
	in >> T;
	int Gabriel = 1, Richard = 2;
	int sol=-1;

	for (unsigned int i = 1; i <= T; i++)
	{
		in >> X;
		in >> R;
		in >> C;

		switch (X)
		{
		case 1:
			sol = Gabriel;
			break;
		case 2:
			if (R*C > 1 && ((R*C) % 2 == 0))
				sol = Gabriel;
			else
				sol = Richard;
			break;
		case 3:
			if (R*C < 3||(R<3&&C<3)||(R<2)||(C<2)) 
				sol = Richard;
			else if (((R*C) % 3 == 0))
				sol = Gabriel;
			else
				sol = Richard;
			break;
		case 4:
			if (R*C < 4)
				sol = Richard;
			else if (R < 4 && C < 4)
				sol = Richard;
			else if (R*C == 12 || R*C == 16)
				sol = Gabriel;
			else
				sol = Richard;
			break;
		default:
			sol = -1;
			break;
		};
		if (sol==Gabriel)
			out << "Case #" << i << ": " << "GABRIEL" << endl;
		else if (sol == Richard)
			out << "Case #" << i << ": " << "RICHARD" << endl;
		else
			out << "............................." << endl;

	}

	//cout << 24 % 4;
	getchar();

	return 0;
};