#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int time;
	fin >> time;
	for(int c=1; c<=time; c++){
		int row1;
		fin >> row1;
		vector<int > r1;
		for(int i=0; i<row1-1; i++){
			for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
			}
		}
		for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
				r1.push_back(waste);
		}
		for(int i=0; i<4-row1; i++){
			for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
			}
		}
		
		int row2;
		fin >> row2;
		vector<int > r2;
		for(int i=0; i<row2-1; i++){
			for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
			}
		}
		for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
				for(int i=0; i<r1.size(); i++){
					if(r1[i]==waste){
						r2.push_back(waste);
						break;
					}	
				}
		}
		for(int i=0; i<4-row2; i++){
			for(int j=0;j<4; j++){
				int waste;
				fin>> waste;
			}
		}
		if(r2.size() ==1){
			fout << "Case #" << c << ": "<< r2[0] << endl;
		}
		else if(r2.size()>1){
			
			fout << "Case #" << c << ": Bad magician!"<< endl;
		}
		else{
			fout << "Case #" << c << ": Volunteer cheated!"<< endl;
		}
	}
	
}
