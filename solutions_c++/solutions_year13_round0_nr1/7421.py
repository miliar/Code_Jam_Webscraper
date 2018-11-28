#include <iostream>
#include <vector>
using namespace std;

void check_game_state(vector<string> b,int testcase) {
	char symbol='*';
	char t='T';
	int a[1][2];
	int total=0;
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(b[i][j]==t){
				total=1;
				a[0][0]=i;
				a[0][1]=j;
				b[i][j]='X';
				break;
			}
		}
	}
	
		
	//check row
	for(int i=0;i<4;i++){
		if((b[i][0]==b[i][1]) && (b[i][1]==b[i][2]) && (b[i][2]==b[i][3]) && (b[i][0]!='.')){
			symbol = b[i][0];
			break;
		}
	}
	//check column
	for(int i=0;i<4;i++){
		if((b[0][i]==b[1][i]) && (b[1][i]==b[2][i]) && (b[2][i]==b[3][i]) && (b[0][i]!='.')){
			symbol = b[0][i];
			break;
		}
	}
	//check diagonal
	if((b[0][0]==b[1][1]) && (b[1][1]==b[2][2]) && (b[2][2]==b[3][3]) && (b[1][1]!='.')){
		symbol = b[1][1];
	}
	if((b[0][3]==b[1][2]) && (b[1][2]==b[2][1]) && (b[2][1]==b[3][0]) && (b[0][3]!='.')){
		symbol=b[0][3];
	}
	
	if((symbol=='*')&&(total==1)){
		b[a[0][0]][a[0][1]] = 'O';
		//check row
		for(int i=0;i<4;i++){
			if((b[i][0]==b[i][1]) && (b[i][1]==b[i][2]) && (b[i][2]==b[i][3]) && (b[i][0]!='.')){
				symbol = b[i][0];
				break;
			}
		}
		//check column
		for(int i=0;i<4;i++){
			if((b[0][i]==b[1][i]) && (b[1][i]==b[2][i]) && (b[2][i]==b[3][i]) && (b[0][i]!='.')){
				symbol = b[0][i];
				break;
			}
		}
		//check diagonal
		if((b[0][0]==b[1][1]) && (b[1][1]==b[2][2]) && (b[2][2]==b[3][3]) && (b[1][1]!='.')){
			symbol = b[1][1];
		}
		if((b[0][3]==b[1][2]) && (b[1][2]==b[2][1]) && (b[2][1]==b[3][0]) && (b[0][3]!='.')){
			symbol=b[0][3];
		}		
	}
	if(symbol!='*'){
		if(symbol=='X'){
			cout<<"Case #"<<testcase<<": X won"<<endl;
		}
		else if(symbol=='O'){
			cout<<"Case #"<<testcase<<": O won"<<endl;
		}
	}
	else{
		int draw=1;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(b[i][j]=='.'){
					draw=0;
					break;
				}
			}
			if(draw==0){
				break;
			}
		}
		if(draw==1){
			cout<<"Case #"<<testcase<<": Draw"<<endl;
		}else if(draw==0){
			cout<<"Case #"<<testcase<<": Game has not completed"<<endl;
		}
	}	
}
int main(){
	
	
	int tt;
	cin>>tt;
	for(int i=1;i<=tt;i++){
		vector <string> board;
		for(int j=0; j<4; j++) {
			string s; cin >> s;
			board.push_back(s);
		}
		check_game_state(board,i);
	}
	
	return 0;
}
