#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <vector>

using namespace std;

template <class T>
void print_vector(const vector<T> vec, int width=0, char delim='\0'){
	for (typename vector< vector<T> >::size_type i = 0; i != vec.size(); i++){
		cout << setw(width) << vec[i] << delim;
	}
	cout << endl;
}

template <class T>
void print_board(const vector< vector<T> > board, int width=0, char delim='\0'){
	for (typename vector< vector<T> >::size_type i = 0; i != board.size(); i++){
		print_vector(board[i], width, delim);
	}
}

char check_vector(vector<char> vec){
	char prev, curr, res;
	
	for (typename vector<char>::size_type i = 0; i != vec.size(); i++){
		curr = vec[i];
		//printf("prev: %c, curr: %c\n", prev, curr);
		if (curr == '.'){
			//cout << "period" << endl;
			return 'F';
		}
		
		if (curr == 'T'){
			continue;
		}
		
		if (i == 0){
			prev = curr;
		}
		
		if (prev != curr){
			return 'F';
		}
		res = curr;
		prev = curr;
	}
	return res;
	
}

int main(){
	int cases;
	int size = 4;
	char ch, res;
	bool over, complete;
	vector< vector<char> > board, rows;
	vector<char> row;

	cin >> cases;
	
	for (int i = 0; i < cases; i++){
		complete = true;
		over = false;
		for (int j = 0; j < size; j++){
			row.clear();
			board.push_back(row);
			row.clear();
			for (int k = 0; k < size; k++){
				cin >> ch;
				if (ch == '.'){
					complete = false;
				}
				board[j].push_back(ch);
			}
		}
		// print_board(board);
		// cout << endl;
		// add rows to list
		for (int j = 0; j < size; j++){
			rows.push_back(board[j]);
		}
		
		// add columns to list
		for (int j = 0; j < size; j++){
			for (int k = 0; k < size; k++){
				row.push_back(board[k][j]);
			}
			rows.push_back(row);
			row.clear();
		}
		
		// add diagonals to list
		for (int j = 0; j < size; j++){
			row.push_back(board[j][j]);
		}
		rows.push_back(row);
		row.clear();
		
		for (int j = 0; j < size; j++){
			row.push_back(board[j][size-j-1]);
		}
		rows.push_back(row);
		row.clear();
		
		typename vector< vector<char> >::size_type j;
		for (j = 0; j != rows.size(); ++j){
			res = check_vector(rows[j]);
			//cout << "current row: ";
			//print_vector(rows[j]);
			if (res == 'X' || res == 'O'){
				printf("Case #%d: %c won\n", i+1, res);
				over = true;
				break;
			}
		}
		
		rows.clear();
		
		if (over){
			board.clear();
			continue;
		}
		
		else if (complete){
			printf("Case #%d: Draw\n", i+1);
		}
		
		else {
			printf("Case #%d: Game has not completed\n", i+1);
		}
		
		board.clear();
	}
}

// keep track of
// board completeness
