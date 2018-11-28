/*
 * cj_qual1.cpp
 *
 *  Created on: 2013-4-13
 *      Author: lenovo
 */
#include <iostream>
#include <fstream>
using namespace std;
int main(void){
	char p[4][4];
	int n,i,j;
	bool all = false;
	int who = 0;
	bool flag = false;
	ofstream SaveFile("out.txt");
	ifstream OpenFile("A-large.in");
	OpenFile>>n;
	//cin>>n;
	for(int cas = 0;cas<n;cas++){
		all = true;
		who = 0;
		flag = false;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				OpenFile>>p[i][j];
				//cin>>p[i][j];
			}
		}
		for(i=0;i<4;i++){
			who = 0;
			for(j=0;j<4;j++){
				if(who == 0 && p[i][j]=='X'){
					who = 1;
				}
				if(who == 0 && p[i][j]=='O'){
					who = 2;
				}
				if((who == 1 && p[i][j] == 'O')||(who == 2 && p[i][j] == 'X')){
					break;
				}
				if(p[i][j]=='.'){
					all = false;
					break;
				}
			}
			if(j==4){
				if(who == 1){
					SaveFile<<"Case #";
					SaveFile<<cas+1<<": X won"<<endl;
					flag = true;
					break;
				}
				if(who == 2){
					SaveFile<<"Case #";
					SaveFile<<cas+1<<": O won"<<endl;
					flag = true;
					break;
				}
			}
		}
		if(flag == true){
			continue;
		}
		for(i=0;i<4;i++){
			who = 0;
			for(j=0;j<4;j++){
				if(who == 0 && p[j][i]=='X'){
					who = 1;
				}
				if(who == 0 && p[j][i]=='O'){
					who = 2;
				}
				if((who == 1 && p[j][i] == 'O')||(who == 2 && p[j][i] == 'X')){
					break;
				}
				if(p[j][i]=='.'){
					all = false;
					break;
				}
			}
			if(j==4){
				if(who == 1){
					SaveFile<<"Case #";
					SaveFile<<cas+1<<": X won"<<endl;
					flag = true;
					break;
				}
				if(who == 2){
					SaveFile<<"Case #";
					SaveFile<<cas+1<<": O won"<<endl;
					flag = true;
					break;
				}
			}
		}
		if(flag == true){
			continue;
		}
		who = 0;
		for(i=0;i<4;i++){
			if(who == 0 && p[i][i]=='X'){
				who = 1;
			}
			if(who == 0 && p[i][i]=='O'){
				who = 2;
			}
			if((who == 1 && p[i][i] == 'O')||(who == 2 && p[i][i] == 'X')){
				break;
			}
			if(p[i][i]=='.'){
				all = false;
				break;
			}
		}
		if(i==4){
			if(who == 1){
				SaveFile<<"Case #";
				SaveFile<<cas+1<<": X won"<<endl;
				continue;
			}
			if(who == 2){
				SaveFile<<"Case #";
				SaveFile<<cas+1<<": O won"<<endl;
				continue;
			}
		}
		who = 0;
		for(i=0;i<4;i++){
			if(who == 0 && p[i][3-i]=='X'){
				who = 1;
			}
			if(who == 0 && p[i][3-i]=='O'){
				who = 2;
			}
			if((who == 1 && p[i][3-i] == 'O')||(who == 2 && p[i][3-i] == 'X')){
				break;
			}
			if(p[i][3-i]=='.'){
				all = false;
				break;
			}
		}
		if(i==4){
			if(who == 1){
				SaveFile<<"Case #";
				SaveFile<<cas+1<<": X won"<<endl;
				continue;
			}
			if(who == 2){
				SaveFile<<"Case #";
				SaveFile<<cas+1<<": O won"<<endl;
				continue;
			}
		}
		if(all == false){
			SaveFile<<"Case #";
			SaveFile<<cas+1<<": Game has not completed"<<endl;
			continue;
		}
		else{
			SaveFile<<"Case #";
			SaveFile<<cas+1<<": Draw"<<endl;
			continue;
		}
	}
	OpenFile.close();
	SaveFile.close();
	return 0;
}

