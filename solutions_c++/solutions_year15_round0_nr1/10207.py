#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
using namespace std;

int main()
{
	int T;
	ifstream in;
	ofstream out;
	string fn = "A-small-attempt4.in";	
	string fo = "solution.out";

	in.open(fn);
	out.open(fo);
	in >> T;

	for (int i = 0; i < T; i++)
	{
		
		int sMax=0;
		int friends = 0;
		int standing = 0;
		in >> sMax;

		string s = "";

		in >> s;
			

		for (int j = 0; j < s.length(); j++)
		{	
			int people = s[j]-'0';
			int shyness = j;		

			if (standing > sMax)
			{
				break;
			}


			if (shyness > standing)
			{
				friends += shyness - standing;
				standing += shyness - standing;
			}
			
			standing += people;

		}

		out << "Case #"<<i+1<<": "<<friends<<endl;
		
	}

	in.close();
	out.close();

	return 0;
}