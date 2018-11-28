#include <iostream>
using namespace std;
int main(){
	int tests;
	cin>>tests;
	int first[4][4];
	int second[4][4];
	int row1, row2;
	for(int ncase=1; ncase<=tests; ncase++){
		cin>>row1;
		for(int i=0; i<4; i++){
			for (int j = 0; j < 4; j++){
				cin>>first[i][j];	
			}
		}
		cin>>row2;
		for(int i=0; i<4; i++){
			for (int j = 0; j < 4; j++){
				cin>>second[i][j];	
			}
		}
		
		int count_intersect=0;
		int no;
		for(int i=0; i<4; i++){
			for(int j=0; j<4; j++){
				if(first[row1-1][i]==second[row2-1][j]){
					count_intersect++;
					no = first[row1-1][i];
				}
			}
		}
		cout<<"Case #"<<ncase<<": ";
		if(count_intersect >1){
			cout<<"Bad magician!";
		}				
		else if(count_intersect == 1){
			cout<<no;
		}
		else cout<<"Volunteer cheated!";

		cout<<endl;
	}
}