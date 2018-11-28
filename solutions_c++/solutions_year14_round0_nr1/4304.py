#include <iostream>
using namespace std;

int main()
{
	int ntest,correct,guess1,guess2,arrange1[4][4],arrange2[4][4],index;
	correct = 0,index = 0 ;
	cin>>ntest;
	
	for(int k = 0; k<ntest; k++)
	{
		cin>>guess1;
		for(int i = 0; i<4; i++)
			for(int j= 0; j<4; j++)
				cin>>arrange1[i][j];
				
			
		cin>>guess2;
		for(int i = 0; i<4; i++)
			for(int j= 0; j<4; j++)
				cin>>arrange2[i][j];

		for(int i = 0; i<4; i++)
			for(int j = 0; j<4; j++)
				if(arrange1[guess1-1][i] == arrange2[guess2-1][j])
				{
					correct++;
					index = i;
				}
		cout<<"Case #" << k+1 << ": " ;
		if(correct == 1)
		{
			cout<<arrange1[guess1-1][index]<<endl;
		}
		else if(correct > 1)
		{
			cout<<"Bad magician!"<<endl;
		}
		else
		{
			cout<<"Volunteer cheated!"<<endl;
		}
		correct = 0;
	}
}
