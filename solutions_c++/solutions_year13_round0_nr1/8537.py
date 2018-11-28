#include <iostream>
#include <fstream>
#include <stack>
#include <string>
#include <cstring>
#include <cstdlib>
using namespace std;

const int BOARD_SIZE = 4;

 bool gameComplete(string board);
 string findLeftDiagonalWinner(string board);
 string findRightDiagonalWinner(string board);
 string findHorizontalWinner(string board);
 string findVerticalWinner(string board);

int main() {

//"XOXTXXOOOXOXXXOO"

    ifstream in;
    ofstream out;
    in.open("A-small-attempt0.in");
    out.open("output.txt");

    int numberOfTests;
    string a;
    getline(in, a);

    numberOfTests = atoi(a.c_str());
    int c=0;

    while( c < numberOfTests ){
	    string board, tmp;
	    for(int i = 0; i < BOARD_SIZE; i++){
	    	getline(in, tmp);
	    	board += tmp;
	    }

	    //REMOVE WHITESPACE
        cout << board << endl;
	    bool complete = gameComplete(board);

	    string win[] = {
	    	findLeftDiagonalWinner(board),
	    	findRightDiagonalWinner(board),
	    	findVerticalWinner(board),
	    	findHorizontalWinner(board),
	    };
        string result;
	    bool hasWinner = false;
	    for(int o=0;o<4;o++){
	    	if(win[o] == "X"){
	    		result = "X won";
	    		cout  << "X WON THE GAME"<< endl << endl;
	    		hasWinner = true;
	    	}else if(win[o] == "O"){
	    		result = "O won";
    			cout << "O WON THE GAME"<< endl<< endl;
	    		hasWinner = true;
	    	}
	    }


	    if(hasWinner == false){
	    	if(complete){
	    		result = "Draw";
	    		cout  << "DRAW"<< endl<< endl;
	    	}else{
	    		result = "Game has not completed";
	    		cout << "Game has not completed" << endl<< endl;
	    	}
	    }

        out << "Case #" << c+1 <<": " << result <<endl;

	    string toss;
	    getline(in, toss);
	    c++;
	}


}

 bool gameComplete(string board){
    char dot = '.';
	for(int i=0; i < sizeof(board); i++){
		if(dot == board.at(i)){
			return false;
		}
	}

	return true;
}

 string findLeftDiagonalWinner(string board){
	stack<char> win;

	for(int i=0;i<BOARD_SIZE;i++){
		win.push(board.at((4*i)+i));
	}

    string a;
	for(int j=0;j<BOARD_SIZE;j++){
        a += win.top();
        win.pop();
    }

    if(a == "OOOO" || a == "TOOO" || a == "OTOO" || a == "OOTO" || a == "OOOT" ){
        return "O";
    }else if(a == "XXXX" || a == "TXXX" || a == "XTXX" || a == "XXTX" || a == "XXXT"){
        return "X";
    }


	return "none";
}

 string findRightDiagonalWinner(string board){
	stack<char> win;

	for(int i=12; i >= 3; (i -= 3) ){
		win.push(board.at(i));
	}

    string a;
	for(int j=0;j<BOARD_SIZE;j++){
        a += win.top();
        win.pop();
    }

    if(a == "OOOO" || a == "TOOO" || a == "OTOO" || a == "OOTO" || a == "OOOT" ){
        return "O";
    }else if(a == "XXXX" || a == "TXXX" || a == "XTXX" || a == "XXTX" || a == "XXXT"){
        return "X";
    }


	return "none";
}

 string findHorizontalWinner(string board){
	stack<char> win;


	for(int i=0;i<BOARD_SIZE;i++){
		for(int j=0;j<BOARD_SIZE;j++){
			win.push(board.at((4*i)+j));
		}
	}

	for(int j=0;j<BOARD_SIZE;j++){
		string a;
		for(int i=0;i<BOARD_SIZE;i++){
			a += win.top();
			win.pop();
		}

		if(a == "OOOO" || a == "TOOO" || a == "OTOO" || a == "OOTO" || a == "OOOT" ){
			return "O";
		}else if(a == "XXXX" || a == "TXXX" || a == "XTXX" || a == "XXTX" || a == "XXXT"){
			return "X";
		}
	}

	return "none";

}

 string findVerticalWinner(string board){
	stack<char> win;

	for(int i=0;i<BOARD_SIZE;i++){
		for(int j=0;j<BOARD_SIZE;j++){
			win.push(board.at(i+(4*j)));
		}
	}

	for(int j=0;j<BOARD_SIZE;j++){
		string a;
		for(int i=0;i<BOARD_SIZE;i++){
			a += win.top();
			win.pop();
		}

		if(a == "OOOO" || a == "TOOO" || a == "OTOO" || a == "OOTO" || a == "OOOT" ){
			return "O";
		}else if(a == "XXXX" || a == "TXXX" || a == "XTXX" || a == "XXTX" || a == "XXXT"){
			return "X";
		}
	}

	return "none";
}
