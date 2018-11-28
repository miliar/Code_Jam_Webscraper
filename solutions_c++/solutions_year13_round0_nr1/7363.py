#include <iostream>
#include <math.h>
#include <string>
using namespace std;

bool won(char a[4][4],int tJ, int tK, char ch);

int main(){
	int testCases=0;;
	cin>>testCases;
	for(int i=1;i<=testCases;i++) {
		int tk=-1,tj=-1;
		bool notFull=0;
		char tictoe[4][4];
		for(int j=0;j<4;j++){
			for(int k=0;k<4;k++){
				cin>>tictoe[j][k];
				if(tictoe[j][k]=='.'){
					notFull = true;
				}
				if(tictoe[j][k]=='T'){
					tk=k;
					tj=j;
				}
			}
		}
		cout<<"Case #"<<i<<": ";
		if(won(tictoe,tj,tk,'X')){
			cout<<"X won"<<endl;
		}
		else if (won(tictoe,tj,tk,'O')) {
			cout<<"O won"<<endl;
		}
		else if(notFull){
			cout<<"Game has not completed"<<endl;
		}
		else {
			cout<<"Draw"<<endl;
		}

	}
}
bool won(char a[4][4],int tJ, int tK, char ch) {
	if(tK!=-1 && tJ!=-1){
		a[tJ][tK] = ch;
	}
	for (int i =0;i<4;i++){
		int diag1=0, diag2 =0,row=0, column=0;
		for (int j =0;j<4;j++){
			if(a[i][j] ==ch){
				row++;
			}
			if(a[j][i] == ch) {
				column++;
			}
			if(i==0){
				if(a[j][j]==ch){
					diag1++;
				}
				if(a[j][3-j]==ch){
					diag2++;
				}
			}
		}
		if((diag1==4 || diag2==4) || (row==4 || column==4)) {
			return true;
		}
	}
	return false;
}
