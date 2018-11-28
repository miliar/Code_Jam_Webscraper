#include <iostream>
#include <fstream>
using namespace std;

int main(){
	int deck1[16];
	int deck2[16];
	int row1, row2;
	int tests;
	cin >> tests;
	int i, j;
	for(i = 0; i < tests; i++){
		cin>>row1;
		for(j = 0; j < 16; j++)
			cin >> deck1[j];
		cin>>row2;
		for(j = 0; j < 16; j++)
			cin >> deck2[j];
		int deck1passed = ((row1-1)*4);
		int deck2passed = ((row2-1)*4);
		int n = 0;
		int card = 0;
		int k;
		for(j = deck1passed; j < deck1passed+4; j++){
			for(k = deck2passed; k < deck2passed+4; k++){
				if(deck1[j] == deck2[k]){
					n++;
					card = deck2[k];
				}
			}
		}
		if(n == 1)
			cout << "Case #"<<i+1<<": "<<card<<"\n";
		else if(n  == 0)
			cout << "Case #"<<i+1<<": Volunteer cheated!\n";
		else
			cout << "Case #"<<i+1<<": Bad magician!\n";
		}
	return 0;
	}
