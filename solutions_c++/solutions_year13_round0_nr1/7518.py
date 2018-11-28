
 
// code jam problem #1 
//Problem #1 Tic-Tac-Toe-Tomek
// code by: mo3dmo
// written on April 12, 2013.

//Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The board starts empty, except that a single 'T' symbol may appear in one of the 16 squares. There are two players: X and O. They take turns to make moves, with X starting. In each move a player puts her symbol in one of the empty squares. Player X's symbol is 'X', and player O's symbol is 'O'.

// After a player's move, if there is a row, column or a diagonal containing 4 of that player's symbols, or containing 3 of her symbols and the 'T' symbol, she wins and the game ends. Otherwise the game continues with the other player's move. If all of the fields are filled with symbols and nobody won, the game ends in a draw. See the sample input for examples of various winning positions.

// Given an 4 x 4 board description containing 'X', 'O', 'T' and '.' characters (where '.' represents an empty square), describing the current state of a game, determine the status of the Tic-Tac-Toe-Tomek game going on. The statuses to choose from are:

// #    "X won" (the game is over, and X won)
// #    "O won" (the game is over, and O won)
// #    "Draw" (the game is over, and it ended in a draw)
// #    "Game has not completed" (the game is not over yet)

// Input

// The first line of the input gives the number of test cases, T. T test cases follow. Each test case consists of 4 lines with 4 characters each, with each character being 'X', 'O', '.' or 'T' (quotes for clarity only). Each test case is followed by an empty line.
// Output

// For each test case, output one line containing "Case #x: y", where x is the case number (starting from 1) and y is one of the statuses given above. Make sure to get the statuses exactly right. When you run your code on the sample input, it should create the sample output exactly, including the "Case #1: ", the capital letter "O" rather than the number "0", and so on.
// Limits

// The game board provided will represent a valid state that was reached through play of the game Tic-Tac-Toe-Tomek as described above.
// Small dataset

//1 ? T ? 10.
// Large dataset

// 1 ? T ? 1000. 

// /* run this program using the console pauser or add your own getch, system("pause") or input loop */




// code plan:
//1.0 define board structure:

// 2.0 open input and output files and read number of test caes.
// 3.0 Read input put board into a 4x4 matix.
// 4.0 sub to check to see if X or O win. (print results immidte to global file marker.
	   // 4.1 check each row.
	   // 4.2 check each column.
	   // 4.3 check digonals.
// 5.0 Print result fuction.


// Start of code:
	
	
// Includes:
#include <iostream>
#include <fstream>
#include <iostream>
#include <string>
#include <cstdlib>

int	verbose = 1; // verbose is global verable that tells all fuctions to print debug and other data.
//1.0 make board structure:


using namespace std;

// define end states
enum end_state  {
 	 O_won = 0, // (the game is over, and X won)
     X_won = 1, // (the game is over, and O won)
     Draw = 2,   // (the game is over, and it ended in a draw)
     Not_done = 3,  // "Game has not completed" (the game is not over yet)
 }; 
 struct board {
    char square [4][4]; // set to 9 so we can used 1 to 8 in checker board.
};

// 3.0 Read input put board into a 4x4 matix.
board read_board(std::ifstream& inf, int N, int M) { 

	board my_board;
	    if (verbose==2) { cout << "starting new board" << endl << endl;
	    }
		for (int iii = 0; iii < N  ; iii++ ) {
			for (int jjj = 0; jjj < M ; jjj++ ) { 
				inf >> my_board.square[iii][jjj]; 
			    if (verbose==2) { cout << "location: " << iii << " " << jjj << " is:" << my_board.square[iii][jjj] << endl; }; 	
			};
		};


return my_board;
}

	
	// 4.0 sub to check to see if X or O win. (print results immidte to global file marker.
	// note code error: right now N and M must be equal.
