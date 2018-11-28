
#include <cstdio>
#include <iostream>

using namespace std;

int T, row1, row2;
int before[4][4], after[4][4];
int choice1[4], choice2[4];

int card;

int numChoices()
{
	int choices = 0;
	
	for(int j = 0; j < 4; j++) {
		choice1[ j ] = before[ row1-1 ][j];
		choice2[ j ] = after[ row2-1 ][j];
   }
	
	for(int i = 0; i < 4; i++)  {
		for(int j = 0; j < 4; j++)  {
			if(choice1[i] == choice2[j]) 
			{
				card = choice1[i];
				choices++;
			}
		}
	}
	
	return choices;
}

int main()
{
	freopen("magic.in", "r", stdin);
   freopen("magic.out", "w", stdout); 
	
	cin >> T;
	for(int i = 0; i < T; i++)
	{
		cin >> row1;
		
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				cin >> before[j][k];
			}
		}
		
		cin >> row2;
		
		for(int j = 0; j < 4; j++) {
			for(int k = 0; k < 4; k++) {
				cin >> after[j][k];
			}
		}
		
		printf("Case #%d: ", i+1);
		
		switch( numChoices() )
		{
			case 0:
				cout << "Volunteer cheated!";
				break;
			
			case 1:
				cout << card;
				break;
			
			default:
				cout << "Bad magician!";
				break;
		}
		
		cout << "\n";
	}
	
	return 0;
}

