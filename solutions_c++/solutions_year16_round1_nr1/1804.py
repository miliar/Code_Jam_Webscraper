#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

int main()
{

	ifstream infile;
	infile.open("A-large1.in", ios::in);

	ofstream outfile;
	outfile.open("A-large1.out", ios::out);

	int T;
	infile>>T;
	int index = 1;

	while(T--)
	{
		char S[1002];
		char Aux[3000];
		infile>>S;
		int cur_beg = 1050;
		int cur_end = 1050;
		int i;
		Aux[cur_beg] = S[0];
		cur_end++;

		outfile<<"Case #"<<index<<": ";
		
		for(i=1; i<strlen(S);i++)
		{
					
			if(S[i] >= Aux[cur_beg])
			{
				cur_beg--;
				Aux[cur_beg] = S[i];

			}
			else
			{
				Aux[cur_end] = S[i];
				cur_end++;
			}


		}

		for(i = cur_beg; i<cur_end; i++)
		outfile <<Aux[i];
		
		outfile<<"\n";
		index++;
	}

	


	return 0;
}
