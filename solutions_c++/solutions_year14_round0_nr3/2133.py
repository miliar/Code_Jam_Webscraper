#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <queue>
#include <functional>
#include <unordered_set>
#include <time.h>

using namespace std;


const string PATH = "C:/ws/vs_projects/GoogleCodeJam2014/Files/";
const string FILENAME = "C-small-attempt7";


int R, C;
struct Board {
	int placesLeft;
	int posX, posY;
	bool ** cells; // if true it contains a mine
};


int u, v;
Board copyBoard(const Board * board) {
	Board temp = Board();
	temp.cells = new bool*[R];
	for (u = 0; u < R; u++) {
		temp.cells[u] = new bool[C];
		for (v = 0; v < C; v++) {
			temp.cells[u][v] = board->cells[u][v];
		}
	}
	temp.placesLeft = board->placesLeft;
	temp.posX = board->posX;
	temp.posY = board->posY;
	return temp;
}

bool operator>(const Board& a, const Board& b) {
	return a.placesLeft > b.placesLeft;
}



Board * moveBoard(const int xarg, const int yarg, const Board * b) {
	Board * newB = &copyBoard(b);
	newB->posX = xarg;
	newB->posY = yarg;
	if (!newB->cells[newB->posY][newB->posX]) {
		newB->cells[newB->posY][newB->posX] = true;
		newB->placesLeft--;		
	}			
	
	if (newB->posY + 1 < R) { // up
		if (!newB->cells[newB->posY + 1][newB->posX]) {
			newB->placesLeft--;
			newB->cells[newB->posY + 1][newB->posX] = true;	
		}
	}

	if (newB->posX + 1 < C && newB->posY + 1 < R) { // upright
		if (!newB->cells[newB->posY + 1][newB->posX+1]) {
			newB->placesLeft--;
			newB->cells[newB->posY + 1][newB->posX+1] = true;
		}
	}
	if (newB->posX + 1 < C) { // right
		if (!newB->cells[newB->posY][newB->posX + 1]) {
			newB->placesLeft--;
			newB->cells[newB->posY][newB->posX + 1] = true;
		}
	}

	if (newB->posX + 1 < C && newB->posY - 1 >= 0) { // bottomright
		if (!newB->cells[newB->posY - 1][newB->posX + 1]) {
			newB->placesLeft--;
			newB->cells[newB->posY - 1][newB->posX + 1] = true;
		}
	}

	if (newB->posY - 1 >= 0) { // bottom
		if (!newB->cells[newB->posY - 1][newB->posX]) {
			newB->placesLeft--;
			newB->cells[newB->posY - 1][newB->posX] = true;
		}
	}

	if (newB->posX - 1 >= 0 && newB->posY - 1 >= 0) { // bottom left
		if (!newB->cells[newB->posY - 1][newB->posX - 1]) {
			newB->placesLeft--;
			newB->cells[newB->posY - 1][newB->posX - 1] = true;
		}
	}
	
	if (newB->posX - 1 >= 0) { // left
		if (!newB->cells[newB->posY][newB->posX - 1]) {
			newB->placesLeft--;
			newB->cells[newB->posY][newB->posX - 1] = true;
		}
	}

	if (newB->posX - 1 >= 0 && newB->posY + 1 < R) { // top left
		if (!newB->cells[newB->posY + 1][newB->posX - 1]) {
			newB->placesLeft--;
			newB->cells[newB->posY + 1][newB->posX - 1] = true;
		}
	}

	return newB;
}


vector<Board> visited;
bool cellsEqual;
bool containsBoard(const Board * b) {
	for (int k = 0; k < visited.size(); k++) {
		cellsEqual = true;
		if (b->posX != visited.at(k).posX || b->posY != visited.at(k).posY) continue;
		for (u = 0; u < R; u++) {
			for (v = 0; v < C; v++) {
				if (visited.at(k).cells[u][v] != b->cells[u][v]) {
					cellsEqual = false;
					break;
				}
			}
			if (!cellsEqual) break;
		}
		if (cellsEqual) return true;
	}
	
	return false;
}



int main() {
	ifstream fin(PATH + FILENAME + ".in");
	ofstream out(PATH + FILENAME + ".out");

	int T, t, M, x, y, i, j;
	bool found = false;
	fin >> T;
	
	t = T;
	
	priority_queue<Board, vector<Board>, greater<Board>> pqueue;
	while (--t >= 0) {
		fin >> R >> C >> M;
		Board current = Board();
		Board next;
		found = false;
		// check on special case: only 1 place free (places-mines=1) 
		
		// TODO: create board with just a click and the rest mines..
		
		visited = vector<Board>();		
		pqueue = priority_queue<Board, vector<Board>, greater<Board>>();
		
		
		// start possibilities, clicked on position x, y	
		// rule: around revealing cell it should always be empty!
		
		
		current.cells = new bool*[R];
		for (i = 0; i < R; i++) {
			current.cells[i] = new bool[C];
			for (j = 0; j < C; j++) {
				current.cells[i][j] = false;
			}
		}
		/*srand(time(NULL));*/
		y = 0;
		x = 0;

		current.posX = x;
		current.posY = y;
		current.cells[y][x] = true; 
		current.placesLeft = (R * C) - M - 1; // -1 because we set the first one (clicked cell)
		if (current.placesLeft != 0) {
			// place around empty click:
			current = *moveBoard(x, y, &current);		
		}

		pqueue.push(current);
		while (!pqueue.empty() && (current = pqueue.top()).placesLeft > 0) {
			current = pqueue.top();
			pqueue.pop();
			if (containsBoard(&current)) {
				continue;
			}
			visited.push_back(current);					
					
			if (current.posY + 1 < R) { // try up
				next = *moveBoard(current.posX, current.posY + 1, &current);
				if (next.placesLeft == 0) {
					current = next;
					found = true;
					break;
				}
				if (next.placesLeft > 0) pqueue.push(next);						
			}


			if (current.posX + 1 < C) { // try right
				next = *moveBoard(current.posX + 1, current.posY, &current);	
				if (next.placesLeft > 0) pqueue.push(next);
				if (next.placesLeft == 0) {
					current = next;
					found = true;
					break;
				}
			}

			if (current.posY - 1 >= 0 ) { // try bottom
				next = *moveBoard(current.posX, current.posY - 1, &current);
				if (next.placesLeft > 0) pqueue.push(next);
				if (next.placesLeft == 0) {
					current = next;
					found = true;
					break;
				}
			}


			if (current.posX - 1 >= 0) { // try left
				next = *moveBoard(current.posX - 1, current.posY, &current);
				if (next.placesLeft > 0) pqueue.push(next);
				if (next.placesLeft == 0) {
					current = next;
					found = true;
					break;
				}
			}
		}
		if (current.placesLeft == 0) found = true;
							
		// Output:
		out << "Case #" << (T - t) << ":\n";
		if (!found) {
			out << "Impossible\n";
		}
		else {
			for (i = 0; i < R; i++) {
				for (j = 0; j < C; j++) {
					if (i == y && j == x) {
						out << "c";
					}
					else {
						out << (current.cells[i][j] ? "." : "*");
					}
				}
				out << "\n";
			}
		}		
	}

	system("pause");
	return 0;
}