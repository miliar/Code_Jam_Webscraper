#include <iostream>
#include <fstream>
#include <string>

using namespace std;


string board[6];
string result [4]= {"X won", "O won", "Game has not completed", "Draw"};

int check_idiag()
{
	int x=0,o=0,t=0,dot=0;
	int i,j;
	for(i = 3,j =0; i >= 0 ; i--, j++) {
		switch(board[i][j]) {
			case 'T':
				t++;
				break;
			case 'O':
				o++;
				break;
			case 'X':
				x++;
				break;
			case '.':
				dot++;
				break;
			default:
				cout<<"error '"<<board[i][j]<<"'\n";
				break;
		}
	}
	//cout<<x<<" "<<o<<" "<<t<<" "<<dot<<endl;
	if((!x||!o)&& !dot)
		if(x>0)
			return 0;
		else
			return 1;
	else
		return 5;
}
int check_diag()
{
	int x=0,o=0,t=0,dot=0;
	int i,j;
	for(i = j =0; i < 4 ; i++, j++) {
		switch(board[i][j]) {
			case 'T':
				t++;
				break;
			case 'O':
				o++;
				break;
			case 'X':
				x++;
				break;
			case '.':
				dot++;
				break;
			default:
				cout<<"error '"<<board[i][j]<<"'\n";
				break;
		}
	}
	//cout<<x<<" "<<o<<" "<<t<<" "<<dot<<endl;
	if((!x||!o)&& !dot)
		if(x>0)
			return 0;
		else
			return 1;
	else
		return 5;
}

int check_hor()
{

	for(int i =0; i < 4 ; i++) {
		int x=0,o=0,t=0,dot=0;
		for(int j = 0 ; j < 4 ; j++) {
			switch(board[i][j]) {
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				case 'X':
					x++;
					break;
				case '.':
					dot++;
					break;
				default:
					cout<<"error '"<<board[i][j]<<"'\n";
					break;
			}
		}
		//cout<<x<<" "<<o<<" "<<t<<" "<<dot<<endl;
		if((!x||!o)&& !dot)
			if(x>0)
				return 0;
			else
				return 1;
	}
	return 5;
}

int check_vert()
{
	for(int i =0; i < 4 ; i++) {
		int x=0,o=0,t=0,dot=0;
		for(int j = 0 ; j < 4 ; j++) {
			switch(board[j][i]) {
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				case 'X':
					x++;
					break;
				case '.':
					dot++;
					break;
				default:
					cout<<"error '"<<board[i][j]<<"'\n";
					break;
			}
		}
		//cout<<x<<" "<<o<<" "<<t<<" "<<dot<<endl;
		if((!x||!o)&& !dot)
			if(x>0)
				return 0;
			else
				return 1;
	}
	return 5;
}
int check_draw()
{
	int x=0,o=0,t=0,dot=0;
	for(int i =0; i < 4 ; i++) {
		for(int j = 0 ; j < 4 ; j++) {
			switch(board[i][j]) {
				case 'T':
					t++;
					break;
				case 'O':
					o++;
					break;
				case 'X':
					x++;
					break;
				case '.':
					dot++;
					break;
				default:
					cout<<"error '"<<board[i][j]<<"'\n";
					break;
			}
		}
		//cout<<x<<" "<<o<<" "<<t<<" "<<dot<<endl;
	}
	if(dot == 0)
		return 3; // Draw
	else
		return 2; // Not completed
}
int main(int argc, char *argv[])
{

	ifstream fp;
	fp.open(argv[1]);

	if(!fp.is_open())
		cout<<"File open fail!\n";

	int i, j, k, case_no;
	fp>>case_no;
	
	for(i=0; i < case_no; i++) {
		// Read input file

		for(j = 0 ; j < 4 ; j++) {
				board[j].clear();
				fp>>board[j];
				//cout<<board[j]<<endl;
		}

		//Check Win
		int check_no=9999;
		//diagonal
		if((check_no = check_diag())<2) {
			cout<<"Case #"<<i+1<<": "<<result[check_no]<<endl;
			continue;
		}
		if((check_no = check_idiag())<2) {
			cout<<"Case #"<<i+1<<": "<<result[check_no]<<endl;
			continue;
		}
		//horizontal
		if((check_no=check_hor())<2) {
			cout<<"Case #"<<i+1<<": "<<result[check_no]<<endl;
			continue;
		}
		//vertical
		//if(check_vert(j))
		if((check_no=check_vert())<2) {
			cout<<"Case #"<<i+1<<": "<<result[check_no]<<endl;
			continue;
		}
		
		//Check Draw or not completed
		cout<<"Case #"<<i+1<<": "<<result[check_draw()]<<endl;
	}

	return 0;
}
