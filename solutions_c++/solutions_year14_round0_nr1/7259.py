#include<iostream>
using namespace std;

int main(){
	int t;
	cin >> t;
	int cse = 1;
	while(t--){
		
		int ans1, ans2, c1[4][4], c2[4][4];
		cin >> ans1;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin >> c1[i][j];
			}
		}
		cin >> ans2;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin >> c2[i][j];
			}
		}
		int matches = 0;
        int num;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(c1[ans1-1][i] == c2[ans2-1][j]){
					matches++;
                    num = c1[ans1-1][i];
				}
			}
		}
		if(matches == 0){
			cout << "Case #"<< cse<< ": "<< "Volunteer cheated!" << endl;
		}
		else if(matches == 1){
			cout << "Case #"<< cse<< ": "<< num << endl;
		}else {
			cout << "Case #"<< cse<< ": "<< "Bad magician!" << endl;
		}
		cse++;
	}
}
