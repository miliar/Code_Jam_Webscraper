#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
#include <vector>
#include <algorithm>    // std::sort

using namespace std;

#define in_file "A-small-attempt0.in"
#define out_file "A-small-attempt0.out"

void split(const string& s, char c, vector<string>& v){ //string tokenizer
	string::size_type i = 0;
	string::size_type j = s.find(c);
	while(j != string::npos){
		v.push_back(s.substr(i, j-i));
		i = ++j;
		j = s.find(c, j);
		if (j == string::npos) v.push_back(s.substr(i, s.length()));
	}
}

void check(char board[4][4], int round){
	ofstream fout;
	fout.open(out_file, ios::app);
	if(fout.fail()){
		cerr<<"Cannot open file "<<out_file<<endl;
		exit(1);
	};
	bool sbWon = false, isComplete = true;
	//check the copleteness
	for(int i=0; i<4; ++i){
		for(int j=0; j<4; ++j){
			if(board[i][j]=='.')
				isComplete = false;
		}
	}
	char winner;
	//check the rows
	char cur, pre;
	for(int i=0; i<4; ++i){
		pre = board[i][0];
		int j=1;
		for(; j<4; ++j){
			cur = board[i][j];
			if(cur == '.') break;
			if(pre == 'T' && j==1){
				pre = cur;
			}
			if(cur=='T') continue;
			if(pre!=cur) break;
			else{
				pre = cur;
			}
		}
		if(j==4){
			sbWon = true;
			winner = pre;
		}
	}
	if(sbWon){
		fout<<"Case #"<<round<<": "<<winner<<" won"<<endl;
		return;
	}
	//check the cols
	for(int i=0; i<4; ++i){
		pre = board[0][i];
		int j=1;
		for(; j<4; ++j){
			cur = board[j][i];
			if(cur == '.') break;
			if(pre == 'T' && i==1){
				pre = cur;
			}
			if(cur=='T') continue;
			if(pre!=cur) break;
			else{
				pre = cur;
			}
		}
		if(j==4){
			sbWon = true;
			winner = pre;
		}
	}
	if(sbWon){
		fout<<"Case #"<<round<<": "<<winner<<" won"<<endl;
		return;
	}
	//check the left-right diognal
	pre = board[0][0];
	int i=1;
	for(; i<4; ++i){
		cur = board[i][i];
		if(cur == '.') break;
		if(pre == 'T' && i==1){
			pre = cur;
		}
		if(cur=='T') continue;
		if(pre!=cur) break;
		else{
			pre = cur;
		}
	}
	if(i==4){
		sbWon = true;
		winner = pre;
	}
	if(sbWon){
		fout<<"Case #"<<round<<": "<<winner<<" won"<<endl;
		return;
	}
	//check the right-left diognal
	pre = board[0][3];
	i=1;
	for(; i<4; ++i){
		cur = board[i][3-i];
		if(cur == '.') break;
		if(pre == 'T' && i==1){
			pre = cur;
		}
		if(cur=='T') continue;
		if(pre!=cur) break;
		else{
			pre = cur;
		}
	}
	if(i==4){
		sbWon = true;
		winner = pre;
	}
	if(sbWon){
		fout<<"Case #"<<round<<": "<<winner<<" won"<<endl;
		return;
	}
	if(!sbWon){
		if(isComplete)
			fout<<"Case #"<<round<<": "<<"Draw"<<endl;
		else
			fout<<"Case #"<<round<<": "<<"Game has not completed"<<endl;
	}
}

void main(){
	ifstream fin;
	fin.open(in_file);
	string line;
	vector<string> v;
	int N=0;      //the number of test cases
	if(fin.fail()){
		cerr<<"Cannot open file "<<in_file<<endl;
		exit(1);
	};
	getline(fin,line);   //to get N
	if(line == "")
		return;
	N = atoi(line.c_str());
	char board [4][4] ;
	int round = 1;
	for(int i=0; i<N; ++i){
		//convert strings to board
		for(int j=0; j<4; ++j){
			getline(fin,line);
			for(int k=0; k<4; ++k){
				board[j][k] = line[k];
			}
		}
		check(board, round++);
		getline(fin, line);      //for the empty line
	}
}
