#include <iostream> 
#include <fstream> 

using namespace std;

void readToArray(int arr[][4], ifstream *file){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			*file >> arr[i][j];
		}
	}
}

void copyRow(int arr[][4], int sel_row[], int row){
	for(int i = 0; i < 4; i++){
		sel_row[i] = arr[row][i];
	}
}

void displayArray(int arr[][4]){
	for(int i = 0; i < 4; i++){
		for(int j = 0; j < 4; j++){
			cout << arr[i][j] << " ";
		}
		cout << "\n";
	}
	cout << "\n";
}

int main() {	
	ifstream input("A-small-attempt3.in");
	ofstream output("output.ou");
	int sets, row, n;
	int arr[4][4];
	int sel_row[4];
	
	if(input.is_open()){
		input >> sets;
		n = 1;
		
		while(sets > 0){
		
			input >> row;
			readToArray(arr, &input);
			copyRow(arr, sel_row, row - 1);
		
			cout << "Selected row is " << row << "\n";
			displayArray(arr);
		
			for(int i = 0; i < 4; i++){
				cout << sel_row[i] << " ";
			}
			cout << "\n\n";
		
			input >> row;
			readToArray(arr, &input);
			
			cout << "Selected row is " << row << "\n";
			displayArray(arr);
		
			int match = 0;
			int card = 0;
			for(int i = 0; i < 4; i++){
				for(int j = 0; j < 4; j++){
					if(sel_row[j] == arr[row - 1][i]){
						card = sel_row[j];
						match++;
					}
				}
				cout << "\n";
			}
		
			cout << "Case #" << n << ": ";
			output << "Case #" << n << ": ";
			if(match == 0){
				cout << "Volunteer cheated!\n";
				output << "Volunteer cheated!\n";
			}
			else if(match == 1){
				cout << card << "\n";
				output << card << "\n";
			}
			else{
				cout << "Bad magician!\n";
				output << "Bad magician!\n";	
			}
			cout << "\n\n";
			
			sets--;
			n++;
			//if(n == 10) break;
		}
		
		
		input.close();
		output.close();
	}
	
	return 0; 
}
