#include<iostream>
#include<string>
#include<fstream>
using namespace std;
	
void main()
{   fstream a;
	a.open("C:\\w.in",ios::in||ios::out);
	char ch;
	
	int n;
	a>>n;
	char *result=new char[n];
	char **b=new char*[n];
	for(int i=0;i<n;i++){
		b[i]=new char[16];
	}
	for(int i=0;i<n;i++){
		for(int j=0;j<16;j++){
			a>>ch;
			cout<<ch;
			b[i][j]=ch;
		}cout<<endl;
	}
	for(int i=0;i<n;i++){
		int ifT=0;
		int isWin=0,isDraw=1;
		
		cout<<"+"<<i<<endl;
		
			
		for(int j=0;j<4;j++){
			if(isWin==1) {break;}
			int ifx=0,ifo=0,ift=0;
			cout<<"toOne"<<"*";
			for(int q=0;q<4;q++){
				
				
				if(b[i][q+j*4]=='X'){
					ifx++;cout<<"to3"<<"*";
				}
				else if(b[i][q+j*4]=='O'){
					ifo++;cout<<"to4"<<"*";
				}
				else if(b[i][q+j*4]=='T'){
					ift=1;cout<<"to5"<<"*";
				}
				else if(b[i][q+j*4]=='.'){
					isDraw=0;cout<<"t6"<<"*";
				
				}}if(ifx==4||(ifx==3&&ift==1)){
					result[i]='X';cout<<"to1"<<"*";
					isWin=1;
					break;
				}
				else if(ifo==4||(ifo==3&&ift==1)){
					result[i]='O';cout<<"to2"<<"*";
					isWin=1;
					break;
				}
		}
		if(isWin==0){cout<<"to7"<<"*";
			for(int j=0;j<4;j++){
			if(isWin==1) {break;}
			int ifx=0,ifo=0,ift=0;
			for(int q=0;q<4;q++){
				
				
				if(b[i][j+q*4]=='X'){
					ifx++;cout<<"to10"<<"*";
				}
				else if(b[i][j+q*4]=='O'){
					ifo++;cout<<"to11"<<"*";
				}
				else if(b[i][j+q*4]=='T'){
					ift=1;cout<<"to12"<<"*";
				}
				else if(b[i][j+q*4]=='.'){
					isDraw=0;cout<<"to13"<<"*";
				}
				}if(ifx==4||(ifx==3&&ift==1)){
					result[i]='X';cout<<"to8"<<"*";
					isWin=1;
					break;
				}
				else if(ifo==4||(ifo==3&&ift==1)){
					result[i]='O';
					isWin=1;cout<<"to9"<<"*";
					break;
				}
		}
			if(isWin==0){cout<<"to14"<<"*";
				int ifx=0,ifo=0,ift=0;
				for(int q=0;q<4;q++){
					
				cout<<"to17"<<"*";
				if(b[i][5*q]=='X'){
					ifx++;cout<<"to18"<<"*";
				}
				else if(b[i][5*q]=='O'){
					ifo++;cout<<"to19"<<"*";
				}
				else if(b[i][5*q]=='T'){
					ift=1;cout<<"to20"<<"*";
				}
				else if(b[i][5*q]=='.'){
					isDraw=0;cout<<"to21"<<"*";
				}
				}
			    if(ifx==4||(ifx==3&&ift==1)){
					result[i]='X';cout<<"to15"<<"*";
					isWin=1;
					
				}
				else if(ifo==4||(ifo==3&&ift==1)){
					result[i]='O';cout<<"to16"<<"*";
					isWin=1;
					
				}
				if(isWin==0){cout<<"to22"<<"*";
					int ifx=0,ifo=0,ift=0;
				for(int q=1;q<=4;q++){
					
				cout<<"to25"<<"*";
				if(b[i][3*q]=='X'){
					ifx++;cout<<"to26"<<"*";
				}
				else if(b[i][3*q]=='O'){
					ifo++;cout<<"to27"<<"*";
				}
				else if(b[i][3*q]=='T'){
					ift=1;cout<<"to28"<<"*";
				}
				else if(b[i][q*3]=='.'){
					isDraw=0;cout<<"to29"<<"*";
				}
				}if(ifx==4||(ifx==3&&ift==1)){
					result[i]='X';cout<<"to23"<<"*";
					isWin=1;
					
				}
				else if(ifo==4||(ifo==3&&ift==1)){
					result[i]='O';cout<<"to24"<<"*";
					isWin=1;
					
				}
				}
		
				
		}}

			if(isWin==0){cout<<"to30"<<"*";
				if(isDraw==1){
					result[i]='d';cout<<"to31"<<"*";
				}
				else result[i]='n';
			}
}
			a.close();
			a.open("C:\\output.txt");
			
			for(int i=0;i<n;i++){
				a<<"Case #"<<i+1<<":";
				//cout<<result[i]<<endl;
				if(result[i]=='X') a<<" X WON"<<endl;
				else if(result[i]=='O') a<<" O WON"<<endl;
				else if(result[i]=='d') a<<" Draw"<<endl;
				else if(result[i]=='n') a<<" Game has not completed"<<endl;
			}
			a.close( );
}