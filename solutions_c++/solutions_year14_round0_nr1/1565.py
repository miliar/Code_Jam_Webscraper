#include<iostream>
using namespace std;

int main()
{
	int t; cin >> t;
	
	for(int i=1; i<=t; i++)
	{
		int a1; cin >> a1; a1--;
		
		int cards1[4][4];
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> cards1[j][k];
	
		int a2; cin >> a2; a2--;
		
		int cards2[4][4];
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				cin >> cards2[j][k];
	
		//program
		
		int zhoda=0, card=0;
		for(int j=0; j<4; j++)
			for(int k=0; k<4; k++)
				if(cards1[a1][j] == cards2[a2][k]) 
				{	
					zhoda++;
					card = cards1[a1][j];
				}
				
		if(zhoda == 1) cout << "Case #" << i << ": " << card << endl;
		else if(zhoda > 1) cout << "Case #" << i << ": Bad magician!" << endl;
		else cout << "Case #" << i << ": Volunteer cheated!" << endl;
		
	}
	
	return 0;	
}





