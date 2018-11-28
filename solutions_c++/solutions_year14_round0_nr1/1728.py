#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<set>

using namespace std;

int main(){
	int t, count = 1, r, temp;
	int cards, card;
	cin >> t;
	set<int> selected;
	
	while(t--){
		selected.clear();
		cards = 0;
		
		cin >> r;
		for(int i = 1; i < r; i++){
			for(int j = 0; j < 4; j++){
				cin >> temp;
			}
		}
		for(int i = 0; i < 4; i++){
			cin >> temp;
			selected.insert(temp);
		}
		for(int i = r+1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> temp;
			}
		}

		cin >> r;
		for(int i = 1; i < r; i++){
			for(int j = 0; j < 4; j++){
				cin >> temp;
			}
		}
		for(int i = 0; i < 4; i++){
			cin >> temp;
			if(selected.count(temp) > 0) {
				card = temp;
				cards++;
			}
		}
		for(int i = r+1; i <= 4; i++){
			for(int j = 0; j < 4; j++){
				cin >> temp;
			}
		}
		
		cout << "Case #" << count++ << ": ";
		if(cards > 0){
			if(cards == 1){
				cout << card << endl;
			} else {
				cout << "Bad magician!" << endl;
			}
		} else {
			cout << "Volunteer cheated!" << endl;
		}
	}
	
	return 0;
}

