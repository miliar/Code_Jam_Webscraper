#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

int main(int argc, char *argv[]){
	int T;
	
	ifstream inputfile(argv[1]);
	ofstream outputfile("output.txt");

	inputfile >> T;
	
	for(int i=0; i<T; i++){
		int ans1, ans2;
		int ret=0;
		int count=0;
		
		int cards1[4][4];
		int cards2[4][4];
		
		inputfile >> ans1;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				inputfile >> cards1[j][k];
			}
		}
		inputfile >> ans2;
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				inputfile >> cards2[j][k];
			}
		}
		
		
		for(int j=0; j<4; j++){
			for(int k=0; k<4; k++){
				if(cards1[ans1-1][j] == cards2[ans2-1][k]){
					ret = cards1[ans1-1][j];
					count++;
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": ";
		outputfile << "Case #" << i+1 << ": ";
		if(count==0){
			cout << "Volunteer cheated!" << endl;
			outputfile << "Volunteer cheated!" << endl;
		}else if(count==1){
			cout << ret << endl;
			outputfile << ret << endl;
		}else if(count>1){
			cout << "Bad magician!" << endl;
			outputfile << "Bad magician!" << endl;
		}
	}
	return 0;
}