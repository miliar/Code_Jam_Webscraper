#include<stdio.h>
#include<conio.h>

char board[4][4];//array to hold the characters
int win=0;//win status
FILE *f;//file pointer for output file

//checkDot is used to locate any dot in the board .if one found then it returns 1.
	int checkDot(){
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(board[i][j]=='.'){return 1;}
			}
		} 
		return 0;
	}
//to check the charaters horizontaly
	int horizontal(int i,int j,char ch){	
		if(ch!='.'&&board[i][j]==ch&&board[i][j+1]==ch&&board[i][j+2]==ch&&(board[i][j+3]==ch||board[i][j+3]=='T')){
			win=1;return 1;
		}
		else{win=0;return 0;}
	}
	
//to check the charaters verticaly	
	int vertical(int i,int j,char ch){
		if(ch!='.'&&board[i][j]==ch&&board[i+1][j]==ch&&board[i+2][j]==ch&&(board[i+3][j]==ch||board[i+3][j]=='T')){
			win=1;return 1;
		}
		else{win=0;return 0;}
	}
	
//to check the charaters diagonaly
//mode is used to indicate diagonal direction ,-1 is left to right and 1 is for right to left.
	int diagonal(int i,int j,char ch,int mode){
		int tmp=(-1*mode);
		if(ch!='.'&&board[i][j]==ch&&board[i+1][j+1*tmp]==ch&&board[i+2][j+2*tmp]==ch&&(board[i+3][j+3*tmp]==ch||board[i+3][j+3*tmp]=='T')){
			win=1;return 1;
		}
		else{win=0;return 0;}
	}
	
//it checks the status of case and give the outputs.
	void CheckCase(int Cnum){
		char current;//too hold current character
		
		for(int l=0;l<4;l++){
			for(int m=0;m<4;m++){	
				current=board[l][m];		
				
				if(l==0&&m==0){
					if(horizontal(0,0,current)){break;}//if win status is true then break from inner loop.
					if(vertical(0,0,current)){break;}
					if(diagonal(0,0,current,-1)){break;}
				}
				else if(l==0&&m==3){
					if(vertical(0,3,current)){break;}
					if(diagonal(0,3,current,1)){break;}
				}
				else if(l==0){
					if(vertical(0,m,current)){break;}
				}
				else if(m==0){
					if(horizontal(l,m,current)){break;}
				}
			
			}
			if(win){break;}//if win status is true then break from outer loop.
		}
		
		
		if(win){
			fprintf(f,"Case #%d: %c won\n",Cnum,current);	
		}
		else if(checkDot()){
			fprintf(f,"Case #%d: Game has not completed\n",Cnum);
		}
		else{
			fprintf(f,"Case #%d: Draw\n",Cnum);
		}
	}


int main(){
	FILE *file;
	file=fopen("A-small-attempt0.in","r+");
	f=fopen("output.txt","w+");
	char ch;
	int Case=1;
	int NumOfCases=0;//number of cases
	
	ch=fgetc(file);
	while(ch!='\n'){	
		NumOfCases=NumOfCases*10+(ch-'0');	
		ch=fgetc(file);
	}
	for(int k=1;k<=NumOfCases;k++){
		ch=fgetc(file);
		if(ch=='\n'){ch=fgetc(file);}	
		
			for(int i=0;i<4;i++){
				for(int j=0;j<4;j++){
					board[i][j]=ch;
					ch=fgetc(file);	
				}
				ch=fgetc(file);
			}
		CheckCase(k);
		
	}
	return 0;
}