end_state check_board(board my_board, int N, int M ) {
       // test results flag setup: We set all flags true then set false when find case prove that are set wrong.
	   int found_blank_square = 0;
	   int row_all_x = 1;
	   int row_all_o = 1;
	   int column_all_x = 1;
	   int column_all_o = 1;
	   int dignal_left_all_x = 1; 
	   int dignal_left_all_o = 1; 
	   int dignal_right_all_x = 1;
	   int dignal_right_all_o = 1;
	   	for (int iii = 0; iii < N  ; iii++ ) {
			row_all_x = 1;
			row_all_o = 1;
			column_all_x = 1;
			column_all_o = 1; 
			if (verbose==3) { 
				cout << endl << "next row all values are reset" << endl;
				cout << "i x   o   B" << endl;   
			    cout << iii << " " << " " << row_all_x << column_all_x << dignal_right_all_x << dignal_left_all_x;
				cout <<        " "               << row_all_o << column_all_o << dignal_right_all_o << dignal_left_all_o;  
			    cout << " " << found_blank_square << endl << endl;
				};
			
			for (int jjj = 0; jjj < M ; jjj++ ) { 
				// if (my_board.square[iii][jjj]) =='T') {  } do nothing if its a T or any other character.
			// 4.1 check each row.
				if (my_board.square[iii][jjj] =='O') { row_all_x = 0; };
				if (my_board.square[iii][jjj] =='X') { row_all_o = 0;  };
				if (my_board.square[iii][jjj] =='.') { found_blank_square = 1; row_all_x = 0; row_all_o = 0; };
			// 4.2 check each column.
				if (my_board.square[jjj][iii] =='O') { column_all_x = 0; };
				if (my_board.square[jjj][iii] =='X') { column_all_o = 0;  };
				if (my_board.square[jjj][iii] =='.') { found_blank_square = 1; column_all_x = 0; column_all_o = 0; };
			
				if (verbose==3) { 
				cout << "i j x   o   B" << endl;   
			    cout << iii << " " << jjj << " " << row_all_x << column_all_x << dignal_right_all_x << dignal_left_all_x;
				cout <<        " "               << row_all_o << column_all_o << dignal_right_all_o << dignal_left_all_o;  
			    cout << " " << found_blank_square << endl;
				}; 
		   };
		   // return results of any of row_all or column_all verables are still set.
			if (row_all_x) { return X_won; };
			if (row_all_o) { return O_won; };
			if (column_all_x) { return X_won; };
			if (column_all_o) { return O_won; };
			// 4.3 check digonals. 
			if (my_board.square[iii][iii] =='O') { dignal_left_all_x = 0; };
			if (my_board.square[iii][iii] =='X') { dignal_left_all_o = 0;  };
			if (my_board.square[iii][iii] =='.') { found_blank_square = 1; dignal_left_all_x = 0; dignal_left_all_o = 0; };
			
			// note: the -1 added because M is total number of squares but indexs go from 0 to M-1.
			if (my_board.square[iii][M-iii-1] =='O') { dignal_right_all_x = 0; };
			if (my_board.square[iii][M-iii-1] =='X') { dignal_right_all_o = 0;  };
			if (my_board.square[iii][M-iii-1] =='.') { found_blank_square = 1; dignal_right_all_x = 0; dignal_right_all_o = 0; };
			
			
		
		
			}
			// return results for digonals:
			if (dignal_right_all_x) { return X_won ;};
			if (dignal_right_all_o) { return O_won ;};
			if (dignal_left_all_x) { return X_won ;};
			if (dignal_left_all_o) { return O_won ;};
			// if no winner decide if not done or a draw:
			if (found_blank_square) { return Not_done ;}
			else {return Draw;};
		}

//O_won = 0, // (the game is over, and X won)
//     X_won = 1, // (the game is over, and O won)
//     Draw = 2,   // (the game is over, and it ended in a draw)
//     Not_done

    // 5.0 Print result fuction.
void print_result(std::ofstream& outf, end_state state, int case_number) {
	if (state==O_won) { outf << "Case #" << case_number << ": O won" << endl;
			if (verbose) { cout << "Case #" << case_number << ": O won" << endl; }; 
	};
	
	if (state==X_won) { outf << "Case #" << case_number << ": X won" << endl; 
			if (verbose)  { cout << "Case #" << case_number << ": X won" << endl; }; 
	}; 
	
	if (state==Draw)  { outf << "Case #" << case_number << ": Draw" << endl; 
			if (verbose)  { cout << "Case #" << case_number << ": Draw" << endl; }; 
	}; 
	
	if (state==Not_done) { outf << "Case #" << case_number << ": Game has not completed" << endl; 
			if (verbose)     { cout << "Case #" << case_number << ": Game has not completed" << endl; }; 
	};  

}

int main() {

    using namespace std;
 
 
 // 2.0 open input and output files and read number of test caes.
    // ifstream is used for reading files
    // We'll read from a file called Sample.dat
    ifstream inf("in.dat");
 
    // If we couldn't open the output file stream for reading
    if (!inf)
    {
        // Print an error and exit
        cerr << "Uh oh, in.dat could not be opened for reading!" << endl;
        exit(1);
    }
 	// 2.1 read number of test cases and print result.
	int T; // number of test cases.int T
	inf >> T;
    if (verbose) { cout << "number of test cases T:" << T << endl; }
   
   	// 2.2 open output file:
    ofstream outf("out.txt");
    // If we couldn't open the output file stream for reading
    if (!outf)
    {
        // Print an error and exit
        cerr << "Uh oh, out.txt could not be opened for reading!" << endl;
        exit(1);
	}	 
// 3.0 Loop Read input put board into a 4x4 matix and look for winners.
// old: test code: 	board my_board = read_board(inf,4,4);
// old: test code:	my_board = read_board(inf,4,4);


for (int iii = 1; iii <= T  ; iii++ ) { 
	board my_board = read_board(inf,4,4);
	print_result(outf, check_board(my_board,4,4), iii);
	}

// 4.0 sub to check to see if X or O win. (print results immidte to global file marker.
	   // 4.1 check each row.
	   // 4.2 check each column.
	   // 4.3 check digonals.
// 5.0 Print result fuction.

return 0;
}
	
	
	
