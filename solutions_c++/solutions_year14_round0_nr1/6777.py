#include <iostream>
#include <vector>
using namespace std;
int tab[5][5];

int main(){
	int z,n;
	cin >> z;
	for(int k=1;k<=z;k++){
		cin >> n;
		for(int i = 1; i<=4; i++)
			for(int j = 1; j<=4; j++)
				cin >> tab[i][j];
		vector<int> pos,pos2;
		for(int i = 1; i<=4; i++)
			pos.push_back(tab[n][i]);
		
		cin >> n;
		for(int i = 1; i<=4; i++)
			for(int j = 1; j<=4; j++)
				cin >> tab[i][j];
		for(int i = 1; i<=4; i++)
			pos2.push_back(tab[n][i]);
		int card;
		int cards = 0;
		for(int i = 0; i<pos.size();i++)
			for(int j = 0; j<pos2.size(); j++)
				if(pos2[j] == pos[i]){
					card = pos[i];
					cards++;
				}
		cout << "Case #"<<k<<": ";
		switch(cards){
			case 0:
				cout << "Volunteer cheated!" << endl;
				break;
			case 1:
				cout << card << endl;
				break;
			default:
				cout << "Bad magician!" << endl;
		}
	}
}
