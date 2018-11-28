/*
	Using Dev C++ compiler
*/
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>
using namespace std;

int main()
{
	int T, N = 1;
	
	int countX[4], countY[4];
	
	int symbolT;
	bool haveWin;
	bool haveEmpty = false;
	ofstream out;
	out.open("e:/problem_A.out");
	ifstream in;
	in.open("e:/A-large.in");
	string line;
	getline(in, line);
	T = atoi(line.c_str());
	//cout << T;
	while(N <= T ){
		
		string row[4];
		for(int i = 0; i< 4; i++){
			getline(in, row[i]);
			//cout <<i<<" "<< row[i] <<endl;
		}
		
		haveWin = false;
		haveEmpty = false;
		int her = 0;
		
		for( her = 0; her< 4; her++ ){
			//Horizon
			symbolT = 0;
			// reset count
			for(int i = 0; i<4; i++)
			{
				countX[i] = countY[i] = 0;
			}
		
			for( int i = 0; i< 4; i++){
				if(row[her][i]=='X'){
					countX[her] ++;
				}
				else if(row[her][i]=='O')
				{
					countY[her]++;
				}	
				else if( row[her][i] == 'T'){
					symbolT ++;
				}
				else {
					haveEmpty = true;
				}
			}
			
			// check win herizon
			if((countX[her] == 3 && symbolT == 1) || countX[her] == 4)
			{
				//X win
				out << "Case #" << N <<": X won"<<endl;
				haveWin = true;
				break;
			}
			else if((countY[her] == 3 && symbolT == 1) || countY[her] == 4)
			{
				//X win
				out << "Case #" << N <<": O won"<<endl;
				haveWin = true;
				break;
			}
			
			// vertical
			symbolT = 0; // reset -> have no T
			// reset count
			for(int i = 0; i<4; i++)
			{
				countX[i] = countY[i] = 0;
			}
		
			for( int i = 0; i< 4; i++){
				if(row[i][her]=='X'){
					countX[her] ++;
				}
				else if(row[i][her]=='O')
				{
					countY[her]++;
				}	
				else if( row[i][her] == 'T'){
					symbolT ++;
				}
				else {
					haveEmpty = true;
				}
			}
			
			// check win vertical
			if((countX[her] == 3 && symbolT == 1) || countX[her] == 4)
			{
				//X win
				out << "Case #" << N <<": X won"<<endl;
				haveWin = true;
				break;
			}
			else if((countY[her] == 3 && symbolT == 1) || countY[her] == 4)
			{
				//X win
				out << "Case #" << N <<": O won"<<endl;
				haveWin = true;
				break;
			}
		}
		
		if( !haveWin){
			// diagonal main
			symbolT = 0;	
			// reset count
			countX[0] = countY[0] = 0;// main
			for( int i = 0; i< 4; i++)
			{
				if( row[i][i] == 'X')
				{
					countX[0]++;
				}
				else if(row[i][i]== 'O'){
					countY[0]++;
				}
				else if(row[i][i]=='T')
				{
					symbolT ++;
				}
				else{
					haveEmpty  = true;
				}
			}
			// check win diagonal
			if((countX[0] == 3 && symbolT == 1) || countX[0] == 4)
			{
				//X win
				out << "Case #" << N <<": X won"<<endl;
				haveWin = true;
			}
			else if((countY[0] == 3 && symbolT == 1) || countY[0] == 4)
			{
				//X win
				out << "Case #" << N <<": O won"<<endl;
				haveWin = true;
			}
		}
		
		if(!haveWin)
		{
			// diagonal other
			symbolT = 0;	
			// reset count
			countX[0] = countY[0] = 0;// main
			for( int i = 0; i< 4; i++)
			{
				if( row[i][3-i] == 'X')
				{
					countX[0]++;
				}
				else if(row[i][3-i]== 'O'){
					countY[0]++;
				}
				else if(row[i][3-i]=='T')
				{
					symbolT ++;
				}
				else{
					haveEmpty  = true;
				}
			}
			// check win diagonal
			if((countX[0] == 3 && symbolT == 1) || countX[0] == 4)
			{
				//X win
				out << "Case #" << N <<": X won"<<endl;
				haveWin = true;
			}
			else if((countY[0] == 3 && symbolT == 1) || countY[0] == 4)
			{
				//X win
				out << "Case #" << N <<": O won"<<endl;
				haveWin = true;
			}
		}
		if(!haveWin && haveEmpty){
			out << "Case #" << N <<": Game has not completed"<<endl;
		}
		else if(!haveWin){
			out << "Case #" << N <<": Draw"<<endl;
		}
		
		N++;
		if(N <= T)
		{
			//cin >> row[0]; // empty line
			getline(in, line);
			//cout <<endl;
			//cout << row[0];
		}
	}
	out.close();
	in.close();
	return 0;
}
