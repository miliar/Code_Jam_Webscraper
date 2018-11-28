#include <stdio.h>
#include<conio.h>
#include <iostream>

using namespace std;
int main(){
	freopen ("E:/code_jam/A-small-attempt4.in","r",stdin);
	freopen ("E:/code_jam/A-small-attempt4.out","w",stdout);
	int first_row,second_row;
	int result[16];
	int test_case;
	int first_array[4][4],second_array[4][4];
	int final_result,number_of_result;
	cin >> test_case;
	for (int t = 1;t <= test_case;t++){
		final_result = 0;
		number_of_result = 0;
		for(int i = 0; i < 16; i++){
			result[i] = 0;
		}
		
		cin >> first_row;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4;j++){
				cin >> first_array[i][j];
				if ((first_row - 1) == i){
					result[first_array[i][j] - 1] = 1;
				}
			}
		}

		cin >> second_row;
		for(int i = 0; i < 4; i++){
			for(int j = 0; j < 4;j++){
				cin >> second_array[i][j];
				if ((second_row - 1) == i && result[second_array[i][j] - 1] == 1){
					number_of_result++;
					final_result = second_array[i][j];
				}
			}
		}
	
		if (number_of_result == 0){
			cout << "Case #" << t << ": Volunteer cheated!\n";            //Case #3: Volunteer cheated!
		}
		else if(number_of_result > 1){
			cout << "Case #" << t << ": Bad magician!\n";                 //Case #2: Bad magician!
		}
		else{
			cout << "Case #" << t << ": " << final_result << "\n";        //Case #1: 7
		}
	}
	return 0;
}
