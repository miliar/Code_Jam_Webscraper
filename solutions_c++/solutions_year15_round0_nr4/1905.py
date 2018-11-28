#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;
/*
int main(int argc, char *argv[]) {
	for(int R = 1; R <= 4; R++){
		for(int C = 1; C <=4; C++){
			cout<<"-------------------------"<<endl;
			// muestra la matriz
			for (int i = 0; i<R; i++){
				for(int j=0; j<C; j++){
					cout<<"[ ] ";
				}
				cout<<endl;
			}
			cout<<endl;
			
			for (int X = 1; X <= 4; X++){
				int nCells = R * C;
				bool richardWins = false;
				
				if(
					(X >= 7) ||				/// RICHARD can choose X-ominoe with holes, this makes imposible for GABRIEL to win
					nCells % X != 0 ||		/// GABRIEL cant fill the whole grid without overlaps or spills
					X > min(R, C)*2 ||		/// RICHARD can choose a X-ominoe that wont fit event if it is rotated
					X > max(R, C)			/// RICHARD can choose the longest X-ominoe, it wont fit event if it is rotated
					){
						richardWins = true;
					}
				
				cout<<X<<": "<<(richardWins?"RICHARD":"GABRIEL")<<endl;
			}
		}
	}
	
	
}*/

int main(int argc, char *argv[]) {
	int nTestCases;
	//auto &input = cin;
	ifstream input("D-small-attempt1.in");
	
	input>>nTestCases;
	
	for(int i = 0; i < nTestCases; i++){
		int X, R, C;
		input>>X>>R>>C;
		//X = 1 + rand() %4;
		//R = 1 + rand() %4;
		//C = 1 + rand() %4;
		
		
		int nCells = R * C;
		bool richardWins = false;
		
		if(
		(X >= 7) ||				/// RICHARD can choose X-ominoe with holes, this makes imposible for GABRIEL to win
		nCells % X != 0 ||		/// GABRIEL cant fill the whole grid without overlaps or spills
		X > min(R, C)*2 ||		/// RICHARD can choose a X-ominoe that wont fit event if it is rotated
		X > max(R, C) ||		/// RICHARD can choose the longest X-ominoe, it wont fit event if it is rotated
		(((R==4 && C==2) || (R==2 && C==4)) && X == 4)						/// Special case
		){
			richardWins = true;
		}
		
		cout<<"Case #"<<i+1<<": "<<(richardWins?"RICHARD":"GABRIEL")<<endl;
		//cout<<X<<" "<<R<<" "<<C<<endl<<endl;

	}
	return 0;
}

