//============================================================================
// Name        : Tic-Tac-Toe-Tomek.cpp
// Author      : 
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main() {
	/*---------------------------------read data*/
	ifstream nmbs("data.txt");
	size_t it  = 0;

	fstream out;
	out.open("out.txt", std::ios::out);

	if (!nmbs){
		cout << "can't open file to read";
		return 1;
	}
	if(!out.good()){
		cout << "can't open file to write";
		return 1;
	}

	int game_size;
	nmbs >> game_size;
	int tab_size = game_size*16;
	char *data = new char[tab_size];

	while (!nmbs.eof()){
		nmbs >> data[it++];
	}
	nmbs.close();

	long int case_num;
	long int offset = 0;
	char* s;
	/*------------------------------------algorithm*/
	for(case_num = 0; case_num < game_size; case_num++){
		bool done = false;
		s = &(data[offset]);

		for(int i = 0; i < 4; i++){
			if(*s != '.'){
				if(*s == 'T'){
					if(*(s+1) == *(s+2) && *(s+2) == *(s+3) && *(s+1)!='.'){
						out << "Case #"<< case_num+1 <<": "<< *(s+1) <<" won" << endl;
						done =  true;
						break;
					}
				}
				else{
					if((*s == *(s+1) || *(s+1)=='T') && (*s == *(s+2) || *(s+2)=='T' )&& (*s == *(s+3)|| *(s+3)=='T')){
						out << "Case #"<< case_num+1 <<": "<< *s <<" won" << endl;
						done = true;
						break;
					}
				}
			}
			s=s+4;
		}
		if(done){
			offset +=16;
			continue;
		}

		s = &(data[offset]);


		for(int i = 0; i < 4; i++){
			if(*s != '.'){
				if(*s == 'T'){
					if(*(s+4) == *(s+8) && *(s+8) == *(s+12) && *(s+4)!='.'){
						out << "Case #"<< case_num+1 <<": "<< *(s+4) <<" won" << endl;
						done = true;
						break;
					}
				}
				else{
					if((*s == *(s+4) || *(s+4)=='T') && (*s == *(s+8) || *(s+8)=='T' )&& (*s == *(s+12)|| *(s+12)=='T')){
						out << "Case #"<< case_num+1 <<": "<< *s <<" won" << endl;
						done = true;
						break;
					}
				}
			}
			s = s+1;
		}
		if(done){
			offset +=16;
			continue;
		}


		s = &(data[offset]);
		if(*s != '.'){
			if(*s == 'T'){
				if(*(s+5) == *(s+10) && *(s+10) == *(s+15) && *(s+5)!='.'){
					out << "Case #"<< case_num+1 <<": "<< *(s+5) <<" won" << endl;
					done =  true;
					break;
				}
			}
			else{
				if((*s == *(s+5) || *(s+5)=='T') && (*s == *(s+10) || *(s+10)=='T' )&& (*s == *(s+15)|| *(s+15)=='T')){
					out << "Case #"<< case_num+1 <<": "<< *s <<" won" << endl;
					done = true;
					break;
				}
			}
		}

		s=s+3;
		if(*s != '.'){
			if(*s == 'T'){
				if(*(s+3) == *(s+6) && *(s+6) == *(s+9) && *(s+3)!='.'){
					out << "Case #"<< case_num+1 <<": "<< *(s+3) <<" won" << endl;
					offset+=16;
					continue;
				}
			}
			else{
				if((*s == *(s+3) || *(s+3)=='T') && (*s == *(s+6) || *(s+6)=='T' )&& (*s == *(s+9)|| *(s+9)=='T')){
					out << "Case #"<< case_num+1 <<": "<< *s <<" won" << endl;
					offset+=16;
					continue;
				}
			}
		}
		s = &(data[offset]);
		for(int i = 0; i<16; i++){
			if(*(s+i)=='.'){
				out << "Case #"<< case_num+1 <<": Game has not completed" << endl;
				done = true;
				break;
			}
		}
		if(!done)
			out << "Case #"<< case_num+1 <<": Draw" << endl;
		offset +=16;
	}
	out.close();
	return 0;
}
