#include <iostream>
#include <fstream>
#include <vector>
using namespace std;


int firstDeck[4][4];
int secondDeck[4][4];
int theCard;


int checkDecks(int firstRow,int secondRow)
{
	int count=0;
	for (int i=0; i<4; i++){
		for (int j=0; j<4; j++){
			if (firstDeck[firstRow][i] == secondDeck[secondRow][j]){
				theCard = firstDeck[firstRow][i];
				count++;
			}
		}		
	}
	
	return count;
}




int main()
{
	ifstream cin("A-small-attempt0.in");
	ofstream cout("sevag_ProbA_out.txt");

	int T;
	

	cin>>T;
	int firstRow, secondRow;

	for (int t=1; t<=T; t++)
	{
		cin>>firstRow;
		firstRow--;
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>firstDeck[i][j];
				
		cin>>secondRow;
		secondRow--;	
		for (int i=0; i<4; i++)
			for (int j=0; j<4; j++)
				cin>>secondDeck[i][j];
				
		int ans = checkDecks(firstRow, secondRow);
		
		cout<<"Case #"<<t<<": ";
		if (ans == 1)
			cout<<theCard<<endl;
		if (ans == 0)
			cout<<"Volunteer cheated!"<<endl;
		if (ans > 1)
			cout<<"Bad magician!"<<endl;
	}


	return 0;
}
