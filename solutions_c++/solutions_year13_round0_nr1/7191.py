/*
 * Problem
 * 
 * Tic-Tac-Toe-Tomek is a game played on a 4 x 4 square board. The
 * board starts empty, except that a single 'T' symbol may appear in
 * one of the 16 squares. There are two players: X and O. They take
 * turns to make moves, with X starting. In each move a player puts
 * her symbol in one of the empty squares. Player X's symbol is 'X',
 * and player O's symbol is 'O'. 
 *
 * After a player's move, if there is a row, column or a diagonal
 * containing 4 of that player's symbols, or containing 3 of her
 * symbols and the 'T' symbol, she wins and the game ends. Otherwise
 * the game continues with the other player's move. If all of the
 * fields are filled with symbols and nobody won, the game ends in a
 * draw. See the sample input for examples of various winning
 * positions. 
 *  
 * Given a 4 x 4 board description containing 'X', 'O', 'T' and '.'
 * characters (where '.' represents an empty square), describing the
 * current state of a game, determine the status of the
 * Tic-Tac-Toe-Tomek game going on. The statuses to choose from are: 
 *  
 * "X won" (the game is over, and X won) 
 * "O won" (the game is over, and O won) 
 * "Draw" (the game is over, and it ended in a draw) 
 * "Game has not completed" (the game is not over yet) 
 * If there are empty cells, and the game is not over, you should
 * output "Game has not completed", even if the outcome of the game is
 * inevitable. 
 * Input 
 *  
 * The first line of the input gives the number of test cases, T. T
 * test cases follow. Each test case consists of 4 lines with 4
 * characters each, with each character being 'X', 'O', '.' or 'T'
 * (quotes for clarity only). Each test case is followed by an empty
 * line. 
 *  
 * Output 
 *  
 * For each test case, output one line containing "Case #x: y", where
 * x is the case number (starting from 1) and y is one of the statuses
 * given above. Make sure to get the statuses exactly right. When you
 * run your code on the sample input, it should create the sample
 * output exactly, including the "Case #1: ", the capital letter "O"
 * rather than the number "0", and so on. 
 *  
 * Limits 
 *  
 * The game board provided will represent a valid state that was
 * reached through play of the game Tic-Tac-Toe-Tomek as described
 * above. 
 *  
 * Small dataset 
 *  
 * 1 ≤ T ≤ 10. 

 * Large dataset 
 *  
 * 1 ≤ T ≤ 1000. 
 *  
 * Sample 
 *  
 *  
 * Input  
 *  	 
 * Output  
 *   
 * 6 
 * XXXT 
 * .... 
 * OO.. 
 * .... 
 *  
 * XOXT 
 * XXOO 
 * OXOX 
 * XXOO 
 *  
 * XOX. 
 * OX.. 
 * .... 
 * .... 
 *  
 * OOXX 
 * OXXX 
 * OX.T 
 * O..O 
 *  
 * XXXO 
 * ..O. 
 * .O.. 
 * T... 
 *  
 * OXXX 
 * XO.. 
 * ..O. 
 * ...O 
 *  
 * Case #1: X won 
 * Case #2: Draw 
 * Case #3: Game has not completed 
 * Case #4: O won 
 * Case #5: O won 
 * Case #6: O won 
 *  
 * Note 
 *  
 * Although your browser might not render an empty line after the last 
 * test case in the sample input, in a real input file there would be 
 * one.  
 */  

#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>
#include <cassert>

using namespace std;

#define TTTT_BOARD_MAX_ROWS 4
#define TTTT_BOARD_MAX_COLS 4
#define MAX_PLAYER_STATE (TTTT_BOARD_MAX_ROWS + TTTT_BOARD_MAX_COLS + 2)

char tttt_board[TTTT_BOARD_MAX_ROWS][TTTT_BOARD_MAX_COLS] = {'\0'};

typedef enum {
	GAME_STATE_MIN		   = 0,

	// valid states
	GAME_STATE_X_WON	   = 1,
	GAME_STAT_O_WON		   = 2,
	GAME_STATE_GAME_IS_DRAW	   = 3,
	GAME_STATE_GAME_UNFINISHED = 4,
	
	GAME_STATE_MAX,
} game_state_t;

#define VALID_GAME_STATE(state) ((state > GAME_STATE_MIN) && (state < GAME_STATE_MAX))

const char *game_state_string[] = {
	"UNKNOWN-STATE",
	"X won",					    // X_WON_THE_GAME
	"O won",					    // O_WON_THE_GAME
	"Draw",						    // GAME_IS_DRAW
	"Game has not completed",			    // GAME_UNFINISHED
};

typedef struct {
	unsigned short row[TTTT_BOARD_MAX_ROWS];
	unsigned short col[TTTT_BOARD_MAX_COLS];
	unsigned short diag[2];
} player_tick_t;

static const char*
get_game_state_string(game_state_t state)
{
	if (!VALID_GAME_STATE(state)) {
		return "INVALID-GAME-STATE";
	}
	
	return game_state_string[state];
}

