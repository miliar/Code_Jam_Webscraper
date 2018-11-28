#include <fstream>

using namespace std;
void main()
{
	ifstream fInput("A-small-attempt2.in", ios::in); //change it
	ofstream fOutput("answer.in", ios::out); //change it
	int caseNumber, answer1, answer2, deck1[4][4], deck2[4][4], bs, matches, card;

	fInput>>caseNumber;
	for(unsigned count=0; count<caseNumber; count++)
	{
		fInput>>answer1;
		for(unsigned count2=0; count2<4; count2++)
		{
			for(unsigned count3=0; count3<4; count3++)
				fInput>>deck1[count2][count3];
		}
		fInput>>answer2;
		for(unsigned count2=0; count2<4; count2++)
		{
			for(unsigned count3=0; count3<4; count3++)
				fInput>>deck2[count2][count3];	
		}
		matches=0;
		for(unsigned count2=0; count2<4; count2++)
		{
			for(unsigned count3=0; count3<4; count3++)
			{
				if(deck1[answer1-1][count2]==deck2[answer2-1][count3])
				{
					++matches;
					card=deck1[answer1-1][count2];
				}
			}
		}
		fOutput<<"Case #"<<count+1<<":"<<" ";

		if(matches==1)
			fOutput<<card<<'\n';
		else if(matches==0)
			fOutput<<"Volunteer cheated!"<<'\n';
		else
			fOutput<<"Bad magician!"<<'\n';

	}


}