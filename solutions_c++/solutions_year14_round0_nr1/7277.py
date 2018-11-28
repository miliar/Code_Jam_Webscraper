#include <iostream>
#include <cstdio>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int cas=1;cas<=T;cas++)
	{
		int a[17] = {0,};
		int x,matrix[4][4];
		cin >> x;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> matrix[i][j];
			}
		}
		for(int i=0;i<4;i++)
			a[ matrix[x-1][i] ]++;
		
		cin >> x;


		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				cin >> matrix[i][j];
			}
		}
		for(int i=0;i<4;i++)
			a[ matrix[x-1][i] ]++;
		
		bool bittimi=false;
		bool oldumu= false;
		int winner;

		

		for(int i=1;i<17;i++)
		{
			if( a[i] == 2 )
			{	
				if( oldumu == false )
				{
					winner = i;
					oldumu=true;
				}
				else
				{
					cout << "Case #"<<cas<<": Bad magician!"<< endl;
					i = 17;
					bittimi=true;
				}
			}
		}
		if( !bittimi )
		{
			if( oldumu)
			{
				cout << "Case #"<<cas<<": " << winner << endl;
			}
			else
				cout << "Case #"<<cas <<": Volunteer cheated!" << endl;
		}
	}
	return 0;
}