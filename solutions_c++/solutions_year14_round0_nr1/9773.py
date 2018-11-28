#include <iostream>

using namespace std;

int main(){
	int t;
	int value1,value2;
	int matrix[4][4],matrix2[4][4];
	int count;
	int chosen;

	while(cin >> t){
		for(int l=0;l<t;l++){
				count = 0;
				chosen = 0;
				cin >> value1;			
			 //ler matrix 1 
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
						cin >> 	matrix[i][j];
				}
			}
			
			cin >> value2;	
			//ler matrix2
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
						cin >> 	matrix2[i][j];
				}
			}
	
			for(int i=0;i<4;i++){
				for(int h  =0;h<4;h++){
					if(matrix[value1-1][i] == matrix2[value2-1][h]){
							count++;
							chosen = matrix[value1-1][i];
					}
				}
			}

			cout << "Case #"<<l+1<<": ";
			if(count == 1)
				cout << chosen;
			if(count == 0)
				cout << "Volunteer cheated!";
			if(count > 1)
				cout << "Bad magician!";
			cout << endl;

		}
	}


	return  0;
}
