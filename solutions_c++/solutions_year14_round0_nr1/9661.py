#include <iostream>
#include <algorithm> 
#include <vector>

using namespace std;

int main(int argc, char *argv[]) {
	vector<int> row(4);
	
	int t, r, card, rep, chosen;
	
	cin >> t;
	
	for(int caso=1; caso<=t;caso++){
		cin >> r;
		r--;
		rep = 0;
		for(int i = 0; i < 4; i++)
		{
			for(int j=0; j < 4; j++){
				cin >> card;
				if(i == r)
					row[j]=card;
			}
		}
		
		cin >> r;
		r--;
		for(int i = 0; i < 4; i++)
		{
			for(int j=0; j < 4; j++){
				cin >> card;
				if(i == r){
					if (find(row.begin(),row.end(),card)!=row.end()){
						chosen=card;
						rep++;
					}
				}
			}
		}
		
		cout << "Case #" << caso << ": ";
		if(rep == 0)	//No hay coincidencia
			cout << "Volunteer cheated!" << endl;
		else if(rep == 1)
			cout << chosen << endl;
		else 
			cout << "Bad magician!" << endl;
		
	}
	
	return 0;
}

