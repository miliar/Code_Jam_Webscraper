# include <iostream>

using namespace std;

int main()
{
	int noOfTricks,patren1[4][4],patren2[4][4],i,j,trueCase=0,row1,row2,card=-1;
	cin>>noOfTricks;
	
	for(int itr=1;itr<=noOfTricks;itr++)
	{
		trueCase=0;
		cin>>row1;
		row1--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>patren1[i][j];
		cin>>row2;
		row2--;
		for(i=0;i<4;i++)
			for(j=0;j<4;j++)
				cin>>patren2[i][j];

		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(patren1[row1][i]==patren2[row2][j])
				{
					card=patren1[row1][i];
					trueCase++;
				}
			}
		}

		if(trueCase==0)
			cout<<"Case #"<<itr<<": Volunteer cheated!"<<endl;
		else if(trueCase==1)
			cout<<"Case #"<<itr<<": "<<card<<endl;
		else if(trueCase>1)
			cout<<"Case #"<<itr<<": Bad magician!"<<endl;

	}
	return 0;
}