#include <iostream>
#include <cmath>
#include <string>
#include <vector>
#include <fstream>
#include <iomanip>
#include <algorithm>
using namespace std;
int t;
bool check, ch;
char mas [4][4],c;
int main(){
	ifstream cin("A-large.in");
	ofstream cout("outt1.txt");
	cin>>t;
	for(int r = 1; r <= t; r++){
		check=false;
		for(int i=0; i<4; i++){
			for(int j = 0; j<4; j++){
				cin>>mas[i][j];
				if(mas[i][j]=='.')check = true;
			}
		}
		ch = false;
		bool we = false;
		for(int i = 0; i < 4; i++){
			if(mas[i][i] != 'X' && mas[i][i] != 'T'){
				ch=true;
			}
			if(mas[i][i] != 'O' && mas[i][i] != 'T'){
				we=true;
			}
		}
		if(!ch){cout<<"Case #"<<r<<": X won"<<endl; continue; }
		if(!we){cout<<"Case #"<<r<<": O won"<<endl; continue; }
		ch=false;
		we = false;
		for(int i = 0; i<4; i++){
			if(mas[i][3-i] != 'X' && mas[i][3-i] != 'T'){
				ch=true;
			}
			if(mas[i][3-i] != 'O' && mas[i][3-i] != 'T'){
				we=true;
			}
		}
		if(!ch){cout<<"Case #"<<r<<": X won"<<endl; continue; }
		if(!we){cout<<"Case #"<<r<<": O won"<<endl; continue; }
		//...
		ch= false;
		for(int i = 0; i < 4; i++){
			bool e = true;
			for(int j=0; j<4; j++){
				if(mas[i][j] !='X' && mas[i][j] != 'T') e = false;
			}
			if(e){
				cout<<"Case #"<<r<<": X won"<<endl;
				ch = true;
				break;
			}else e = true;
			for(int j = 0; j < 4; j++){
				if(mas[i][j] !='O' && mas[i][j] != 'T') e = false;
			}
			if(e){
				cout<<"Case #"<<r<<": O won"<<endl;
				ch=true;
				break;
			}else e=true;
			for(int j = 0; j < 4; j++){
				if(mas[j][i] !='O' && mas[j][i] != 'T') e = false;
			}
			if(e){
				cout<<"Case #"<<r<<": O won"<<endl;
				ch = true;
				break;
			}else e=true;
			for(int j = 0; j < 4; j++){
				if(mas[j][i] !='X' && mas[j][i] != 'T') e = false;
			}
			if(e){
				cout<<"Case #"<<r<<": X won"<<endl;
				ch = true;
				break;
			}else e = true;
		}
		if(ch){ ch = false; continue; }
		if(check){ cout<<"Case #"<<r<<": Game has not completed"<<endl;}
		else cout<<"Case #"<<r<<": Draw"<<endl;
	}

	return 0;
}
