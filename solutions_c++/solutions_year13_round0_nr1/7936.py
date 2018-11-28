#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>
using namespace std;


 int main(int argc, char *argv[]) {
 	//for all start
	ofstream outputfile;
 	ifstream inputfile;
 	inputfile.open(argv[1], ios::in);
	outputfile.open("c.out", ios::out);
	int numcases = 0;
	inputfile >> numcases; // case count - line 1
	//for all end
	for(int i = 0; i < numcases; i++)
	{
		int count = 0;
		bool xwin = false;
		bool owin = false;
		char board[4][4]; // board[x][y]
		for(int j = 0; j < 4; j++)
		{		
		for(int i = 0; i <4; i++)
		{inputfile >> board[j][i];}
		}
		//xwin accross
		for(int u = 0; u <4;u++)
		{
			for(int v = 0; v <4;v++){if(board[v][u] == 'X' || board[v][u] == 'T'){count=count+1;;}}
			if(count == 4){xwin = true;}
		count = 0;
		}
		//xwin upie downie
		for(int u = 0; u <4;u++)
		{
			for(int v = 0; v <4;v++){if(board[u][v] == 'X' || board[u][v] == 'T'){count=count+1;;}}
			if(count == 4){xwin = true;}
		count = 0;
		}
		//owin accross
		for(int u = 0; u <4;u++)
		{
			for(int v = 0; v <4;v++)
			{
			if(board[v][u] == 'O' || board[v][u] == 'T')
			{count=count+1;}
			}
			if(count == 4){owin = true;}
		count = 0;
		}
		//owin upie downie
		for(int u = 0; u <4;u++)
		{
			for(int v = 0; v <4;v++)
			{
			if(board[u][v] == 'O' || board[u][v] == 'T')
			{count=count+1;}
			}
			if(count == 4){owin = true;}
		count = 0;
		}
		//owin diags left top to right bottom
		for(int u = 0; u <4;u++)
		{	
			if(board[u][u] == 'O' || board[u][u] == 'T'){count=count+1;}
			if(count == 4){owin = true;}
		}
			count = 0;
		//owin diags left bottom to right top
		for(int u = 0; u <4;u++)
		{	
			if(board[u][4-u-1] == 'O' || board[u][4-u-1] == 'T'){count=count+1;}
			if(count == 4){owin = true;}
		}
			count = 0;
		
		if(xwin == true && owin == true){outputfile << "Case #" << i+1 << ": Draw";
		}else{
		if(xwin == true){outputfile << "Case #" << i+1 << ": X won";}else{
		if(owin == true){outputfile << "Case #" << i+1 << ": O won";}}}
		//not complete to be added
		bool incomplete = false;
		for(int u = 0; u <4;u++){for(int v = 0; v <4;v++){if(board[v][u] == '.'){incomplete = true;}}}
		if(xwin == false && owin == false && incomplete == true){outputfile << "Case #" << i+1 << ": Game has not completed";}
		if(xwin == false && owin == false && incomplete == false){outputfile << "Case #" << i+1 << ": Draw";}
		outputfile << "\n";

	}
	
outputfile.close();
inputfile.close();
	return 0;
}

