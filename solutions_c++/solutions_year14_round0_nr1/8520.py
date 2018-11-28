#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <iostream>

using namespace std;

int main(){
	ifstream file("in");
	int testcase;
	file >> testcase;
	

	vector<vector<int> > cards;	
	vector<vector<int> > cards2;	
	cards.reserve(4);
	cards2.reserve(4);

	for(int i = 0; i < testcase; i++){
		cards.clear();
		cards2.clear();
		cout<<"Case #"<<i+1<<": ";
		int guess1, guess2;
		int c1, c2, c3, c4;
		file >> guess1;

		for(int j =0 ; j < 4; j++){
			file>> c1>>c2>>c3>> c4;
			vector<int> row;
			row.reserve (4);
			row.push_back(c1);
			row.push_back(c2);
			row.push_back(c3);
			row.push_back(c4);
			cards.push_back(row);
		}

////////////////////////////////////////////////////////////////////
		file >> guess2;

		for(int j =0 ; j < 4; j++){
			file>> c1>>c2>>c3>> c4;
			vector<int> row;
			row.push_back(c1);
			row.push_back(c2);
			row.push_back(c3);
			row.push_back(c4);
			cards2.push_back(row);
		}

		int found = 0; 
		int cardnum; 
		for(int j = 0; j < 4; j++){
			for(int k = 0; k < 4; k++){
			if(cards2[guess2-1][j] == cards[guess1-1][k]){
				found++;
				cardnum = cards[guess1-1][k];
				break;
			}
			}

		}

		if(found == 0)
			cout<<"Volunteer cheated!"<<endl;
		else if (found == 1)
			cout<<cardnum<<endl; 
		else
			cout<<"Bad magician!"<<endl;

	}

	return 0; 
}
