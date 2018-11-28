#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<fstream>
#include<sstream>
#include<stack>
#include<math.h>
using namespace std;

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);


	short grid1[4][4];
	short grid2[4][4]; 
	short numberOfCases;
	short choice1;
	short choice2;
	short result;
short nOfmatch = 0;

	cin>>numberOfCases;
	short index =0;
	while(index < numberOfCases)
	{
		cin>>choice1;
		choice1--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>grid1[i][j];
		
		cin>>choice2;
		choice2--;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				cin>>grid2[i][j];
		
		bool match[4] = {false,false,false,false};

		(grid1[choice1][0] == grid2[choice2][0])? match[0] = true: match[0] = false;
		(grid1[choice1][1] == grid2[choice2][1])? match[1] = true: match[0] = false;
		(grid1[choice1][2] == grid2[choice2][2])? match[2] = true: match[0] = false;
		(grid1[choice1][3] == grid2[choice2][3])? match[3] = true: match[0] = false;

	
			
			for(int i=0; i<4; i++){
				
				for(int j=0; j<4; j++)
				{
					if(grid1[choice1][i] == grid2[choice2][j])
					{
						nOfmatch++;
						result = grid1[choice1][i];
					}
				}
			}
			if(nOfmatch>1)
				cout<<"Case #"<<index+1<<": Bad magician!"<<endl;
			else if(nOfmatch == 0)
				cout<<"Case #"<<index+1<<": Volunteer cheated!"<<endl;
			else
				cout<<"Case #"<<index+1<<": "<<result<<endl;
			nOfmatch = 0;
			index++;
	}
}