#include <iostream>
#include <string>
#include <cstring>

using namespace std;

int countX = 0;
int countO = 0;
int countPoint = 0;
string game[4][4];
	string lineGame;

int main(){

	int cases = 0;
	int n = 0;
	bool over = false;
	
	cin >> cases;
	while (n < cases) {
		//preenche game
		for (int i = 0; i< 4; i++){
			cin >> lineGame;
			for(int j = 0; j< 4; j++){
				game[i][j] = lineGame[j];
				if (game[i][j] =="X"){ countX++;}
				if (game[i][j] =="O"){ countO++;}
				if (game[i][j] =="."){ countPoint++;}
			}
		}
	
		//Diagonais
		if(!over){
			if (
				((game[0][0] == "T" || game[0][0] == game[1][1] ) && (game[1][1]== game[2][2]) && (game[2][2] ==game[3][3] || game[3][3] =="T")) 
				||
				( (game[0][3] == game[1][2] || game[0][3] == "T") && (game[1][2] == game[2][1]) && (game[2][1] == game[3][0] || game[3][0] == "T" ) ) 
				)	
			 {
				if( ( (game[0][0] == "X" && game[1][1] == "X" && game[2][2] == "X" ) || (game[0][0] == "T" && game[1][1] == "X" && game[2][2] == "X")) 							|| 
					((game[0][3] == "X" && game[1][2] == "X" && game[2][1] == "X") || (game[0][3] == "T" && game[1][2] == "X" && game[2][1] == "X") ) ){
					cout << "Case #"<<n+1<<": X won "<<endl;
					over = true;
				}
				else if( ( (game[0][0] == "O" && game[1][1] == "O" && game[2][2] == "O") || (game[0][0] == "T" && game[1][1] == "O" && game[2][2] == "O")) || 
					((game[0][3] == "O" && game[1][2] == "O" && game[2][1] == "O") || (game[0][3] == "T" && game[1][2] == "O" && game[2][1] == "O") ) ){
					cout << "Case #"<<n+1<<": O won "<<endl;						
					over = true;
				}
			}
		}
		//verificações horizontais
		if(!over){
			for(int i = 0; i < 4; i++) {
				if( ((game[i][0] == game[i][1] && game[i][1] == game[i][2] && game[i][3]==game[i][2]) ||
					(game[i][1] == game[i][2] && game[i][2] == game[i][3] && game[i][0]==game[i][3]) )
					||
					((game[i][0] == game[i][1] && game[i][1] == game[i][2] && game[i][3]=="T") ||
					(game[i][1] == game[i][2] && game[i][2] == game[i][3] && game[i][0]=="T") )){
				
					if((game[i][0] == "X") || (game[i][1] == "X")){
						cout << "Case #"<<n+1<<": X won "<<endl;
						over = true;
						break;
					}
					else if(game[i][0] == "O" || game[i][1] == "O"){
						cout << "Case #"<<n+1<<": O won "<<endl;						
						over = true;
						break;
					}
				}
			}
		}
		//verificação vertical
		if(!over){
			for (int j = 0; j < 4; j++){
				if( (game[0][j] == game[1][j] && game[1][j] == game[2][j] && game[2][j] == game[3][j])
					||
				
				( game[0][j] == game[1][j] && game[1][j] == game[2][j] && game[3][j]=="T") ||
					( game[1][j] == game[2][j] && game[2][j] == game[3][j]  && game[0][j]=="T") ||
					( game[0][j] == game[3][j] && (game[1][j] == "T " || game[2][j] == "T" ))
					 )
					{
				
					if((game[0][j] == "X") || (game[1][j] == "X")){
						cout << "Case #"<<n+1<<": X won "<<endl;
						over = true;
						break;
					}
					else if(game[0][j] == "O" || game[1][j] == "O"){
						cout << "Case #"<<n+1<<": O won "<<endl;						
						over = true;
						break;
					}
				}
			}
		}
		if(!over){
			if((countX == (countO -1) ||  (countX -1) == countO || (countO == countX)) && (countPoint < countO || countPoint < countX) ){
				cout << "Case #"<<n+1<<": Draw "<<endl;
				over = true;
			}else if(countPoint > countX || countPoint > countO){
				cout << "Case #"<<n+1<<": Game has not completed "<<endl;
				over = true;
			}
		}
		
		n++;
		countX = 0;
		countO = 0;
		countPoint = 0;
		over = false;
	}
}
//g++ -o problemA problemA.cpp
// ./problemA < problemAIn.txt
