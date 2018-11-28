#include<iostream>
using namespace std;


int main(){

	int T,row1 ,t =0, row2 ,mat1[4][4] , mat2[4][4];
	cin>>T;
	while(t<T){
		cin>>row1;
		for(int i = 0;i<4;i++){
			for(int j=0 ;j< 4;j++){
				cin>>mat1[i][j];
			}
		}
		cin>>row2;
		for(int i = 0;i<4;i++){
			for(int j=0 ;j< 4;j++){
				cin>>mat2[i][j];
			}
		}
		int count = 0 , obtained = -1;
		for(int j = 0; j<4;j++){
			for(int k = 0;k<4 ; k++){
				if(mat1[row1-1][j] == mat2[row2-1][k]){
					obtained = mat1[row1-1][j];
					count++;
				}
			}
		}
		if(count == 1){
			cout<<"Case #"<<(t+1)<<": "<<obtained<<"\n";
		}
		else if(count>1){
			cout<<"Case #"<<(t+1)<<": Bad magician!\n";
		}
		else
			cout<<"Case #"<<(t+1)<<": Volunteer cheated!\n";
		t++;
	}
	return 0;
}
				
				
