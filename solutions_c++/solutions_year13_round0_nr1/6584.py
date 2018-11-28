// googlecj2013a.cpp : 定義主控台應用程式的進入點。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

bool compare(char &a, char &b)
{
	if(a=='.'||b=='.')return 0;
	else if(a==b)return 1;
	else if(a=='T'||b=='T')return 1;
	else return 0;
}
int _tmain(int argc, _TCHAR* argv[])
{
	ifstream fin( "c:\\tinput.txt" );
	ofstream fout( "c:\\output.txt" , ios_base::in || ios_base::trunc);
	string temp1, temp2;
	istringstream stream1;
	string temp;
	fin>>temp;
	int times=0;
	stream1.str(temp);
	stream1>>times;
	cout<<times<<endl;
	string stc;
	getline(fin, stc);//clear fisrt line
	string board[4];
	for(int n=0; n<times; ++n)
	{		
		getline(fin, board[0]);
		getline(fin, board[1]);
		getline(fin, board[2]);
		getline(fin, board[3]);
		getline(fin, stc);
		int state=0;
		char *won;
		if(compare(board[0][0],board[0][1])
			&&compare(board[0][0],board[0][2])
			&&compare(board[0][0],board[0][3])
			&&compare(board[0][1],board[0][2])
			&&compare(board[0][1],board[0][3])
			&&compare(board[0][2],board[0][3])){state=1;if(board[0][0]=='T')won=&board[0][1];else won=&board[0][0];}
		else if(compare(board[1][0],board[1][1])
			&&compare(board[1][0],board[1][2])
			&&compare(board[1][0],board[1][3])
			&&compare(board[1][1],board[1][2])
			&&compare(board[1][1],board[1][3])
			&&compare(board[1][2],board[1][3])){state=1;if(board[1][0]=='T')won=&board[1][1];else won=&board[1][0];}
		else if(compare(board[2][0],board[2][1])
			&&compare(board[2][0],board[2][2])
			&&compare(board[2][0],board[2][3])
			&&compare(board[2][1],board[2][2])
			&&compare(board[2][1],board[2][3])
			&&compare(board[2][2],board[2][3])){state=1;if(board[2][0]=='T')won=&board[2][1];else won=&board[2][0];}
		else if(compare(board[3][0],board[3][1])
			&&compare(board[3][0],board[3][2])
			&&compare(board[3][0],board[3][3])
			&&compare(board[3][1],board[3][2])
			&&compare(board[3][1],board[3][3])
			&&compare(board[3][2],board[3][3])){state=1;if(board[3][0]=='T')won=&board[3][1];else won=&board[3][0];}
		//end of horizon

		else if(compare(board[0][0],board[1][0])
			&&compare(board[0][0],board[2][0])
			&&compare(board[0][0],board[3][0])
			&&compare(board[1][0],board[2][0])
			&&compare(board[1][0],board[3][0])
			&&compare(board[2][0],board[3][0])){state=1;if(board[0][0]=='T')won=&board[1][0];else won=&board[0][0];}
		else if(compare(board[0][1],board[1][1])
			&&compare(board[0][1],board[2][1])
			&&compare(board[0][1],board[3][1])
			&&compare(board[1][1],board[2][1])
			&&compare(board[1][1],board[3][1])
			&&compare(board[2][1],board[3][1])){state=1;if(board[0][1]=='T')won=&board[1][1];else won=&board[0][1];}
		else if(compare(board[0][2],board[1][2])
			&&compare(board[0][2],board[2][2])
			&&compare(board[0][2],board[3][2])
			&&compare(board[1][2],board[2][2])
			&&compare(board[1][2],board[3][2])
			&&compare(board[2][2],board[3][2])){state=1;if(board[0][2]=='T')won=&board[1][2];else won=&board[0][2];}
		else if(compare(board[0][3],board[1][3])
			&&compare(board[0][3],board[2][3])
			&&compare(board[0][3],board[3][3])
			&&compare(board[1][3],board[2][3])
			&&compare(board[1][3],board[3][3])
			&&compare(board[2][3],board[3][3])){state=1;if(board[0][3]=='T')won=&board[1][3];else won=&board[0][3];}
		//end of vertical
		else if(compare(board[0][0],board[1][1])
			&&compare(board[0][0],board[2][2])
			&&compare(board[0][0],board[3][3])
			&&compare(board[1][1],board[2][2])
			&&compare(board[1][1],board[3][3])
			&&compare(board[2][2],board[3][3])){state=1;if(board[0][0]=='T')won=&board[1][1];else won=&board[0][0];}
		else if(compare(board[0][3],board[1][2])
			&&compare(board[0][3],board[2][1])
			&&compare(board[0][3],board[3][0])
			&&compare(board[1][2],board[2][1])
			&&compare(board[1][2],board[3][0])
			&&compare(board[2][1],board[3][0])){state=1;if(board[0][3]=='T')won=&board[1][2];else won=&board[0][3];}
		//end of skew
		else
			for(int k=0; k<4; ++k)
				for(int l=0; l<4; ++l)
					if(board[k][l]=='.') state=2;

		if(state==0)
			state=3;
		switch(state)
		{
			case 1:
				fout<<"Case #"<<n+1<<": "<<*won<<" won"<<endl;
				break;
			case 2:
				fout<<"Case #"<<n+1<<": Game has not completed"<<endl;
				break;
			case 3:
				fout<<"Case #"<<n+1<<": Draw"<<endl;
				break;
			default:
				;
		};
		//if(n<times)
		//	fout<<"Case #"<<n+1<<": "<<stc<<endl;
	}
	system("pause");
	return 0;
}