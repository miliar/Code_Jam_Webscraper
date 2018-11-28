//Created by krever
//Google Codejam 2014

#include <iostream>
#include <fstream>
using namespace std;

	ifstream practice;
	ofstream output;

int main()
{
	practice.open("A-small-attempt3.in");
	output.open("output.txt");

	int cases;			//T
	int casecount(1);
	int row;
	int cardrow[16];
	int rowcount(0);
	int cardmatch[4];
	int cardmatch2[4];
	int j(0);
	int k(0);
	int matchcounter(0);
	int find;
	int number;

	practice >> cases;

	while((!practice.eof()) && (casecount <=cases))
	{
		practice >> row;
		int i(0);		//item in array
		
		while(i<16)
		{
			practice >> cardrow[i];
			i++;
		}

		i=0;

		switch(row)
		{
			case 1:
				while(j<4)
				{
					cardmatch[j]= cardrow[j];
					j++;
				}
				break;

			case 2:
				while(j<4)
				{
					cardmatch[j]= cardrow[j+4];				
					j++;
				}
				break;
			case 3:
				while(j<4)
				{
					cardmatch[j]= cardrow[j+8];
					j++;
				}
				break;
			case 4:
				while(j<4)
				{
					cardmatch[j]= cardrow[j+12];
					j++;
				}
				break;
		}

		practice >> row;

		while(i<16)
		{
			practice >> cardrow[i];
			i++;
		}

		i=0;
		j=0;
		switch(row)
		{
			case 1:
				while(j<4)
				{
					cardmatch2[j]= cardrow[j];
					j++;
				}
				break;

			case 2:
				while(j<4)
				{
					cardmatch2[j]= cardrow[j+4];
					j++;
				}
				break;
			case 3:
				while(j<4)
				{
					cardmatch2[j]= cardrow[j+8];
					j++;
				}
				break;
			case 4:
				while(j<4)
				{
					cardmatch2[j]= cardrow[j+12];
					j++;
				}
				break;
		}

		j=0;

		for(j=0, k=0; j<4;k++)
		{
			find=cardmatch[j];

			if(find== cardmatch2[k])
			{
				matchcounter++;
				number = cardmatch2[k];
			}

			if(k==3)
			{
				k=-1;
				j++;
			}
		}

		output << "Case #" << casecount << ": ";

		if(matchcounter ==0)
		{
			output << "Volunteer cheated!" << endl;
		}
		else if(matchcounter >1)
		{
			output << "Bad magician!" << endl;
		}
		else if(matchcounter ==1)
		{
			output << number << endl;
		}
		matchcounter=0;
		casecount++;
		number = 0;
		j =0;
		i= 0;
	}

	return 0;
}