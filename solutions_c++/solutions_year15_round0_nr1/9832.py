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
	
	ifstream in("A-small-attempt0.in");
	ofstream out("out.txt");
	stringstream buffer;


	//buffer << t.rdbuf();
	unsigned int T;		//test cases
	in >> T;
	
	unsigned int Smax = 0;
	string audience;
	unsigned int standed;
	unsigned int friends;
	for (unsigned int i = 1; i <= T; i++)
	{
		audience.clear();
		standed = 0;
		friends = 0;
		in >> Smax;
		in >> audience;
		for (unsigned int k = 0; k <= Smax; k++)
		{
			if (audience[k] == '0')
				;
			else if (standed >= k)
			{
				standed += audience[k]-'0';
			}
			else
			{
				friends += (k - standed);
				standed += audience[k] - '0' + friends;
			}

		}

		out << "Case #" << i <<": "<< friends << endl;
		
	}





	
	//out << buffer.str();
	in.close();
	out.close();
	
	getchar();

	return 0;

}