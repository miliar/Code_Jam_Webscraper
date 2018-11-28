#include <iostream>
#include <fstream>

bool CheckArr(bool arr[], int arrSize);

int main(){
	int input = 0;
	int numOfCase = 0;
	bool check[10] = { false, };
	int count = 0;
	int index=0;
	int r = 0;

	std::ifstream trainData("A-small-attempt1.in");
	std::ofstream result("result.txt");

	if (trainData.fail()) {
		std::cout << "Failed to open input file" << std::endl;
		exit(1);
	}

	trainData >> numOfCase;
	
	for (int c = 0; c < numOfCase;c++) {
		trainData >> input;
		while (!CheckArr(check, 10) && count < 100) {
			r = input * (count + 1);
			index = r;
			
			while (index > 9) {
				check[index % 10] = true;
				index = index / 10;
			}
			check[index] = true;
			count++;
		}

	

		
	
		if (CheckArr(check, 10)) result << "Case #" << c << ": " << r << std::endl;
		else result << "Case #" << c << ": INSOMNIA" << std::endl;
		count = 0;
		for (int i = 0; i < 10; i++) {
			check[i] = false;
		}
	}

	trainData.close();
	result.close();
}

bool CheckArr(bool arr[],int arrSize){
	bool ret = true;
	for (int i = 0; i < arrSize; i++) {
		if (arr[i] == false) return false;
	}
	return true;
}
