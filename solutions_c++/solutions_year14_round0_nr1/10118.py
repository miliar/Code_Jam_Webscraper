#include<iostream>

using namespace std;

int main()
{
	int t = 0;
	int ans1 = 0;
	int ans2 = 0;
	int matrix1[4][4];
	int matrix2[4][4];
	int noOfMatches = 0;
	int matchedNo = 0;
	int caseNo = 1;

	cin>>t;
	
	while ( caseNo <= t){

	cin>>ans1;

	for ( int i = 0; i < 4; i++ )
	{
		for ( int j =0; j < 4; j++ )
		{
			cin>> matrix1[i][j];
		}
	}

	cin>>ans2;

	for ( int i = 0; i < 4; i++ )
	{
		for ( int j =0; j < 4; j++ )
		{
			cin>> matrix2[i][j];
		}
	}

	noOfMatches = 0;

	for ( int i = 0; i< 4; i++)
	{
		for ( int j = 0; j<4; j++ )
		{
			if ( matrix1[ans1-1][i] == matrix2[ans2-1][j] )
			{
				matchedNo = matrix1[ans1-1][i];
				noOfMatches++;
			}
		}
	}

	if( noOfMatches == 0 )
	{
		cout<<"Case #"<<caseNo<<": Volunteer cheated!"<<endl;
	}
	else{

		if( noOfMatches>1 )
		{
			cout<<"Case #"<<caseNo<<": Bad magician!"<<endl;
			
		}
		else{
			cout<<"Case #"<<caseNo<<": "<<matchedNo<<endl;
		}
	}

	caseNo++;

	}

	return 0;
}
