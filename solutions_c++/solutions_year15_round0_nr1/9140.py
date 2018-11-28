#include <iostream>
#include <string>
#include <fstream>

using namespace std;

int main()
{
	fstream input,output;
	input.open("input.in",ios::in);
	output.open("output.out",ios::out);

	int T;
	input >> T;

	for(int cont=1; cont<=T; cont++)
	{
		int ms=0, people=0,y=0;

		string s;

		input >> ms;
		input >> s;

		for(int cont1=0; cont1<(ms+1); cont1++)
		{
			people = people + ((int)s[cont1] - 48);

			if(people < cont1+1)
			{
				while(people != cont1+1)
				{
					y++;
					people++;
				}
			}

		}

		output << "Case #" << cont << ": " << y << endl;
	}

	return 0;
}