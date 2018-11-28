#include<iostream>
#include<sstream>
#include<fstream>
using namespace std;

bool match(char c,char player){

	if(c==player || c=='T'){
	
		return true;
	}
	else
		return false;

}
bool checkrow(char x[][5] ,char player){

	for(int i=0;i<4;i++){
		
		if(match(x[i][0],player) && match(x[i][1],player) && match(x[i][2],player) &&match(x[i][3],player)){
			
			return true;
		
		}
	
	}
	return false;

}
bool checkcol(char x[][5],char player){

	for(int i=0;i<4;i++){
		
		if(match(x[0][i],player) && match(x[1][i],player) && match(x[2][i],player) && match(x[3][i],player)){
			
			return true;
		
		}
	
	}
	return false;

}
bool checkdiag1(char x[][5],char player){
	
		if(match(x[0][0],player) && match(x[1][1],player) && match(x[2][2],player) &&match(x[3][3],player)){
			
			return true;
		
		}
	
		return false;
}
bool checkdiag2(char x[][5],char player){
	
		if(match(x[0][3],player) && match(x[1][2],player) &&match(x[2][1],player) &&match(x[3][0],player)){
			
			return true;
		
		}
	return false;

}
bool is_full(char x[][5]){
	
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(x[i][j]=='.'){

				return false;

			}
		
		}
	
	}
	return true;

}
void main(void){
	fstream in,out;
	char tictac [4][5];
	in.open("input.in",ios::in||ios::binary);
	out.open("output.txt",ios::out);
	if(in.fail()){
	cout<<"cannot open file";
	}
	int test_cases=0;
	in>>test_cases;
	char pl1='X';
	char pl2='O';
	bool p1=0,p2=0;
	for(int i=0;i<test_cases;i++){
		for(int j=0;j<4;j++){
			in>>tictac[j];
		}

		p1=checkrow(tictac,pl1) || checkcol(tictac,pl1) || checkdiag1(tictac,pl1) || checkdiag2(tictac,pl1);
		if(!p1){
		p2=checkrow(tictac,pl2) || checkcol(tictac,pl2) || checkdiag1(tictac,pl2) || checkdiag2(tictac,pl2);
		}
		if(p1){
			
			out<<"Case #"<<i+1<<": X won"<<endl;
		
		}
	    else if(p2){

			out<<"Case #"<<i+1<<": O won"<<endl;
		
		}
		else if(!p1 && !p2 && !is_full(tictac)){
		
			out<<"Case #"<<i+1<<": Game has not completed"<<endl;
		}
		else{
		
			out<<"Case #"<<i+1<<": Draw"<<endl;
		}


	}
	out.close();
	in.close();

}

