#include <iostream>
#include <fstream>

char getPos(const char (&board)[16], int x, int y) {
	return board[x*4+y];
}

char match(const char (&board)[16], char c, int x, int y, int dx, int dy) {
	char t;
	while ( ((x+=dx) < 4) && ((y+=dy)<4) ) {
		t = getPos(board,x,y);
		if ( c != t && 'T' != t ) {
			return ' ';
		}
	}
	return c;
}

//x, y, dx, dy

const int checkpoints = 10;
int points[checkpoints*4] = {0,0,1,0 ,0,0,0,1 ,0,0,1,1 ,0,3,1,-1 ,0,1,1,0 ,0,2,1,0, 0,3,1,0 ,1,0,0,1 ,2,0,0,1, 3,0,0,1};

int main(int argv, char** argc) {
	int T, counter;
	char board[16], c, winner;
	bool empty;
	std::ifstream file("tttt.in");
	std::ofstream out("tttt.out");
	file >> T;
	file.get(c); // skip the first
	for ( int i = 0; i<T; ++i ) {
		counter = 0;
		empty = false;
		winner = ' ';
		for ( int j = 0; j < 21; ++j ) {
			file.get(c);
			if ( '\n' != c ) {
				if ( '.' == c ) {
					empty = true;
				}
				board[counter++] = c;
			}
		}
		for ( int j = 0; j < checkpoints*4; j+= 4) {
			c = getPos(board, points[j],points[j+1]);
			if ( '.' != c ) {
				if ('T' == c ) {
					c = match(board, 'O', points[j], points[j+1], points[j+2], points[j+3]);
					if ( ' ' != c ) {
						winner = c;
						break;
						// this is won
					}
					c = match(board, 'X', points[j], points[j+1], points[j+2], points[j+3]);
					if ( ' ' != c ) {
						winner = c;
						break;
						// this is won
					}
				} else {
					c = match(board, c, points[j], points[j+1], points[j+2], points[j+3]);
					if ( ' ' != c ) {
						winner = c;
						break;
						// this is won
					}
				}
			}
		}
		out << "Case #" << i + 1 << ": ";
		if ( ' ' != winner ) {
			// someone won
			out << winner << " won";
		} else if ( !empty ) {
			out << "Draw";
		} else {
			out << "Game has not completed";
		}
		out << std::endl;
		// only deal with the top and left columns, rest are not important
	}
}