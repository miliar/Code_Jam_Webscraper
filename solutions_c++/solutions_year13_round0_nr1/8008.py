//      tic_tac_toe.cpp
//      
//      Copyright 2013 Antonio <antonio@antonio-laptop>
//      
//      This program is free software; you can redistribute it and/or modify
//      it under the terms of the GNU General Public License as published by
//      the Free Software Foundation; either version 2 of the License, or
//      (at your option) any later version.
//      
//      This program is distributed in the hope that it will be useful,
//      but WITHOUT ANY WARRANTY; without even the implied warranty of
//      MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//      GNU General Public License for more details.
//      
//      You should have received a copy of the GNU General Public License
//      along with this program; if not, write to the Free Software
//      Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
//      MA 02110-1301, USA.


#include <iostream>
#include <fstream>
#include <string.h>
#include <cstdlib>

using namespace std;
//Describe the bot class

/*Codification 
 1: X won
 2: O won
 3: Game has not completed
 4: Draw */

int check_status_game (char game_status[][4]) {
	//Check every row
	int column = 0;
	int row = 0;
	
	bool empty_space = false;
	char init_value = '0';
	
	//Row matching
	for(int i = 0; i <= 3; i++) {
		while(column <= 3) {
			if(column == 0) {	
				if(game_status[i][column] == 'X' || game_status[i][column] == 'T' || game_status[i][column] == 'O') {
					init_value = game_status[i][column];
					column++; 
					cout<<"Init value row parsing  is "<< init_value << endl;
				}		
				else {
					//cout<<"Found row empty space"<<endl;
					empty_space = true;
					break;
				}
			}
			else {
				if(game_status[i][column] != init_value && game_status[i][column] != 'T' && game_status[i][column] != '.' && init_value != 'T') {
					break;//Go to next row
				}
				else if (game_status[i][column] == '.') {
					//cout<<"Found row empty space"<<endl;
					empty_space = true;
					break;
				}
				//Refresh
				else if (init_value == 'T') {
					init_value = game_status[i][column];
					//cout<<"Init refreshed value row parsing  is "<< init_value << endl;
				}
				column++;
			}
			if(column == 4) {
			//A row has been matched
				cout<<"Row has been matched"<<endl;
				switch (init_value) {
					case 'X' : return 1;
					case 'O' : return 2; 
				}
			}
		}
		column = 0;
	}
    //Go to column matching
	
	for(int i = 0; i <= 3; i++) {
		while(row <= 3) {
			if(row == 0) {	
				if(game_status[row][i] == 'X' || game_status[row][i] == 'T' || game_status[row][i] == 'O') {
					init_value = game_status[row][i];
					row++; 
					cout<<"Init value column parsing 1 is "<< init_value << endl;
				}		
				else {
					break;
				}
			}
			else {
				if(game_status[row][i] != init_value && game_status[row][i] != 'T' && game_status[row][i] != '.' && init_value != 'T') {
					break;//Go to next row
				}
				else if (game_status[row][i] == '.') {
					break;
				}
				//Refresh
				else if (init_value == 'T') {
					init_value = game_status[row][i];
					//cout<<"Found a T as initial value in column"<<endl;
				}
				row++;
			}
			if(row == 4) {
			//A row has been matched
				cout<<"Column has been matched"<<endl;
				switch (init_value) {
					case 'X' : return 1;
					case 'O' : return 2; 
				}
			}
		}
		row = 0;
	}
	//Do diagonal matching
	
	//First diagnonal
	init_value = game_status[0][0];
	if(init_value == 'T'){
		init_value = game_status[1][1];
	}	
	if( (init_value == game_status[1][1] || game_status[1][1] == 'T') && (init_value == game_status[2][2] || game_status[2][2] == 'T') && (init_value == game_status[3][3] || game_status[3][3] == 'T') ) {
		cout<<"Diagonal has been matched"<<endl;
		switch (init_value) {
			case 'X' : return 1;
			case 'O' : return 2; 
		}
	}
	
	//cout<<"After first diagonal"<<endl;
	init_value = game_status[0][3];	
	//Second diagonal
	if( (init_value == game_status[1][2] || game_status[1][2] == 'T') && (init_value == game_status[2][1] || game_status[2][1] == 'T') && (init_value == game_status[3][0] || game_status[3][0] == 'T') ) {
		cout<<"Diagonal has been matched"<<endl;
		switch (init_value) {
			case 'X' : return 1;
			case 'O' : return 2;
		} 
	}
		
	//cout<<"After second diagonal"<<endl;
	//If gets here, it is a draw
	if(empty_space == false) {
		return 4;
	}
	else {
		return 3;
	}
}

//Logic
int main(int argc, char** argv)
{
	//Number of test cases
	char cycles_char[4];
	int cycles = 0;
	
	char operations_char = '0';
	
	char line[4][4];
	memset(line, '0',sizeof(line));
	

	//Start to execute the sequence
	string filename = argv[1];
	//Open the filename
	ifstream file_inst (filename.c_str());
	ofstream file_output;
	file_output.open("tic_tac_toe.out",ios::out);
	file_inst >> cycles_char;
	//cycles = cycles_char - '0';
	cout<<"The value of cycles char is "<<cycles_char<<endl;
	cycles = atoi(cycles_char);
	cout<<"The value of cycles is "<<cycles<<endl;
	for(int i = 0 ; i < cycles ; i++)//Number of test cases
	{
		//Populate the matrix
		for (int j = 0; j < 4; j++) {//Row
			for(int p = 0; p < 4 ; p++) {//Column
				file_inst >> operations_char;
				line[j][p] = operations_char;
				//cout << "The value of operations_char is "<<operations_char<<endl;
			}
		}	
		//Check the status
		int result = check_status_game(line);
		cout<<"The result is "<<result << endl;
		char X_won[] = "X won";
		char O_won[] = "O won";
		char draw[] = "Draw";
		char not_end[] = "Game has not completed";
		switch (result) {
			case 1 : file_output<<"Case #"<<(i+1)<<": "<<X_won << endl; 
				break;
			case 2 : file_output<<"Case #"<<(i+1)<<": "<<O_won << endl;
				break;
			case 3 : file_output<<"Case #"<<(i+1)<<": "<<not_end << endl;
				break;
			case 4 : file_output<<"Case #"<<(i+1)<<": "<<draw << endl;
				break;
		}
		
		
		
	}
	file_inst.close();
	file_output.close();
	return 0;
}
