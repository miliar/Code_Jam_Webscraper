#include<iostream>
#include<fstream>
using namespace std;
ifstream in("A-small-attempt5.in");
ofstream out("google.txt");
int  check(char a[4][4],int n);
int main(){

	int n;
	in>>n;
	char a[4][4];
	for(int i=0;i<n;i++){
		
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				in>>a[j][k];
		}
	}
	
		check(a,i+1);
	}
}

int check(char a[4][4],int n){
		for(int i=0;i<4;i++){
			if( (a[i][0]==a[i][1] && a[i][1]==a[i][2] && a[i][3]=='T' && a[i][0]!='.') ||
			 	(a[i][0]==a[i][1] && a[i][1]==a[i][2] &&a[i][2]==a[i][3] &&  a[i][0]!='.')||
			 	(a[i][0]=='T' && a[i][1]==a[i][2] && a[i][3]==a[i][1] && a[i][1]!='.')
			  )
			 {
				out<<"Case #"<<n<<": "<< a[i][1]<<" won\n";
				return 0;
			}
		}
		
		for(int i=0;i<4;i++){
			if( (a[0][i]==a[1][i] && a[1][i]==a[2][i] && a[3][i]=='T' && a[0][i]!='.') || 
				(a[0][i]==a[1][i] && a[1][i]==a[2][i] && a[2][i]==a[3][i] &&  a[0][i]!='.')||
				(a[0][i]=='T' && a[1][i]==a[2][i] && a[3][i]==a[1][i] && a[1][i]!='.')){
				out<<"Case #"<<n<<": "<< a[1][i]<<" won\n";
				return 0;
			}
		}
		
	
		if((a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[3][3]=='T' && a[1][1]!='.') || 
		(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[2][2]==a[3][3] && a[1][1]!='.') ||
		(a[0][0]=='T' && a[1][1]==a[2][2] && a[3][3]==a[1][1] && a[1][1]!='.') ){
				out<<"Case #"<<n<<": "<< a[1][1]<<" won\n";
				return 0;
			
		}
		
		if((a[0][3]==a[1][2] && a[1][2]==a[2][1] && a[3][0]=='T' && a[0][3]!='.') || 
		(a[0][3]==a[1][2] && a[1][2]==a[2][1] && a[2][1]==a[3][0] && a[0][3]!='.') ||
		(a[0][3]=='T' && a[1][2]==a[2][1] && a[3][0]==a[1][2] && a[0][3]!='.') ){
				out<<"Case #"<<n<<": "<< a[1][2]<<" won\n";
				return 0;
			
		}
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(a[i][j]=='.'){
					out<<"Case #"<<n<<": Game has not completed\n";
						return 0;
				}
		}
		}
		
			out<<"Case #"<<n<<": Draw\n"; 
	
}
