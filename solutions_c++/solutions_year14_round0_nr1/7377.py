#include<iostream>
#include<fstream>

#define FILENAME "A-small-attempt3.in"

using namespace std;

int **firstArr;
int **secondArr;
int ***arr;
fstream fin(FILENAME);

void inputArrangment(int n){
	for(int i = 0;i < 4;i++){
		for(int j = 0;j < 4;j++){
			fin >> arr[n][i][j];
		}
	}
}

void magicShow(int numOfTime){
	int idxOne,idxTwo,result,count = 0;
	fin >> idxOne;
	inputArrangment(0);
	fin >> idxTwo;
	inputArrangment(1);
	
	for(int i = 0;i < 4;i++){
		for(int j = 0;j < 4;j++){
			if(secondArr[idxTwo - 1][i] == firstArr[idxOne - 1][j]){
				result = secondArr[idxTwo - 1][i];
				count++;
			}
		}
	}
	
	cout << "Case #" << numOfTime << ": ";
	if(count == 0){
		cout << "Volunteer cheated!" << endl;
	}else if(count == 1){
		cout << result << endl;
	}else{
		cout << "Bad magician!" << endl;
	}
}

int main(){
	arr = new int**[4];
	firstArr = new int*[4];
	secondArr = new int*[4];
	arr[0] = firstArr;
	arr[1] = secondArr;

	for(int i = 0;i < 4;i++){
		firstArr[i] = new int[4];
		secondArr[i] = new int[4];
	}

	int count = 0;
	int i = 1;
	fin >> count;

	while(i <= count){
		magicShow(i++);
	}

	fin.close();

	return 0;
}
