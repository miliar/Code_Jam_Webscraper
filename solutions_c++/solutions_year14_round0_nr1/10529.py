#include <iostream>

using namespace std;

int main () {
	int t;
	cin>>t;
	int count =t;
	int firstRow, secondRow;
	int firstGrid[4][4], secondGrid[4][4];

	while(t--) {
		cin>>firstRow;
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>firstGrid[i][j];	
			}
		}

		cin>>secondRow;		
		for(int i=0;i<4;i++) {
			for(int j=0;j<4;j++) {
				cin>>secondGrid[i][j];	
			}
		}
	/*	for(int i=0;i<4;i++) {
			cout<<firstGrid[firstRow][i];
		}
		cout<<endl;
		for(int i=0;i<4;i++) {
			cout<<secondGrid[secondRow][i];
		}
*/
		int result =-1;		
		for(int j=0;j<4;j++) {
			for(int k=0;k<4;k++) {
				if( firstGrid[firstRow-1][j] == secondGrid[secondRow-1][k]) {
	//				cout<<"firstrow"<<firstRow<<"\t";					
		//			cout<<"secrow"<<secondRow<<"\t";					
			//		cout<<"firstgrid elem"<<firstGrid[firstRow][j]<<"\t";
					if(result == -1) {					
						result = firstGrid[firstRow-1][j];
				//		cout<<"rs"<<result<<endl;
					}	
					else {
					//	cout<<"rs"<<result<<endl;
						result = 0;
						break;

					}
				}
			}
		}
//		cout<<"before swithc"<<endl;
		switch(result) {
			
			case 0:
				cout<<"Case #"<<count-t<<": Bad magician!"<<endl;
				break;
			case -1:
				cout<<"Case #"<<count-t<<": Volunteer cheated!"<<endl;
				break;
			default:
				cout<<"Case #"<<count-t<<": "<<result<<endl;
		}
	}	
	
	return 0;	
	
}
