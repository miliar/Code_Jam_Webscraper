// google_jam_0.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <fstream>

using namespace std; 

string getResult(string strXO, string total, int first);

int _tmain(int argc, _TCHAR* argv[])
{
	int i = 0, j = 0;
	string board[4];
	int t = 0;
	string total = "";

	for (i=0;i<4;i++)
		board[i] = "....";

	ifstream fin("A-large.txt");	
	fin >> t;
	string strT = "T";
	string strXO = "";
	string result = "";
	
	ofstream fout("result_large.txt");
	

	int case_num = 0;
	while (case_num < t){
		i = 0;
		total = "";
		while (i<4){
			fin >> board[i];
			if (board[i].size() != 4){
				fout << "error input" << endl;
				fin >> board[i];
			}
			total += board[i];
			i++;
		}

		int first = total.find_first_of(strT);

		strXO = "X";
		result = getResult(strXO, total, first);

		if (result == "nE"){
			strXO = "O";
			result = getResult(strXO, total, first);

			if (result == "nE")
				result = "Draw";
		}

		else if (result == "yE"){
			strXO = "O";
			result = getResult(strXO, total, first);

			if (result == "yE")
				result = "Game has not completed";		
		}

		fout << "Case #" << case_num + 1 << ": " << result << endl;
		case_num++;
	}

	fout << flush; 
	fout.close();
	system ("pause");
	return 0;
}

string getResult(string strXO, string total, int first){
	int count_row = 0, count_col = 0, count_dig1 = 0, count_dig2 = 0;
	string result = "";
	char flag = strXO[0];
	string strBlk = ".";

	if(first != string::npos)
		total.replace(first, 1, strXO);
	
	//check row and col
	for (int i=0; i<4; i++){
		count_row = 0;
		count_col = 0;
		for (int j=0; j<4; j++){
			if (total[j + 4*i] == flag)
				count_row++;
			if (total[i + 4*j] == flag)
				count_col++;
		}

		if ((count_row == 4) || (count_col == 4))
		{
			result = strXO + " won";
			return result;
		}
	}

	//check diagonal
	//flag = total[0];
	for (int i = 0; i<4; i++){
		if (total[5*i] == flag)
			count_dig1++;
	}
	if (count_dig1 == 4){
		result = strXO + " won";
		return result;
	}

	//check another diagonal
	//flag = total[3];
	for (int i = 0; i<4; i++){
		if (total[3*(i+1)] == flag)
			count_dig2++;
	}
	if (count_dig2 == 4){
		result = strXO + " won";
		return result;
	}

	int empty = total.find_first_of(strBlk);

	if(empty == string::npos){
		result = "nE";
		return result;
	}
	else{
		result = "yE";
		return result;
	}
	
}
