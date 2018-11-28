#include <fstream>
#include <iostream>

using namespace std;

	int arr[4][4];
	void show(){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				cout << arr[i][j];
			}
			cout << endl;
		}
	}
	
	
	bool checkRow(int val){
		bool check = true;
		for(int j=0;j<4 ;j++){
			check = true;
			for(int i=0;i<4 && check ;i++){
				if(arr[i][j] != val && arr[i][j] != 1){
					check = false;
	//				cout << arr[i][j] << ' ' << i << ' ' << j << endl;
				}
			}
			if(check){
//				cout << "Returning True" << endl;
				return true;
			}
			
		}
			return false;
	}
	
	bool findZero(){
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(arr[i][j] == 0)
					return true;
		return false;
	}

	bool checkCol(int val){
		bool check = true;
		for(int i=0;i<4 ;i++){
			check = true;
			for(int j=0;j<4 && check ;j++){
				if(arr[i][j] != val && arr[i][j] != 1){
					check = false;
				}
		
		}
			if(check)
				return true;
	
	}
				return false;
	
	}
	
	bool checkDiag1(int val){

		for(int i=0;i<4;i++){
			if(arr[i][i] != val && arr[i][i] != 1)
			{
				return false;
			}
		}
		return true;
	}

	bool checkDiag2(int val){

		for(int i=0;i<4;i++){
			if(arr[i][3-i] != val && arr[i][3-i] != 1)
			{
				return false;
			}
		}
		return true;
	}


	
	bool checkDiag(int val){
		return (checkDiag1(val) || checkDiag2(val));
	}
/*
	X pe 2
	0 pe 3
	. pe 0
	T pe 1
*/
int main(){

	int testcase = 0;
	char c;
	ifstream fin;
	ofstream cout("sonyc.out");
	fin.open("input.txt");
	
	fin >> testcase;
//	cout << "Test Case " << testcase << endl;
	for(int k=0;k<testcase;k++){
		
	/*	for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				arr[i][j] = 0;*/
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				fin >> c;
				switch(c){
					case 'X':
						arr[i][j] = 2;
						break;
					case 'O':
						arr[i][j] = 3;
						break;
					case '.':
						arr[i][j] = 0;
						break;
					case 'T':
						arr[i][j] = 1;
						break;
						
				}
			}
		}
//		show();
		cout << "Case #" << k+1 << ": ";
		// 
		if(checkCol(2) || checkRow(2) ||checkDiag(2))
			cout << "X won" << endl;
		else if(checkCol(3) || checkRow(3) || checkDiag(3))
			cout << "O won" << endl;
		else if(findZero())
			cout << "Game has not completed" << endl;
		else
			cout << "Draw" << endl;;
		
	
	}
	system("pause");
	return 0;
}
