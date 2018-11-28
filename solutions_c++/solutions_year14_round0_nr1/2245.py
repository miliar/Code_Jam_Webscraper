#include <iostream>
#include <fstream>

using namespace std;

int main(){
	ifstream input("A-small-attempt0.in");
	ofstream output("A-small-attempt0.out");
	int t, cs = 1;
	input >> t;
	
	while(t--){
		int r1, r2;
		int conf1[4][4], conf2[4][4];
		
		input >> r1;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				input >> conf1[i][j];
				
		input >> r2;
		for(int i=0; i<4; i++)
			for(int j=0; j<4; j++)
				input >> conf2[i][j];
				
		int ans = -1, n = 0;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(conf1[r1-1][i]==conf2[r2-1][j]){
					ans = conf1[r1-1][i]; 
					n++;
				}
			}
		}
		
		output << "Case #" << cs << ": ";
		if(n==0)
			output << "Volunteer cheated!" << endl;
		else if(n==1)
			output << ans << endl;
		else
			output << "Bad magician!" << endl;
		
		cs++;
	}
	return 0;
}
