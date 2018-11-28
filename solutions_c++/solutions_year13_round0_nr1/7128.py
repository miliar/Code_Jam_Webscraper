#include<iostream>
using namespace std;
int main(){
	int tt;
	char bd[1000][4][4];
	int dot;
	int i,j,k;
	int p,q;
	int x, o, t;
	int X,O;
		
	cin >> tt;
	i=0;
	while(i < tt){
		for(p=0; p<4; p++){
			for(q=0;q<4; q++)
				cin >> bd[i][p][q];
		}
		//cin >> buffer;
		X=O=0;
		dot = 0;
		for(j=0; j< 4; j++){
			x=o=t=0;
			for(k=0; k<4; k++){
				if(bd[i][j][k] == 'X')
					x++;
				if(bd[i][j][k] == 'O')
					o++;
				if(bd[i][j][k] == 'T')
					t++;
				if(bd[i][j][k] == '.')
					dot++;
			}
			if((x == 4) || (x == 3) && (t == 1)) 
				X = 1;
			if((o == 4) || (o == 3) && (t == 1)) 
				O = 1;
		}
	    if(X == 0 || O == 0){
		for(j=0; j< 4; j++){
			x=o=t=0;
			for(k=0; k<4; k++){
				if(bd[i][k][j] == 'X')
					x++;
				if(bd[i][k][j] == 'O')
					o++;
				if(bd[i][k][j] == 'T')
					t++;
			}
			if((x == 4) || (x == 3) && (t == 1)) 
				X = 1;
			if((o == 4) || (o == 3) && (t == 1)) 
				O = 1;
		}
	    }
	    if(X == 0 || O == 0){
		x=o=t=0;
		for(j=0; j< 4; j++){
			
			k = j;
				if(bd[i][k][j] == 'X')
					x++;
				if(bd[i][k][j] == 'O')
					o++;
				if(bd[i][k][j] == 'T')
					t++;
			

		}
			if((x == 4) || (x == 3) && (t == 1)) 
				X = 1;
			if((o == 4) || (o == 3) && (t == 1)) 
				O = 1;
		x=o=t=0;
		k = 3;
		for(j=0; j< 4; j++){
				if(bd[i][j][k] == 'X')
					x++;
				if(bd[i][j][k] == 'O')
					o++;
				if(bd[i][j][k] == 'T')
					t++;
			k--;
			
		}
			if((x == 4) || (x == 3) && (t == 1)) 
				X = 1;
			if((o == 4) || (o == 3) && (t == 1)) 
				O = 1;
	    }
			cout << "Case #"<<i+1 <<": ";
			if(X == 1)
				cout <<"X won"<<endl;
			else if(O == 1)
				cout << "O won"<<endl;
			else if(dot > 0)
				cout << "Game has not completed"<<endl;
			else
				cout <<"Draw"<<endl;
	
	i++;
	}

	return 0;
}
