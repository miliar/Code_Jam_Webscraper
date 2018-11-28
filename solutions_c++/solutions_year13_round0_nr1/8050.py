#include <string>
#include <stdio.h>
#include <fstream>
#include <Windows.h>

using namespace std;

#define SIZE 4

struct Game {
	char input[SIZE][SIZE];
	char output[50];
};

enum { DRAW, X, O, DOT };

int setStatus(char ch) {
	if(ch == 'X') return X;
	if(ch == 'O') return O;
}

char *result[4] = { "Draw", "X won", "O won", "Game has not completed" };

DWORD WINAPI whoWins (LPVOID param) {
	struct Game *game = (struct Game*)param;
	int i,j;
	int status = DRAW;
	char ch;
	
	//Check on ROW wise
	for(i=0;i<SIZE;i++) {
		ch = game->input[i][0];

		if(ch == '.') {
			status = DOT;
			continue;
		}

		if(ch == 'T') {
			ch = game->input[i][1];
		}

		bool skip = false;
		for(j=1;j<SIZE&&!skip;j++) {
			//Encounter a dot
			if(game->input[i][j]=='.') {
				status = DOT;
				skip = true;
			} else if(game->input[i][j] == ch || game->input[i][j] == 'T'){
				//if its a last ch
				if(j==SIZE-1) {
					status = setStatus(ch);
					goto EndDiagonal;
				}
			} else {
				skip = true;
			}
		}
	}
	
	//Check on Column wise
	for(j=0;j<SIZE;j++) {
		ch = game->input[0][j];

		if(ch == '.') {
			status = DOT;
			continue;
		}

		if(ch == 'T') {
			ch = game->input[1][j];
		}

		bool skip = false;
		for(i=1;i<SIZE&&!skip;i++) {
			//Encounter a dot
			if(game->input[i][j]=='.') {
				status = DOT;
				skip = true;
			} else if(game->input[i][j] == ch || game->input[i][j] == 'T'){
				//if its a last ch
				if(i==SIZE-1) {
					status = setStatus(ch);
					goto EndDiagonal;
				}
			} else {
				skip = true;
			}
		}
	}

AfterCol:

	//First Diagonal check
	ch = game->input[0][0];
	if(ch == '.') {	
		status = DOT;
		goto SecondDiagonal;
	}

	if(ch == 'T') {
		ch = game->input[i+1][i+1];
	}

	for(i=1;i<SIZE;i++) {

		if(game->input[i][i] == '.') {
			status = DOT;
			break;
		}

		if(game->input[i][i] == ch || game->input[i][i] == 'T') {
			if(i==SIZE-1) {
				status = setStatus(ch);
				goto EndDiagonal;
			}	
		} else {
			break;
		}

	}

SecondDiagonal:

	//Second Diagonal check
	ch = game->input[0][SIZE-1];
	if(ch == '.') {	
		status = DOT;
		goto EndDiagonal;
	}

	if(ch == 'T') {
		ch = game->input[1][SIZE-2];
	}

	for(i=1;i<SIZE;i++) {

		if(game->input[i][SIZE-(i+1)] == '.') {
			status = DOT;
			break;
		}

		if(game->input[i][SIZE-(i+1)] == ch || game->input[i][SIZE-(i+1)] == 'T') {
			if(i==SIZE-1) {
				status = setStatus(ch);
				goto EndDiagonal;
			}	
		} else {
			break;
		}

	}

EndDiagonal:
	strcpy(game->output, result[status]);
	return 0;
}

int main() {

	int T;
	string input;
	char filename[50];

	printf("Enter the testcase filename: ");
	scanf("%s",filename);

	ifstream file(filename);

	if(file >> T) {
		//printf("\nTestcase: %d\n",T);
	} else {
		printf("Invalid file\n");
		system("pause");
		return 0;
	}
	
	//Reads empty line
	getline(file,input);

	HANDLE *hThread = new HANDLE[T];
	struct Game *board = new struct Game[T];

	for(int i=0;i<T;i++) {
		
		//Reads board values
		getline(file,input);
		strncpy(board[i].input[0],input.c_str(),4);
		getline(file,input);
		strncpy(board[i].input[1],input.c_str(),4);
		getline(file,input);
		strncpy(board[i].input[2],input.c_str(),4);
		getline(file,input);
		strncpy(board[i].input[3],input.c_str(),4);
		
		//Reads empty line
		getline(file,input);
	
		for(int t=0;t<SIZE;t++) {
			for(int j=0;j<SIZE;j++) {
				printf("%c",board[i].input[t][j]);
			}
			printf("\n");
		}
		printf("\n");

		hThread[i] = CreateThread( NULL,0,whoWins,&board[i],0,0);
	}
	file.close();

	ofstream outfile("output.txt");

	printf("\nOutput\n");
	for(int i=0;i<T;i++) {
		char output[100];
		WaitForSingleObject( hThread[i], INFINITE );
		sprintf(output,"Case #%d: %s\n",i+1,board[i].output);
		printf("%s",output);
		outfile<<output;
		
	}
	
	outfile.close();

	system("pause");
	return 0;
}