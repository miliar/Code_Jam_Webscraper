#include <bits/stdc++.h>

using namespace std;

int main(){

	int cards[4][4];

	int T;
	cin>>T;
	for(int k=1; k<=T; k++){
		int r1, r2;
		int sel[4];
		cin>>r1;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>> cards[i][j];
			}
		}

		for(int i=0 ; i<4; i++){
			sel[i]=cards[r1-1][i];
		}

		cin>>r2;

		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				cin>> cards[i][j];
			}
		}

		int matches=0;
		int c=-1;

		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(sel[i]==cards[r2-1][j]){
					matches++;
					c=sel[i];
				}
			}
		}

		if(matches>1){
			printf("Case #%d: Bad magician!\n", k);
		}
		else if(matches<1){
			printf("Case #%d: Volunteer cheated!\n", k);

		}
		else{
			printf("Case #%d: %d\n", k, c);
		}


	}

}