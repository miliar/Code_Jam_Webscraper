#include <iostream>
using namespace std;

int main() {
	int T=0,A1=0,A2=0,c=0,A3=0;
	int oline [4][4];
	int nline [4][4];
	
	cin >> T;
	for(int i=1;i<=T;i++){
		A1=0,A2=0,c=0,A3=0;
		cin >> A1;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin >> oline[j][k];
			}
		}
		cin >> A2;
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin >> nline[j][k];	
			}
		}
	
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				if(oline[A1-1][j]==nline[A2-1][k]){
					if(c==0&&A3==0){
						c=1;
						A3=oline[A1-1][j];
					}
					else if(c!=0||A3!=0){
						c=2;
					}
					else{
						cout << "Error #1" << endl;
					}
				}
			}
		}
		
		switch (c) {
  			case 1:
    			cout << "Case #"<<i<<": " << A3 << endl;
    			break;
  			case 2:
    			cout << "Case #"<<i<<": Bad magician!" << endl;
    			break;
  			default:
    			cout << "Case #"<<i<<": Volunteer cheated!" << endl;
  		}
	}
	return 0;
}