#include "competitive.h"

int main(){
	int T;
	char a[4][4];
	char b[4][4];
	bool flag;
	cin>>T;
	for(int i = 1;i<=T;i++){
		int j;
		flag = false;
		for(j=0;j<4;j++)
			for(int k=0;k<4;k++){
				cin>>a[j][k]; 
				b[j][k]=a[j][k]; 
				if(a[j][k]=='.') flag=true;
				if(a[j][k]=='T') {a[j][k]='X'; b[j][k]='O';}
			}
					
		for(j =0;j<4;j++){
			if(
			(a[0][j]=='X' &&a[1][j]=='X' && a[2][j]=='X' && a[3][j]=='X')
			||
			(a[0][j]=='X' &&a[j][1]=='X' && a[j][2]=='X' && a[j][3]=='X')
			)
			{cout<<"Case #"<<i<<": X won\n"; break;}
		}
		if(j<4) continue;

		for(j =0;j<4;j++){
			if(
			(b[0][j]=='O' &&b[1][j]=='O' && b[2][j]=='O' && b[3][j]=='O')
			||
			(b[0][j]=='O' &&b[j][1]=='O' && b[j][2]=='O' && b[j][3]=='O')
			)
			{cout<<"Case #"<<i<<": O won\n"; break;}
		}
		if(j<4) continue;
		
			if(
			(a[0][0]=='X' &&a[1][1]=='X' && a[2][2]=='X' && a[3][3]=='X')
			||
			(a[0][3]=='X' &&a[1][2]=='X' && a[2][1]=='X' && a[3][0]=='X')
			)
			{cout<<"Case #"<<i<<": X won\n"; continue;}
			
			if(
			(b[0][0]=='O' &&b[1][1]=='O' && b[2][2]=='O' && b[3][3]=='O')
			||
			(b[0][3]=='O' &&b[1][2]=='O' && b[2][1]=='O' && b[3][0]=='O')
			)
			{cout<<"Case #"<<i<<": O won\n"; continue;}
		
		
		if(flag) cout<<"Case #"<<i<<": Game has not completed\n";
		else
		cout<<"Case #"<<i<<": Draw\n";

		
		}
		
	
	return 0;
}
