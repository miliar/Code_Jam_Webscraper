#include <iostream>
#include <fstream>
using namespace std;
struct input {
	int pos;
	int arr[4][4];
};
void read(){
	input *input1, *input2;
	int input_number;
	ifstream file("A-small-attempt2.in");
	file >> input_number;
	input1 = new input[input_number];
	input2 = new input[input_number];
	for (int i = 0; i < input_number; i++){
		file >> input1[i].pos;
		for (int m = 0; m < 4; m++){
			for (int k = 0; k < 4; k++)
				file >> input1[i].arr[m][k];
		}
		file >> input2[i].pos;
		for (int m = 0; m < 4; m++){
			for (int k = 0; k < 4; k++)
				file >> input2[i].arr[m][k];
		}
	}
	file.close();
	ofstream fileout ("A-small-attempt2.out");
	for (int i = 0; i < input_number; i++){
		int fix1[4],fix2[4];
		int key=-1;
		bool check = false;
		for (int j = 0; j < 4; j++){
			fix1[j] = input1[i].arr[input1[i].pos - 1][j];
		}
		for (int j = 0; j < 4; j++)
			fix2[j] = input2[i].arr[input2[i].pos - 1][j];
		bool check2 = false;
		for (int m = 0; m < 4; m++){
			for (int k = 0; k < 4; k++){
				if (fix1[m] == fix2[k])
					check2 = true;
			}
		}
		if (!check2){
				fileout << "Case #" << i + 1 << ": Volunteer cheated!";
				if (i != (input_number - 1))
					fileout << "\n";
				check = true;
		}
		if (!check){
			for (int m = 0; m < 4; m++){
				for (int k = 0; k < 4; k++)
				{
					if (fix1[m] == fix2[k]){
						if (key != -1){
							fileout << "Case #" << i + 1 << ": Bad magician!";
							if (i != (input_number - 1))
								fileout << "\n";
							check = true;
							break;
						}
						key = fix1[m];
					}
				}
				if (check)
					break;
			}
			if (!check){
					fileout << "Case #" << i + 1 << ": " << key;
					if (i != (input_number - 1))
						fileout << "\n";
			}
		}
	}
	fileout.close();
}
int main(){
	read();
	return 0;
}