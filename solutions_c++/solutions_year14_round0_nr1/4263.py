#include<iostream>
#include<fstream>
using namespace std;

int main(){
	int T, row1, row2;
	int ary1[4][4] = {0};
	int ary2[4][4] = {0};

	ifstream inFile;
	inFile.open("data.txt");
	ofstream outFile("out.txt");

	inFile>>T;
	for(int i = 1; i<=T; i++)
	{
		inFile>>row1;
		for(int x = 0; x<4; x++)
			for(int y = 0; y<4; y++)
				inFile>>ary1[x][y];
		
		inFile>>row2;
		for(int x = 0; x<4; x++)
			for(int y = 0; y<4; y++)
				inFile>>ary2[x][y];
		
		int counter = 0;
		int number = 0;
		for(int r1 = 0; r1<4; r1++)
			for(int r2 = 0; r2<4; r2++){
				if(ary1[row1-1][r1] == ary2[row2-1][r2]){
					counter++;
					number = ary1[row1-1][r1];
				}
			}

		if(counter<1)
			outFile<<"Case #" << i <<": Volunteer cheated!"<<endl;
		else{
			if(counter>1)
				outFile<<"Case #"<< i <<": Bad magician!"<<endl;
			else{
				if(counter == 1)
					outFile<<"Case #"<< i <<": " << number<<endl;
			}
		}

	} 
	inFile.close();
	outFile.close();
	return 0;
}