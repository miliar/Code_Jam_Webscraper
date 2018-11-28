#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main(){
	ifstream in("A-small-attempt1.in");
	ofstream out("A-small-attempt1.out");
	string board[4];
	int n;
	in>>n;
	string letters = "XO";
	char winLetter=' ';
	int answers[n];
	for(int i=0; i<n; i++){
		for(int j=0; j<4; j++)
				in>>board[j];
		
		for(int k = 0; k<2; k++){
			for(int m=0; m<4; m++){
				if((letters.at(k)==board[m].at(0) && letters.at(k)==board[m].at(1)) && (letters.at(k)==board[m].at(2) && letters.at(k)==board[m].at(3))) winLetter = letters.at(k);
				else if((letters.at(k)==board[m].at(0) && letters.at(k)==board[m].at(1)) && (letters.at(k)==board[m].at(2) && board[m].at(3)=='T')) winLetter = letters.at(k);
				else if((letters.at(k)==board[m].at(1) && letters.at(k)==board[m].at(2)) && (letters.at(k)==board[m].at(3) && board[m].at(0)=='T')) winLetter = letters.at(k);
				else if((letters.at(k)==board[0].at(m) && letters.at(k)==board[1].at(m)) && (letters.at(k)==board[2].at(m) && board[3].at(m)==letters.at(k))) winLetter = letters.at(k);
				else if((letters.at(k)==board[0].at(m) && letters.at(k)==board[1].at(m)) && (letters.at(k)==board[2].at(m) && board[3].at(m)=='T')) winLetter = letters.at(k);
				else if((letters.at(k)==board[3].at(m) && letters.at(k)==board[1].at(m)) && (letters.at(k)==board[2].at(m) && board[0].at(m)=='T')) winLetter = letters.at(k);
			}
			if((letters.at(k)==board[0].at(0) && letters.at(k)==board[1].at(1)) && (letters.at(k)==board[2].at(2) && board[3].at(3)=='T')) winLetter = letters.at(k);
			else if((letters.at(k)==board[0].at(0) && letters.at(k)==board[1].at(1)) && (letters.at(k)==board[2].at(2) && board[3].at(3)==letters.at(k))) winLetter = letters.at(k);
			else if((letters.at(k)==board[0].at(3) && letters.at(k)==board[1].at(2)) && (letters.at(k)==board[2].at(1) && board[3].at(0)=='T')) winLetter = letters.at(k);
			else if((letters.at(k)==board[0].at(3) && letters.at(k)==board[1].at(2)) && (letters.at(k)==board[2].at(1) && board[3].at(0)==letters.at(k))) winLetter = letters.at(k);
			else if((letters.at(k)==board[3].at(3) && letters.at(k)==board[1].at(1)) && (letters.at(k)==board[2].at(2) && board[0].at(0)=='T')) winLetter = letters.at(k);
			else if((letters.at(k)==board[3].at(0) && letters.at(k)==board[1].at(2)) && (letters.at(k)==board[2].at(1) && board[0].at(3)=='T')) winLetter = letters.at(k);
			
		}
		if(winLetter!=' '){
							if(winLetter=='X')answers[i]=0;
							if(winLetter=='O') answers[i]=1;
		 } 
		else{
			bool filled = true;
			for(int q = 0; q<4; q++)
				for(int r = 0; r<4;r++)
					if(board[q].at(r)=='.') filled=false;
			if(filled)answers[i]=2;
			 
			else answers[i]=3; 
		}
		winLetter=' ';
	}
	
	for(int i=0; i<n; i++){
		if(answers[i]==0) out<<"Case #"<<i+1<<": X won"<<endl;
		if(answers[i]==1) out<<"Case #"<<i+1<<": O won"<<endl;
		if(answers[i]==2) out<<"Case #"<<i+1<<": Draw"<<endl;
		if(answers[i]==3) out<<"Case #"<<i+1<<": Game has not completed"<<endl;
	}
}
