#include <iostream>
#include <fstream>

using namespace std;

int maxi, nFriends, nCases, nStand, shyness, nPeople;
char c;

int main(void){
	cin >> nCases;
	ofstream out("out.txt");
	for(int i=1; i <= nCases; i++){
		cin >> maxi;
		cin.ignore();
		nFriends = nStand = 0;
		for(shyness = 0; shyness<=maxi; shyness++){
			c = cin.get();
			//cout << "C= " << c << endl;
			nPeople = c-'0';
			if(nStand < shyness){
				nFriends+=(shyness - nStand);
				nStand = shyness +  nPeople;
			}
			else{
				nStand+=nPeople;
			}
		}
		out << "Case #" << i << ": " << nFriends << endl;
	}
	out.close();
}