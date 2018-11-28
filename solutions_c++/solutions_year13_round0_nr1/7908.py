#include <iostream>
#include <string>
using namespace std;
string S[4];
int nX;int nO; int nT;bool bx;bool bo;
void inp(){
	for(int i=0;i<4;i++)getline(cin,S[i]);
}
void outp(int a, int c){
	switch(c){
		case 1: cout << "Case #"<<a<<": X won"<<endl;break;
		case 2: cout << "Case #"<<a<<": O won"<<endl;break;
		case 3: cout << "Case #"<<a<<": Draw"<<endl;break;
		case 4: cout << "Case #"<<a<<": Game has not completed"<<endl;break;
	}
}
void check(){
	if((nX==4) || ((nX==3)&&(nT==1)))bx = true;
	if((nO==4) || ((nO==3)&&(nT==1)))bo = true;
	nX = 0; nO = 0; nT = 0;
}
void add(int i, int j){
	if(S[i][j]=='X') nX++;
	if(S[i][j]=='O') nO++;
	if(S[i][j]=='T') nT++;
}
void alg(int test){
	nX=0;nO=0;nT=0;bx=false;bo=false;
	//Filas
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++) add(i,j);
		check();
	}//Columnas
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++) add(j,i);
		check();
	}//Diagonales
	for(int i=0;i<4;i++) add(i,i);
	check();
	for(int i=0;i<4;i++) add(i,3-i);
	check();
	bool fill = true;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(S[i][j]=='.'){
				fill = false; break;
			}
		}
	}
	if((bx == true)&&(bo == false)) outp(test, 1);
	if((bx == false)&&(bo == true)) outp(test, 2);
	if((bx == true)&&(bo == true)) outp(test, 3);
	if((bx == false)&&(bo == false)&&( fill == true)) outp(test, 3);
	if((bx == false)&&(bo == false)&&(fill == false)) outp(test, 4);
}
int main(){
	int n;
	while(cin>>n){
		string tmp; getline(cin,tmp);
		for(int i = 0; i < n; i++){
			if(i!=(n-1)){
				inp();
				string tmp; getline(cin,tmp);
				alg(i+1);
			}else{
				inp();
				alg(i+1);
			}
		}
	}
	return 0;
}
