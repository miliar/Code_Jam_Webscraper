#include <iostream>
using namespace std;

int main(){
	int T;
	cin >> T;
	for( int t=1; t<=T; t++){
		cout << "Case #" << t << ": ";
		int ans1, ans2, row[17]={0}, temp;
		int output = -1;
		cin >> ans1;
		for( int r=0; r<4; r++){
			for( int c=0; c<4; c++){
				cin >> temp;
				row[temp] = r;
			}
		}
		cin >> ans2;
		ans2 --;
		ans1 --;
		for( int r=0; r<4; r++){
			for( int c=0; c<4; c++){
				cin >> temp;
				if( r == ans2 ){
					if( row[temp] == ans1 ){
						if( output == -1 ){
							output = temp;
						}else if( output > 0 ){
							output = 0;
						}
					}
				}
			}
		}

		if( output > 0 ){
			cout << output << "\n";
		}else if( output == -1 ){
			cout << "Volunteer cheated!\n";
		}else{
			cout << "Bad magician!\n";
		}
	
	}
}
