#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

int main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("out.txt");
	int caseCount;
	vector<int> answers;
	in>>caseCount;
	
	for(int i=0;i<caseCount;i++)
	{
		int rowNumber;
		in>>rowNumber;
		vector<int> cards;
		int card;
		for(int i=0;i<16;i++)
		{
			in>>card;
			if((i/4 + 1) == rowNumber)
			{
				cards.push_back(card);
			}
		}
		in>>rowNumber;
		for(int i=0;i<16;i++)
		{
			in>>card;
			if((i/4 + 1) == rowNumber)
			{
				cards.push_back(card);
			}
		}
		int equalsCount = 0;
		for(int i=0;i<cards.size();i++)
		{
			for(int j=0;j<cards.size();j++)
			{
				if(i!=j && cards[i] == cards[j])
				{
					equalsCount++;
					card = cards[i];
				}
			}
		}
		equalsCount/=2;
		if(equalsCount == 0)
		{
			answers.push_back(-1);
		}
		else if(equalsCount > 1)
		{
			answers.push_back(-2);
		}
		else
		{
			answers.push_back(card);
		}
	}

	for(int i=0;i<answers.size();i++)
	{
		if(answers[i] == -1)
		{
			out<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
		else if(answers[i] == -2)
		{
			out<<"Case #"<<i+1<<": Bad magician!"<<endl;
		}
		else
		{
			out<<"Case #"<<i+1<<": "<<answers[i]<<endl;
		}
	}
	return 0;
}