#include <iostream>
#include <cstdlib>


using namespace std;
int main() {
	int t;
	cin >> t;
	int ans=0;
	for(int i=0; i<t; i++){
		int r1,r2;
		int deck[4][4];
		int a1[4];
		int a2[4];
		cin >> r1;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				cin >> deck[j][k];
				if(j==r1-1) a1[k] = deck[j][k];
			}
		}
		cin >> r2;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				cin >> deck[j][k];
				if(j==r2-1) a2[k] = deck[j][k];
			}
		}
		int count = 0;
		for(int x=0; x<4; x++){
			for(int y=0; y<4; y++){
				if(a1[x] == a2[y]){
					count++;
					ans = a1[x];
				}
			}	
		}
		if(count==1) cout << "Case #" << i+1 << ": " << ans << endl;
		if(count==0) cout << "Case #" << i+1 << ": " << "Volunteer cheated!" << endl;
		if(count>1)  cout << "Case #" << i+1 << ": " << "Bad magician!" << endl;
	}

	return 0;
}