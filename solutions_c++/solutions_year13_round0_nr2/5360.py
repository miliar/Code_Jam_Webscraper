#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

void cut(int& grass, int height){
	if(grass > height) grass = height;
}

int main(int argc, char const *argv[]){
	if(argc != 2){
		cout<<"Error in Input"<<endl;
		return 0;
	}
	ifstream inFile;
	ofstream outFile;
	inFile.open(argv[1]);
	outFile.open("output.txt", ios::trunc | ios::out);
	if(!(inFile.is_open() && outFile.is_open()) ){
		cout << "can't open files"<<endl;
		return 0;
	}

	int N;
	int height, width;
	bool possible;
	inFile >> N;
	cout << "Running through " << N << " Iterations" << endl;
	for(int count=0; count<N; count++){
		//Initialize
		inFile >> height;
		inFile >> width;
		possible = true;
		int idealLawn[height][width];
		int practiceLawn[height][width];
		for(int i=0; i<height; i++){
			for(int j=0; j<width; j++){
				practiceLawn[i][j] = 100;
			}
		}

		//Read in Data
		for(int i=0; i<height*width; i++){
			char tmp;
			inFile >> tmp;
			idealLawn[i/width][i%width] = tmp;
		}

		//Cut the lawns
		for(int i=0; i<height; i++){
			int h = 0;
			for(int j=0; j<width; j++) if(idealLawn[i][j] > h) h = idealLawn[i][j];
			for(int j=0; j<width; j++){
				cut(practiceLawn[i][j], h);
			}
		}
		for(int j=0; j<width; j++){
			int h = 0;
			for(int i=0; i<height; i++) if(idealLawn[i][j] > h) h = idealLawn[i][j];
			for(int i=0; i<height; i++){
				cut(practiceLawn[i][j], h);
			}
		}

		//Compare
		for(int i=0; i<height; i++){
			for(int j=0; j<width; j++){
				possible &= idealLawn[i][j]==practiceLawn[i][j];
			}
		}

		if(possible){
			cout << "Case #" << count+1 << ": " << "YES" << endl;
			outFile << "Case #" << count+1 << ": " << "YES" << endl;
		} else {
			cout << "Case #" << count+1 << ": " << "NO" << endl;
			outFile << "Case #" << count+1 << ": " << "NO" << endl;
		}
	}
	inFile.close();
	outFile.close();
	return 0;
}
