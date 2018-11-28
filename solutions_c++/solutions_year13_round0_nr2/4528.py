#include <iostream>
#include <vector>

using namespace std;

void flatten(int threshold, vector< vector<int> > &board) {
	int height = board.size();
	int width = board[0].size();

	// horizontal
	for(int i=0; i<height; i++) {
		bool cuttable = true;
		for(int j=0; j<width; j++)
			cuttable &= ((board[i][j] == threshold) || board[i][j] == 0);

		if(cuttable)
			for(int j=0; j<width; j++)
				board[i][j] = 0;
	}

	// vertical
	for(int j=0; j<width; j++) {
		bool cuttable = true;
		for(int i=0; i<height; i++)
			cuttable &= ((board[i][j] == threshold) || (board[i][j] == 0));

		if(cuttable)
			for(int i=0; i<height; i++)
				board[i][j] = 0;
	}
}

bool isAllZero(vector< vector<int> > &board) {
	int height = board.size();
	int width = board[0].size();

	for(int i=0; i<height; i++) {
		for(int j=0; j<width; j++) {
			if(board[i][j] > 0)
				return false;
		}
	}

	return true;
}

void printBoard(vector< vector<int> > &board) {
	int height = board.size();
	int width = board[0].size();

	for(int i=0; i<height; i++) {
		for(int j=0; j<width; j++) {
			cout << board[i][j] << " ";
		}
		cout << endl;
	}
}

void computeBoard(int T, vector< vector<int> > &board) {
//	printBoard(board);
	for(int i=1; i<=100; i++)
		flatten(i, board);
	
	string output = isAllZero(board) ? "YES" : "NO";

	cout << "Case #" << T << ": " << output << endl;
//	printBoard(board);
}

int main() {
	int T, N, M;
	cin >> T;

	for(int i=1; i<=T; i++) {
		cin >> N >> M;
		vector< vector<int> > board(N, vector<int>(M, 0));

		for(int j=0; j<N; j++) for(int k=0; k<M; k++) {
			cin >> board[j][k];
		}

		computeBoard(i, board);
	}
}
