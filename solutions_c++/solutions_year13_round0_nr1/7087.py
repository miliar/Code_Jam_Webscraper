using namespace std;
#include <iostream>
int main(){
	int n, i, j, k;
	char a[1000][4][4];
	int status[1000];
	int calc[1000];
	cin>>n;
	for(i=1 ; i<=n ; i++){
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				cin>>a[i-1][j][k];
			}
		}
	}
	for(i = 0; i<n; i++){
		calc[i] = 0;
	}
	//CHECK FOR X/O IN EACH COLUMN
	for(i=0 ; i<n ; i++){
		for(j=0;j<4;j++){
			if(
				(a[i][j][0] == 'X' || a[i][j][0] == 'T') && 
				(a[i][j][1] == 'X' || a[i][j][1] == 'T') && 
				(a[i][j][2] == 'X' || a[i][j][2] == 'T') &&
				(a[i][j][3] == 'X' || a[i][j][3] == 'T')
			  ){
				status[i] = 1;
				calc[i] =1;
			}
			if(
				(a[i][j][0] == 'O' || a[i][j][0] == 'T') && 
				(a[i][j][1] == 'O' || a[i][j][1] == 'T') && 
				(a[i][j][2] == 'O' || a[i][j][2] == 'T') &&
				(a[i][j][3] == 'O' || a[i][j][3] == 'T')
			  ){
				status[i] = 2;
				calc[i] =1;
			}
		}
	}

	//CHECK FOR X/O IN EACH ROW
	for(i=0 ; i<n ; i++){
		for(j=0;j<4;j++){
			if(
				(a[i][0][j] == 'X' || a[i][0][j] == 'T') && 
				(a[i][1][j] == 'X' || a[i][1][j] == 'T') && 
				(a[i][2][j] == 'X' || a[i][2][j] == 'T') &&
				(a[i][3][j] == 'X' || a[i][3][j] == 'T')
			  ){
				status[i] = 1;
				calc[i] =1;
			}
			if(
				(a[i][0][j] == 'O' || a[i][0][j] == 'T') && 
				(a[i][1][j] == 'O' || a[i][1][j] == 'T') && 
				(a[i][2][j] == 'O' || a[i][2][j] == 'T') &&
				(a[i][3][j] == 'O' || a[i][3][j] == 'T')
			  ){
				status[i] = 2;
				calc[i] =1;
			}
		}
	}

	//CHECK FOR DIAGONALS
	for(i=0 ; i<n ; i++){
		if(
			(a[i][0][0] == 'X' || a[i][0][0] == 'T') && 
			(a[i][1][1] == 'X' || a[i][1][1] == 'T') && 
			(a[i][2][2] == 'X' || a[i][2][2] == 'T') &&
			(a[i][3][3] == 'X' || a[i][3][3] == 'T')
		  ){
			status[i] = 1;
			calc[i] =1;
		}
		if(
			(a[i][0][3] == 'X' || a[i][0][3] == 'T') && 
			(a[i][1][2] == 'X' || a[i][1][2] == 'T') && 
			(a[i][2][1] == 'X' || a[i][2][1] == 'T') &&
			(a[i][3][0] == 'X' || a[i][3][0] == 'T')
		  ){
			status[i] = 1;
			calc[i] =1;
		}
		if(
			(a[i][0][0] == 'O' || a[i][0][0] == 'T') && 
			(a[i][1][1] == 'O' || a[i][1][1] == 'T') && 
			(a[i][2][2] == 'O' || a[i][2][2] == 'T') &&
			(a[i][3][3] == 'O' || a[i][3][3] == 'T')
		  ){
			status[i] = 2;
			calc[i] =1;
		}
		if(
			(a[i][0][3] == 'O' || a[i][0][3] == 'T') && 
			(a[i][1][2] == 'O' || a[i][1][2] == 'T') && 
			(a[i][2][1] == 'O' || a[i][2][1] == 'T') &&
			(a[i][3][0] == 'O' || a[i][3][0] == 'T')
		  ){
			status[i] = 2;
			calc[i] =1;
		}

	}

	for(i=0 ; i<n ; i++){
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				if(a[i][j][k] == '.' && calc[i] != 1){
					status[i] = 4;
					calc[i] = 1;
				}
			}
		}
	}


	for(i = 0; i<n;i++){
		if(calc[i] == 0){
			status[i] = 3;
		}	
	}
	for(i=0 ; i<n ; i++){
		switch(status[i]){
			case 1:
				cout<<"Case #"<<i+1<<": X won"<<endl;
				break;
			case 2:
				cout<<"Case #"<<i+1<<": O won"<<endl;
				break;		
			case 3:
				cout<<"Case #"<<i+1<<": Draw"<<endl;
				break;
			case 4:
				cout<<"Case #"<<i+1<<": Game has not completed"<<endl;
				break;
		}
	}
	return 0;
}
