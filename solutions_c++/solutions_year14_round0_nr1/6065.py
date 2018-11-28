#include<bits/stdc++.h>

using namespace std;

int main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T, t=0;
	cin >> T;
	while(T--){
		vector<int> card, card1;
		int p, q;
		cin >> p;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				cin >> q;
				if(i==p) card.push_back(q);
			}
		}
		cin >> p;
		for(int i=1; i<=4; i++){
			for(int j=1; j<=4; j++){
				cin >> q;
				if(i==p){
					for(int k=0; k<card.size(); k++){
						if( card[k]==q )card1.push_back(q);
					}
				}
			}
		}
		
		cout << "Case #" << ++t << ": ";
		if(card1.size()==1) cout << card1[0] << endl;
		else if(card1.size()==0) cout << "Volunteer cheated!" << endl;
		else cout << "Bad magician!" << endl;
		
	}
	return 0;
}
