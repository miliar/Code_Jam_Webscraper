#include <iostream>
#include<fstream>
#include <vector>
using namespace std;
void main(){
	ifstream file("A-large.in");
	//grabbing number of testcases
	int numoftest;
	file >> numoftest;
	bool exit = false;
	int num1 = 10000;
	int num = num1;
	int last_digit = 0;
	int multiplier=2;
	int arrnum[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	ofstream file2("result.txt");
	for (int i = 0; i < numoftest; i++){
		file >> num1;
		num = num1;
		if (num1 == 0){
			//cout << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
			
			file2 << "Case #" << i + 1 << ": " << "INSOMNIA" << endl;
		}
		else{
			while (!exit){

				//finding number of numbers in the number
				//cout << num<<endl;
				int counter = 0;
				int divider = 10;
				for (int i = 0; i < num; i++){
					int x = num / divider;
					if (x == 0){
						break;
					}
					counter++;
					divider = 10 * divider;
				}

				vector<int> numbers;
				int modifynum = num;
				int extracted_number;
				for (int i = 0; i < counter + 1; i++){
					extracted_number = modifynum % 10;
					numbers.push_back(extracted_number);
					modifynum = modifynum / 10;
				}

				//extracted_num contains all the numbers of the digit now
				//checking if the numbers cancel any number
				for (int i = 0; i < 10; i++){
					for (int j = 0; j < numbers.size(); j++){
						if (arrnum[i] == numbers[j]){
							arrnum[i] = -1;
						}
					}
				}
				//checking if all the numbers have been met
				
				for (int i = 0; i < 10; i++){
					if (arrnum[i] == -1){
						exit = true;
						//printing number in numbers

						last_digit = num;
					}
					else{
						exit = false;

						break;
					}
				}
				num = multiplier * num1;
				multiplier++;
				numbers.clear();

			}

			//cout << "Case #" << i + 1 << ": " << last_digit << endl;
			file2 << "Case #" << i + 1 << ": " << last_digit << endl;
			exit = false;
			for (int i = 0; i < 10; i++){
				arrnum[i] = i;
			}
			multiplier = 2;
		}
	}
}