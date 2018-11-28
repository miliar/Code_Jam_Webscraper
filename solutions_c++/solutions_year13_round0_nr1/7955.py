#include <iostream>
using namespace std;

int main(){
	int T;
	char board[4][4];
	cin>>T;
	for (int c = 0; c <T;c++){
	int x_axis, y_axis;
	bool empty=false;
	for (int i = 0; i<4 ; i++){
		for (int j = 0; j<4;j++){
			cin >> board[i][j];
			if (board[i][j]=='T'){ x_axis=i; y_axis=j;}
			if (board[i][j]=='.'){empty = true;}
			
		}
	}
	
	cout<<"Case #"<<c+1<<": ";
	int line=0;
	int row=0;
	int left=0;
	int right=0;
	for (int i = 0; i<4; i++){
		line=0;
		row =0;
		for ( int j=0; j<4; j++){
			if (board[i][0]!='T'){
				if ((board[i][j] == board[i][0] || board[i][j] =='T')&&board[i][0]!='.'){
					line++;				
					continue;}
				else{break;}
			}
			else{
				if ((board[i][j] == board[3-i][0] || board[i][j] =='T')&&board[i][0]!='.'){
					line++;				
					continue;}
				else{break;}
			}
		}
		for (int j=0;j<4; j++){
			if (board[0][i]!='T'){
				if ((board[j][i] == board[0][i] || board[j][i] == 'T')&&board[0][i]!='.'){
					row++;
					continue;}
				else{break;}
			}
			else{
				if ((board[j][i] == board[0][3-i] || board[j][i] =='T')&&board[0][i]!='.'){
					line++;				
					continue;}
				else{break;}
			}
		}
		if (board[0][0]!='T'){
			if ((board[i][i] == board[0][0] || board[i][i] == 'T')&&board[0][0]!='.'){
				left++;}
		}
		else{
			if ((board[i][i] == board[3][3] || board[i][i] == 'T')&&board[0][0]!='.'){
				left++;}
		}
		if (board[0][3]!='T'){
			if ((board[i][3-i] == board[0][3] || board[i][3-i] == 'T')&&board[0][3]!='.'){
				right++;}
			}
		else{
			if ((board[i][3-i] == board[3][0] || board[i][3-i] == 'T')&&board[0][3]!='.'){
				right++;}
			}
		if (line == 4){if (board[i][0]!='T'){cout<<board[i][0]<<" won"<<endl; break;}
				else{cout<<board[3-i][0]<<" won"<<endl; break;}}
		if (row == 4){if (board[0][i]!='T'){cout<<board[0][i]<<" won"<<endl;break;}
				else{cout<<board[0][3-i]<<" won"<<endl; break;}}
		}
		if (line == 4){continue;}
		else if (row == 4){continue;}
		if (left == 4){	if (board[0][0]!='T'){cout<<board[0][0]<<" won"<<endl;}
				else{cout<<board[3][3]<<" won"<<endl;}}
		else if (right == 4){ if (board[0][3]!='T'){cout<<board[0][3]<<" won"<<endl;}
				else{cout<<board[3][0]<<" won"<<endl;}}
		else {
			if (empty){cout<<"Game has not completed"<<endl;}
			else{cout<<"Draw"<<endl;}
		}
	}
}
		

