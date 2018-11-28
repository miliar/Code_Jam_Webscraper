// Hedgemony.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include<vector>
#include<iostream>
#include<string>

using namespace std;

int func(vector<vector<char> > &bush,char chr){
	int succ = 1;
	for(int i = 0 ; i < 4 ; i++)
		{
			succ =1;
			for(int j =0 ; j < 4 ; j++)
			{
				if(bush[i][j] == chr || bush[i][j] == '.'){
					succ = 0;
					break;
				}
			}
			if(succ==1){
				return 1;
			}
		}
		
		for(int i = 0 ; i < 4 ; i++)
		{
			succ = 1;
			for(int j =0 ; j < 4 ; j++)
			{
				if(bush[j][i] == chr || bush[j][i] == '.'){
					succ = 0;
					break;
				}
			}
			if(succ==1){
				return 1;
			}
		}
		
		succ = 1;
		for(int i = 0 ; i < 4 ; i++)
		{
			if(bush[i][i] == chr || bush[i][i] == '.'){
				succ = 0;
				break;
			}
		}
		if(succ==1){
				return 1;
			}

		succ = 1;
		for(int i = 3 ; i >= 0 ; i--)
		{
			if(bush[i][3-i] == chr || bush[i][3-i] == '.'){
				succ = 0;
				break;
			}
		}
		if(succ==1){
				return 1;
			}
	return 0;
}

int _tmain(int argc, _TCHAR* argv[])
{
	int T,t=0;
	cin >> T;
	vector<char> output(T);
	while(t<T){
		string str;
		int open = 0;
		int succ = 0;
		vector<vector<char> > bush(4,vector<char>(4,'.'));
		for(int i = 0 ; i < 4 ; i++)
		{
			cin >> str;
			for(int j =0 ; j < 4 ; j++)
			{
				bush[i][j] = str[j];
				if(str[j] == '.'){
					open = 1;
				}
			}
		}
		
		succ = func(bush,'O');
		if(succ == 1){
			output[t] = 'X';
			t++;
			continue;
		}
		succ = func(bush,'X');
		if(succ == 1){
			output[t] = 'O';
			t++;
			continue;
		}
		if(succ == 0){
			if(open == 1){
				output[t] = 'G';
			}else{
				output[t] = 'D';
			}
		}

		t++;
	}
	for(int i = 0; i < T ; i++){
		cout << "Case #" << i+1 << ": ";
		if(output[i] == 'X'){
			cout << "X won";
		}
		else if(output[i] == 'O'){
			cout << "O won";
		}
		else if(output[i] == 'D'){
			cout << "Draw";
		}
		else{
			 cout << "Game has not completed";
		}
			cout << endl;
	}
	return 0;
}