static void
debug_dump_tttt_board(bool do_debug)
{
	if (do_debug) {
		for (int row = 0; row < TTTT_BOARD_MAX_ROWS; row++) {
			for (int col = 0; col < TTTT_BOARD_MAX_COLS; col++) {
				cout << tttt_board[row][col];
			}
			cout << endl;
		}

		cout << "---" << endl;
	}
	

	return;
}

// a player can win only if there are '4' marks in
// horizontal/vertical/diagonal position for their pieces
static bool
has_player_won(const player_tick_t pt)
{
	bool won = false;

	// check rows
	if (!won) {
		for (int r = 0; !won && r < TTTT_BOARD_MAX_ROWS; r++) {
			won = (pt.row[r] == 4);
		}
	}

	// check columns
	if (!won) {
		for (int c = 0; !won && c < TTTT_BOARD_MAX_ROWS; c++) {
			won = (pt.col[c] == 4);
		}
	}

	// check diagonal
	if (!won) {
		won = ((pt.diag[0] == 4) || (pt.diag[1] == 4));
	}
	
	return won;
}

static void
debug_dump_player_moves(const char *player,
			const player_tick_t& pt)
{
	cout << "---" << player << "---" << endl;
	
	// rows
	cout << "row-moves: ( ";
	for (int r = 0; r < TTTT_BOARD_MAX_ROWS; r++) {
		cout << pt.row[r] << ", ";
	}
	cout << " )" << endl;

	// columns
	cout << "col-moves: ( ";
	for (int c = 0; c < TTTT_BOARD_MAX_COLS; c++) {
		cout << pt.col[c] << ", ";
	}
	cout << " )" << endl;
	
	// diagonals
	cout << "diag-moves: ( "
	     << pt.diag[0] << ", "
	     << pt.diag[1] << " )"
	     << endl; 

	return;
}

static void
update_ticks(player_tick_t &pt,
	     int i,					    // row
	     int j)					    // col
{
	pt.row[i] += 1;
	pt.col[j] += 1;
	
	if (i == j) {
		pt.diag[0] += 1;
	}
	
	if ((i+j) == TTTT_BOARD_MAX_ROWS - 1) {
		pt.diag[1] += 1;
	}
	
	return;
}

/*
 * we basically are trying to brute-force our way out of this
 * one. since the board dimensions are small enough, i think it should
 * basically work.
 *
 * couple of points on this process:
 *
 *   1. for every board game, we need to figure out iff either 'X' or
 *      'O' actually won
 *
 *   2. if (1) doesn't work, then we check iff there are still
 *      non-used positions on the board. if yes ==>
 *      GAME_STATE_GAME_UNFINISHED
 *
 *   3. if neither (1) nor (2) is satisfied ==>
 *   GAME_STATE_GAME_IS_DRAW.
 *
 * so, for both the players, we have a vector of [10] values
 * corresponding to number of places where that player has marked his
 * move. 10 because 4 (row) + 4 (column) + 2 (diagonal)
 *
 * 'T' is just counted towards 'X' as well as towards 'O' while doing
 * the above mentioned processing.
 *
 * all-right !
 */
static game_state_t
compute_game_state(void)
{
	player_tick_t x_ticks = {'\0'};
	player_tick_t o_ticks = {'\0'};
	bool available = false;

	for (int i = 0; i < TTTT_BOARD_MAX_ROWS; i++) {
		for (int j = 0; j < TTTT_BOARD_MAX_COLS; j++) {
			char ch = tttt_board[i][j];

			switch (ch) {
			case 'X':
				update_ticks(x_ticks, i, j);
				break;

			case 'O':
				update_ticks(o_ticks, i, j);
				break;

			case 'T':
				update_ticks(x_ticks, i, j);
				update_ticks(o_ticks, i, j);
				break;

			case '.':
				available = true;
				break;
			default:
				break;
			}
		}
	}

	bool x_won = has_player_won(x_ticks);
	bool o_won = has_player_won(o_ticks);

	if (x_won) {
		return GAME_STATE_X_WON;
	}

	if (o_won) {
		return GAME_STAT_O_WON;
	}

	if (available == true && x_won == false && o_won == false) {
		return GAME_STATE_GAME_UNFINISHED;
	}

	return GAME_STATE_GAME_IS_DRAW;
}

static void
dump_results(int tc,game_state_t gs)
{
	cout << "Case #" << tc << ": "
	     << get_game_state_string(gs)
	     << endl;

	return;
}

int main(int argc, char **argv)
{
	ifstream ifs(argv[1]);
	int num_tc = 0;
	string line;
	game_state_t gs = GAME_STATE_MIN;

	ifs >> num_tc;
	getline(ifs, line);

	for (int i = 0; i < num_tc; i++) {
		for (int row = 0; row < TTTT_BOARD_MAX_ROWS; row++) {
			ifs >> tttt_board[row][0]
			    >> tttt_board[row][1]
			    >> tttt_board[row][2]
			    >> tttt_board[row][3];
		}

		debug_dump_tttt_board(false);
		
		gs = compute_game_state();
		dump_results(i+1, gs);
	}

	return 0;
}


/*
 * Local Variables:
 * compile-command : "g++ tttt.cpp -o obj/tttt"
 * End:
 */
