#include <iostream>
#include <fstream>
#include <iostream>

using namespace std;

int comptx;
int compto;
bool syt;
 
string tester(int o, int x, bool syt){
	if(o==4 || (o==3 && syt==true))
	 return "O won";
	else if(x==4 || (x==3 && syt==true))
	 return "X won";
	return "continue";
	}
int main(void){
	ifstream in("A-large.in") ;
	ofstream out("a.out") ;
	int t, n=1, i, j ;
	char tictac[4][4]; 
	string tst;
	in >> t ;
	while(n<=t){
		out << "Case #" << n << ": " ;
		tst="continue";
		for(i=0 ; i<4 ; i++){
			for(j=0 ; j<4 ; j++){
				in >> tictac[i][j];
			}
		}
		// ligne
		for(i=0 ; i<4 && tst=="continue" ; i++){
			comptx=0;
			compto=0;
			syt=false;
			for(j=0 ; j<4 ; j++){
				if(tictac[i][j] == 'T')
					syt = true;
				else if(tictac[i][j] == 'O')
						compto++;
				else if(tictac[i][j] == 'X')
						comptx++;
			}
			tst=tester(compto, comptx, syt);
					if(tst!="continue"){
					out << tst;
					tst="";
					i=4;
					} 
		}
		// colone
		for(j=0 ; j<4 && tst=="continue" ; j++){
			comptx=0;
			compto=0;
			syt=false;
			for(i=0 ; i<4 ; i++){
				if(tictac[i][j] == 'T')
					syt = true;
				else if(tictac[i][j] == 'O')
						compto++;
				else if(tictac[i][j] == 'X')
						comptx++;
			}
			tst=tester(compto, comptx, syt);
					if(tst!="continue"){
					out << tst;
					tst="";
					j=4;
					} 
		}
		// diagonal
		if(tst=="continue"){
			comptx=0;
			compto=0;
			syt=false;
			for(i=0 ; i<4 ; i++){
				if(tictac[i][i] == 'T')
					syt = true;
				else if(tictac[i][i] == 'O')
						compto++;
				else if(tictac[i][i] == 'X')
						comptx++;
			}
			tst=tester(compto, comptx, syt);
					if(tst!="continue"){
					out << tst;
					tst="";
					}
		}
		if(tst=="continue"){
			comptx=0;
			compto=0;
			syt=false;
			for(i=0 ; i<4 ; i++){
				if(tictac[3-i][i] == 'T')
					syt = true;
				else if(tictac[3-i][i] == 'O')
						compto++;
				else if(tictac[3-i][i] == 'X')
						comptx++;
			}
			tst=tester(compto, comptx, syt);
					if(tst!="continue"){
					out << tst;
					tst="";
					}
		}
		if(tst=="continue"){
			for(i=0 ; i<4 && tst=="continue" ; i++){
		    for(j=0 ; j<4 ; j++){
				if(tictac[i][j] == '.'){
					out << "Game has not completed";
					tst="";
					j=4;i=4;
					}
				}
			}
		}
		if(tst=="continue"){
			out << "Draw";
			tst="";
			}
		out  << endl ;
		n++;
		}
	return 0;
	}
