#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;



int main(int argc, char*argv[]){

	fstream fcin(argv[1], fstream::in);
	fstream fcout(argv[2], fstream::out);


	int totalCase;
	fcin >> totalCase;
	
	for(int caseIdx=1; caseIdx <= totalCase; caseIdx++){
		int X,R,C;
		fcin >> X >> R >> C;

		if(X == 1){
			fcout << "Case #" << caseIdx << ": GABRIEL" << endl;
		}
		else if(X == 2){
			if(((R*C)%2) == 0){
				fcout << "Case #" << caseIdx << ": GABRIEL" << endl;
			}
			else{
				fcout << "Case #" << caseIdx << ": RICHARD" << endl;
			}
		}	
		else if(X == 3){
			if( ((R*C)%3) == 0 ){
				if( (R==1) || (C == 1)){
					fcout << "Case #" << caseIdx << ": RICHARD" << endl;
				}
				else{
					fcout << "Case #" << caseIdx << ": GABRIEL" << endl;
				}
			}
			else{
				fcout << "Case #" << caseIdx << ": RICHARD" << endl;
			}
		}
		else if (X == 4){
			if( ((R==3)&&(C==4)) ||  ((R==4)&&(C==3)) || ((R==4)&&(C==4)) ){
				fcout << "Case #" << caseIdx << ": GABRIEL" << endl;
			}
			else{
				fcout << "Case #" << caseIdx << ": RICHARD" << endl;
			}
		}
		else{
			fcout << "Case #" << caseIdx << ": RICHARD" << endl;
		}
	}


	return 0;
}


