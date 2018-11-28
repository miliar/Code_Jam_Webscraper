#include <iostream>
#include <fstream>
#include <string>

using namespace std;

static unsigned short patt[10] = {4369, 61440, 3840, 240, 15, 34952, 17476, 8738, 33825, 4680};

int main(){
	fstream file;
	file.open("./A-large.in", fstream::in);
	if(!file){
		cout << "Error opening file\n";
		return 1;
	}
	int T, caseNo = 0;
	string line;
	file >> T;
	getline(file, line); // Read the extra blank line...
	while(T--){
		unsigned short O = 0, X = 0;
		bool hasDot = false;
		++caseNo;
		for(int i=0; i<4; ++i){
			getline(file, line);
			for(int j=0; j<4; ++j){
				if(line[j] == '.')
					hasDot = true;
				if(line[j] == 'T' || line[j] == 'O')
					O |= 1;
				if(line[j] == 'T' || line[j] == 'X')
					X |= 1;
				if(i == 3 && j == 3)
					break;
				O <<= 1;
				X <<= 1;
			}
		}
		getline(file, line); // Read the next blank line...
		
		
		bool Owon, Xwon, draw, incomplete;
		Owon = Xwon = draw = incomplete = false;
		for(int i=0; i<10; ++i){
			if((O & patt[i]) == patt[i]){
				Owon = true;
				break;
			}
			if((X & patt[i]) == patt[i]){
				Xwon = true;
				break;
			}
		}
		///////////////////////////////
		if(Owon)
			cout << "Case #" << caseNo << ": " << "O won\n";
		else if(Xwon)
			cout << "Case #" << caseNo << ": " << "X won\n";
		else{
			if(hasDot)
				cout << "Case #" << caseNo << ": Game has not completed\n";
			else
				cout << "Case #" << caseNo << ": Draw\n";
		}
	}//end while(T--)
	file.close();
	return 0;
}//end main

