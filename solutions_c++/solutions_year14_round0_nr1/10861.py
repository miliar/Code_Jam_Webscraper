#include <iostream>
#include <set>
using namespace std;

int main(int argc, char** arv) {
	unsigned int numTests = 0;
	cin>>numTests;
	for(unsigned int i = 1; i <= numTests; i++)
	{
		unsigned firstRow = 0;
		cin>>firstRow;
		unsigned int temp = 0;
		unsigned int firstSel = 0;
		for(unsigned int k = 1; k <= 4; k++)
		{
			for(unsigned int w = 0; w < 4; w++)
			{
				cin>>temp;
				if(k == firstRow)
				{
					firstSel |= (1 << temp);
				}
			}
		}
		cin>>firstRow;
		for(unsigned int k = 1; k <= 4; k++)
		{
			unsigned int matches  = 0;
			unsigned  int selected = 0;
			for(unsigned int w = 0; w < 4; w++)
			{
				cin>>temp;
				if(k == firstRow)
				{
					if(firstSel & ( 1 << temp))
					{
						selected = temp;
						matches += 1;
					}
				}
			}
			if(k == firstRow)
			{
					if(matches == 1)
						cout<<"Case #"<<i<<": "<<selected<<endl;
					else if(matches > 1)
						cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
					else
						cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;
			}
		}
	}
	// your code goes here
	return 0;
}
