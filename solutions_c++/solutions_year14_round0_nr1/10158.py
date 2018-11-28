#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ifstream f;
	ofstream of;
	
	f.open("input.txt");
	of.open("output.txt");
	int size;
	f>>size;
	
	for(int i = 0; i< size ; i++){
		
		int first_row;
		f>>first_row;
		
		
		int matrix1[4][4];
		
		for(int j = 0 ; j < 4 ; j++){
			
			for(int k = 0; k < 4 ; k++){
				
				f>>matrix1[j][k];
			}
		}


		int second_row;
		f>>second_row;

		int matrix2[4][4];
		
		
		for(int j = 0 ; j < 4 ; j++){
			
			for(int k = 0; k < 4 ; k++){
				
				f>>matrix2[j][k];
			}
		}
		
		
		
		int count = 0;
		int number = 0;
		
		for(int x= 0 ;x<4;x++){
			for(int y= 0 ;y<4;y++){
				if(matrix1[first_row-1][x] == matrix2[second_row-1][y]){
					count++;
					number = matrix2[second_row-1][y];
				}
			}
		}
		
		if(count == 1){
			of<<"Case #"<<i+1<<": "<<number;
		}
		else if (count == 0){
			of<<"Case #"<<i+1<<": "<<"Volunteer cheated!";			
		}
		else{
			of<<"Case #"<<i+1<<": "<<"Bad magician!";
		}
		
		of<<endl;
		
		
	}
	
	
	return 0;
}
