#include <iostream>
using namespace std;
#include <string>
#include <fstream>
#include <cmath>


char parseBoard(string board[4]);
char findWinner(char check0, char check1, char check2, char check3);

int main()
{
	string charRead,lineRead,board[4], result;
	int numCases=0;
	

	ifstream inputFile;
	ofstream outFile;

	outFile.open("A-small-result2.in",ofstream::out);
	inputFile.open("A-small-attempt2.in", ifstream::in);
	//outFile<<"Is this working "<<endl;

	if(inputFile.good()){
		getline(inputFile,lineRead);

		numCases= atoi(lineRead.c_str());
		//cout<<"Number of Cases = "<<numCases<<endl;

		for(int x=0; x<numCases; x++){
			for(int column=0; column<4;column++){
				inputFile>>charRead;
				if(!charRead.compare("\n")){
					column--;
				}
				else board[column]=charRead;
				//cout<<"Board["<<column<<"]= "<<board[column]<<endl;

				//cout<<"First Letter of Board["<<column<<"] ="<<board[column].c_str()[0] <<endl;
			}
			char winner = parseBoard(board);

			switch(winner){
			case ('X'):
				outFile<<"Case #"<<x+1<<": X won\n";
				break;
			case ('O'):
				outFile<<"Case #"<<x+1<<": O won\n";
				break;
			case ('.'):
				outFile<<"Case #"<<x+1<<": Game has not completed\n";
				break;
			case ('D'):
				outFile<<"Case #"<<x+1<<": Draw\n";
				break;
			}
		}
	}
	//else cout<<"ERROR Opening the File"<<endl;
	//getchar();
}

char parseBoard(string board[]){

	char check0_col, check1_col, check2_col, check3_col, winner[4]={NULL};
	char answer;

	for(int column=0;column<4;column++){
		check0_col = board[0].c_str()[column];
		check1_col = board[1].c_str()[column];
		check2_col = board[2].c_str()[column];
		check3_col = board[3].c_str()[column];
		winner[column] = findWinner(check0_col, check1_col, check2_col, check3_col);
	}
	if(winner[0] =='X' || winner[1] =='X' || winner[2] =='X' || winner[3] =='X' )
		answer='X';
	else if(winner[0] =='O' || winner[1] =='O' || winner[2] =='O' || winner[3] =='O' )
		answer= 'O';
	else if(winner[0] =='.' || winner[1] =='.' || winner[2] =='.' || winner[3] =='.' )
		answer= '.';

	if(answer=='X' || answer=='O'){
		return answer;
	}

	for(int column=0;column<4;column++){
		check0_col = board[column].c_str()[0];
		check1_col = board[column].c_str()[1];
		check2_col = board[column].c_str()[2];
		check3_col = board[column].c_str()[3];
		winner[column] = findWinner(check0_col, check1_col, check2_col, check3_col);
	}
	if(winner[0] =='X' || winner[1] =='X' || winner[2] =='X' || winner[3] =='X' )
		answer= 'X';
	else if(winner[0] =='O' || winner[1] =='O' || winner[2] =='O' || winner[3] =='O' )
		answer= 'O';
	else if(winner[0] =='.' || winner[1] =='.' || winner[2] =='.' || winner[3] =='.' )
		answer= '.';

	if(answer=='X' || answer=='O'){
		return answer;
	}

	check0_col= board[0].c_str()[0];
	check1_col= board[1].c_str()[1];
	check2_col= board[2].c_str()[2];
	check3_col= board[3].c_str()[3];
	winner[0] = findWinner(check0_col, check1_col, check2_col, check3_col);

	check0_col= board[0].c_str()[3];
	check1_col= board[1].c_str()[2];
	check2_col= board[2].c_str()[1];
	check3_col= board[3].c_str()[0];
	winner[1] = findWinner(check0_col, check1_col, check2_col, check3_col);

	if(winner[0] =='X' || winner[1] =='X' )
		return 'X';
	else if(winner[0] =='O' || winner[1] =='O' )
		return 'O';
	else if(winner[0] =='.' || winner[1] =='.' )
		return '.';
	else
		return 'D';
		
}

char findWinner(char check0, char check1, char check2, char check3)
{
	int first = abs(check0-check1);
	int second = abs(check2-check3);
	int third = abs(check1-check2);
	//X = 4, O = 5
	int total = first + second + third;
	if( total==0){
		return check0;
	}
	else if(total==4){
		return 'X';
	}
	else if(total==5){
		return 'O';
	}
	else if( (check0=='.') || (check1=='.') || (check2=='.') || (check3=='.')){
		return '.';
	}
	else return 'D';

	/*if( (first ==0 ) || (first==4) ){
			if( (check2 == check3) || ('T' == check2) || ('T' == check3) ){
				if( (check1 == check2) || ('T' == check1) || ('T' == check2) ){
					if( (check1 == 'X') || (check2=='X')){
						return 'X';
					}
					else if( (check1 == 'O') || (check2=='O')){
						return 'O';
					}
					else if( (check1 == '.') || (check2=='.')){
						return 'I';
					}
				}
				else return NULL;
			}
			else return NULL;
	}
	else return NULL;
	*/
}