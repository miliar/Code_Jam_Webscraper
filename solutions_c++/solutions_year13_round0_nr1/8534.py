/* https://code.google.com/codejam/contest/2270488/dashboard#s=p0 */

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>

#define DEFAULT_CHAR	' '		// dummy char which would be replaced by the winner in diagonal(if applicable)
#define HELPER_CHAR		'T'		// can help both opponents whoever is in Majority
#define EMPTY_CHAR		'.'		// means it was not accessed by any opponent throughout the play
#define NO_MORE_CHECK	'~'		// NO WINNER
#define PLAYER_X		'X'
#define PLAYER_O		'O'

using namespace std;

int main() {
	int T, found;
	map <char, int> horizontal_turn_count;
	map <char, int> vertical_turn_count;
	map <char, int> left_diag_turn_count;
	map <char, int> right_diag_turn_count;
	string turns[4], blank;
	char last_horizontal_turn, last_vertical_turn, last_left_diag_turn, last_right_diag_turn, winner;
	
	cin>>T;
	
	for(int i = 0; i < T; i++) {
		// Phase 1: Initialization for each test case
		getline(cin, blank); // dummy extract from stream. Its of no use but mandatory
		found = -1;
		
		//Setting left diagonal and right diagonal turn as default
		last_left_diag_turn = last_right_diag_turn = DEFAULT_CHAR; 
		
		//Setting left diagonal and right diagonal turn count for each player as 0
		left_diag_turn_count[PLAYER_X] = left_diag_turn_count[PLAYER_O] = left_diag_turn_count[HELPER_CHAR] = left_diag_turn_count[EMPTY_CHAR] = 0;
		right_diag_turn_count[PLAYER_X] = right_diag_turn_count[PLAYER_O] = right_diag_turn_count[HELPER_CHAR] = right_diag_turn_count[EMPTY_CHAR] = 0;
		
		getline(cin, turns[0]);
		getline(cin, turns[1]);
		getline(cin, turns[2]);
		getline(cin, turns[3]);
		
		// Phase 2: Accepting the inputs and processing
		for(int row = 0; (row < 4) && (found == -1); row++) {
		
			//Setting last horizontal and vertical turn as default
			last_horizontal_turn = last_vertical_turn = DEFAULT_CHAR;
			
			//Setting horizontal and vertical turn count for each player as 0
			horizontal_turn_count[PLAYER_X] = horizontal_turn_count[PLAYER_O] = horizontal_turn_count[HELPER_CHAR] = horizontal_turn_count[EMPTY_CHAR] = 0;	
			vertical_turn_count[PLAYER_X] = vertical_turn_count[PLAYER_O] = vertical_turn_count[HELPER_CHAR] = vertical_turn_count[EMPTY_CHAR] = 0;	
			
			for(int col = 0; (col < 4) && (found == -1); col++) {			
				//Step 1: Horizontal check (Sequence of if...else if... which are nested matters!)
				if(NO_MORE_CHECK != last_horizontal_turn) {
					horizontal_turn_count[turns[row][col]] += 1;
					
					if(EMPTY_CHAR == turns[row][col]) { // We now cant find any winner horizontally
						last_horizontal_turn = NO_MORE_CHECK; // Henceforth do not check any winner vertically in this row
					} else if(DEFAULT_CHAR == last_horizontal_turn) { // if its the first time horizontal elem access
						last_horizontal_turn = turns[row][col];					
					} else if(HELPER_CHAR == turns[row][col]) {
						last_horizontal_turn = turns[row][col];
					} else if(last_horizontal_turn == turns[row][col]) {
						;
					} else { // 
						;
					}
				} // end of Step 1
				
				//Step 2: Vertical check
				if(NO_MORE_CHECK != last_vertical_turn) {
					vertical_turn_count[turns[col][row]] += 1;	

					if(EMPTY_CHAR == turns[col][row]) { // We now cant find any winner vertically
						last_vertical_turn = NO_MORE_CHECK; // Henceforth do not check any winner vertically in this col
					} else if(DEFAULT_CHAR == last_vertical_turn) { // if its the first time vertical elem access
						last_vertical_turn = turns[col][row];					
					} else if(HELPER_CHAR == turns[col][row]) {
						last_vertical_turn = turns[col][row];
					} else if(last_vertical_turn == turns[col][row]) {
						;
					} else {
						;
					}
				} // end of Step 2
				
				//Step 3: Left diagonal check
				if(row == col) {
					if(NO_MORE_CHECK != last_left_diag_turn) {
						left_diag_turn_count[turns[row][col]] += 1;						

						if(EMPTY_CHAR == turns[row][col]) { // We now cant find any winner diagonally (left)
							last_left_diag_turn = NO_MORE_CHECK; //Henceforth do not check any winner diagonally (left) in this row
						} else if(DEFAULT_CHAR == last_left_diag_turn) { // if its the first time diagonal (left) elem access
							last_left_diag_turn = turns[row][col];					
						} else if(HELPER_CHAR == turns[row][col]) {
							last_left_diag_turn = turns[row][col];
						} else if(last_left_diag_turn == turns[row][col]) {
							;
						} else {
							;
						}						
					}
				} // end of Step 3
				
				//Step 4: Right diagonal check
				else if(3 == (row + col)) {
					if(NO_MORE_CHECK != last_right_diag_turn) {				
						right_diag_turn_count[turns[row][col]] += 1;
						
						if(EMPTY_CHAR == turns[row][col]) { // We now cant find any winner diagonally (left)
							last_right_diag_turn = NO_MORE_CHECK; //Henceforth dont check any winner diagonally (right) in this col
						} else if(DEFAULT_CHAR == last_right_diag_turn) { // if its the first time diagonal (left) elem access
							last_right_diag_turn = turns[row][col];					
						} else if(HELPER_CHAR == turns[row][col]) {
							last_right_diag_turn = turns[row][col];
						} else if(last_right_diag_turn == turns[row][col]) {
							;
						} else {
							;
						}						
					}
				} // end of Step 4
				/*cout<<"#PLAYER_X in ("<<row<<","<<col<<")--> "<<horizontal_turn_count[PLAYER_X]<<" "<<vertical_turn_count[PLAYER_X]<<" "<<left_diag_turn_count[PLAYER_X]<<" "<<right_diag_turn_count[PLAYER_X];
				cout<<"\t#PLAYER_O in ("<<row<<","<<col<<")--> "<<horizontal_turn_count[PLAYER_O]<<" "<<vertical_turn_count[PLAYER_O]<<" "<<left_diag_turn_count[PLAYER_O]<<" "<<right_diag_turn_count[PLAYER_O];		
				cout<<"\t#HELPER_CHAR in ("<<row<<","<<col<<")--> "<<horizontal_turn_count[HELPER_CHAR]<<" "<<vertical_turn_count[HELPER_CHAR]<<" "<<left_diag_turn_count[HELPER_CHAR]<<" "<<right_diag_turn_count[HELPER_CHAR];				
				cout<<"\t#EMPTY_CHAR in ("<<row<<","<<col<<")--> "<<horizontal_turn_count[EMPTY_CHAR]<<" "<<vertical_turn_count[EMPTY_CHAR]<<" "<<left_diag_turn_count[EMPTY_CHAR]<<" "<<right_diag_turn_count[EMPTY_CHAR]<<endl;*/
			} // end of 'col' loop

			
			// Deciding the winner (if there is one)
			if((4==horizontal_turn_count[PLAYER_X]) || ((3==horizontal_turn_count[PLAYER_X]) && (1==horizontal_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_X;
			} else
			if((4==horizontal_turn_count[PLAYER_O]) || ((3==horizontal_turn_count[PLAYER_O]) && (1==horizontal_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_O;
			} else
			if((4==vertical_turn_count[PLAYER_X]) || ((3==vertical_turn_count[PLAYER_X]) && (1==vertical_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_X;
			} else
			if((4==vertical_turn_count[PLAYER_O]) || ((3==vertical_turn_count[PLAYER_O]) && (1==vertical_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_O;
			}
		} // end of 'row' loop
		
		//Check winner in diagonals only if it was not found horizontally/vertically
		if(0 != found) {
			if((4==left_diag_turn_count[PLAYER_X]) || ((3==left_diag_turn_count[PLAYER_X]) && (1==left_diag_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_X;
			} else
			if((4==left_diag_turn_count[PLAYER_O]) || ((3==left_diag_turn_count[PLAYER_O]) && (1==left_diag_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_O;
			} else
			if((4==right_diag_turn_count[PLAYER_X]) || ((3==right_diag_turn_count[PLAYER_X]) && (1==right_diag_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_X;
			} else
			if((4==right_diag_turn_count[PLAYER_O]) || ((3==right_diag_turn_count[PLAYER_O]) && (1==right_diag_turn_count[HELPER_CHAR]))) {
				found = 0;
				winner = PLAYER_O;
			}		
		}
		
		// Phase 3: Printing the winner (if there is one)
		cout<<"Case #"<<i+1<<": ";
		if(0 == found){
			cout<<winner<< " won"<<endl;
		} else {
			if(horizontal_turn_count[EMPTY_CHAR] || vertical_turn_count[EMPTY_CHAR] || left_diag_turn_count[EMPTY_CHAR] || right_diag_turn_count[EMPTY_CHAR]) {
				cout<<"Game has not completed"<<endl;
			} else {
				cout<<"Draw"<<endl;
			}
		}
	} // end of all test cases
} //end of main()
