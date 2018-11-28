/*
Code Jam 2013 Round 1 A
Tyler Allen 
C++
Solve Code Jam:Round 1: A Large and Small Sets
*/

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <sstream>
using namespace std;
int score(int board[4][4]){
	int max;
	max=0;
	int scores[8]={};
	int tempx,tempy;
	for(int x=0;x<4;x++){
		tempx=tempy=0;
		for(int y=0;y<4;y++){
			tempx=(tempx+board[x][y])*((x==3)?1:board[x][y]);
			tempy=(tempy+board[y][x])*((y==3)?1:board[y][x]);
			if(x==y)
				scores[2]=(scores[2]+board[x][y])*((y==3)?1:board[x][y]);
			if((x+y)==3)
				scores[3]=(scores[3]+board[x][y])*((y==3)?1:board[x][y]);
			if((x-1)==y)
				scores[4]=(scores[4]+board[x][y]);
			if(x==(y-1))
				scores[5]=(scores[5]+board[x][y]);
			if(x+y==2)
				scores[6]=(scores[6]+board[x][y]);
			if(x+y==4)
				scores[7]=scores[7]+board[x][y];
		}
		if(scores[0]<tempx)
			scores[0]=tempx;
		if(scores[1]<tempy)
			scores[1]=tempy;
	}
	for(int i=0;i<8;i++){
		
		max=(scores[i]>max)?scores[i]:max;
	}
	return (max<3)?0:max;
}
string printWinner(char winner,int num){
	stringstream ss;
	if(winner=='n')
		ss <<"Case #"<<num<<": Game has not completed\n";
	else if(winner=='d')
		ss<<"Case #"<<num<<": Draw\n";
	else
		ss<< "Case #"<<num<<": "<<winner<<" won\n";
	return ss.str();
}
int main () {

	
	fstream input;
	ofstream output("codeJam1aoutsmall.txt");
	input.open("A-small-attempt2.in");
	
	string temp;
	input >> temp;
	int iterations=atoi(temp.c_str());
	string boards[iterations];
	for(int i=0;i<iterations;i++){
		for(int j=0;j<4;j++){
			input >>temp;
			boards[i]=boards[i]+temp+'\n';
		}
		
	}
	int boardx[4][4];
	int boardo[4][4];
	int counter=0;
	int scorex,scoreo;
	bool inc;
	for(int i=0;i<iterations;i++){
		counter=0;
		inc=false;
		for(int y=0;y<4;y++){	
			for(int x=0;x<4;x++){
				char val=boards[i][counter];
				if(val=='X'){
					boardx[x][y]=1;
					boardo[x][y]=0;
				}
				else if(val=='O'){
					boardo[x][y]=1;
					boardx[x][y]=0;
				}
				else if(val=='T')
				{
					boardo[x][y]=1;
					boardx[x][y]=1;
				}
				else{
					boardo[x][y]=0;
					boardx[x][y]=0;
					inc=true;
				}
				counter++;
			}
			counter++;
		}
		scorex=score(boardx);
		scoreo=score(boardo);
		if(scoreo==scorex&&scoreo!=0)
			output<<printWinner('d',i+1);
		else if(scorex>scoreo)
			output<<printWinner('X',i+1);
		else if(scoreo>scorex)
			output<<printWinner('O',i+1);
		else if(inc){
			output << printWinner('n',i+1);
		}
	}
	input.close();
}