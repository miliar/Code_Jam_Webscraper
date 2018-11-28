#include<iostream>
#include<fstream>

using namespace std;

//#define T 10
ifstream ifs("A-small-attempt2.in");
ofstream ofs("ans.txt");
int main(){
	int table[4][4][10]; //○×の書かれたフィールド	
	int n; //入力の個数
	int i,j,k;
	int flag = 0; //1でO 2でX 3でDRAW 4で未終了

	char temp;
	
	//初期化
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			for(k=0;k<10;k++){
			table[i][j][k] = 0;
			}
		}
	}
	
	//ファイル入力
	//cin >> n;
	ifs >> n;

	for(i=0;i<n;i++){
		for(j=0;j<4;j++){
			for(k=0;k<4;k++){
				//cin >> temp;
				ifs >> temp;
				if(temp == 'O')
					table[j][k][i] = 0;
				else if(temp == 'X')
					table[j][k][i] = 1;
				else if(temp == 'T')
					table[j][k][i] = 2;
				else
					table[j][k][i] = 3;
			}
		}
	}
	/*
	for(k=0;k<n;k++){
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
			cout << table[i][j][k] <<endl;
			}
		}
	}
	*/
	
	//ファイル出力
	for(i=0;i<n;i++){
		flag = 0;
		//1
		if(table[0][0][i]==0||table[0][0][i]==2){
			if((table[0][1][i]==0||table[0][1][i]==2)&&(table[0][2][i]==0||table[0][2][i]==2)&&(table[0][3][i]==0||table[0][3][i]==2))
				flag = 1;
			else if((table[1][1][i]==0||table[1][1][i]==2)&&(table[2][2][i]==0||table[2][2][i]==2)&&(table[3][3][i]==0||table[3][3][i]==2))
				flag = 1;
			else if((table[1][0][i]==0||table[1][0][i]==2)&&(table[2][0][i]==0||table[2][0][i]==2)&&(table[3][0][i]==0||table[3][0][i]==2))
				flag = 1;
		}
		if(flag!=0){}
		else if(table[0][0][i]==1||table[0][0][i]==2){
			if((table[1][0][i]==1||table[1][0][i]==2)&&(table[2][0][i]==1||table[2][0][i]==2)&&(table[3][0][i]==1||table[3][0][i]==2))
				flag = 2;
			else if((table[0][1][i]==1||table[0][1][i]==2)&&(table[0][2][i]==1||table[0][2][i]==2)&&(table[0][3][i]==1||table[0][3][i]==2))
				flag = 2;
			else if((table[1][1][i]==1||table[1][1][i]==2)&&(table[2][2][i]==1||table[2][2][i]==2)&&(table[3][3][i]==1||table[3][3][i]==2))
				flag = 2;
		}
		//2
		if(flag!=0){}
		else if(table[1][1][i]==0||table[1][1][i]==2){
			if((table[1][0][i]==0||table[1][0][i]==2)&&(table[1][2][i]==0||table[1][2][i]==2)&&(table[1][3][i]==0||table[1][3][i]==2))
				flag = 1;
			else if((table[0][1][i]==0||table[0][1][i]==2)&&(table[2][1][i]==0||table[2][1][i]==2)&&(table[3][1][i]==0||table[3][1][i]==2))
				flag = 1;
		}
		if(flag!=0){}
		else if(table[1][1][i]==1||table[1][1][i]==2){
			if((table[1][0][i]==1||table[1][0][i]==2)&&(table[1][2][i]==1||table[1][2][i]==1)&&(table[1][3][i]==1||table[1][3][i]==2))
				flag = 2;
			else if((table[0][1][i]==1||table[0][1][i]==2)&&(table[2][1][i]==1||table[2][1][i]==2)&&(table[3][1][i]==1||table[3][1][i]==2))
				flag = 2;
		}
		//3
		if(flag!=0){}
		else if(table[2][2][i]==0||table[2][2][i]==2){
			if((table[2][0][i]==0||table[2][0][i]==2)&&(table[2][1][i]==0||table[2][1][i]==2)&&(table[2][3][i]==0||table[2][3][i]==2))
				flag = 1;
			else if((table[0][2][i]==0||table[0][2][i]==2)&&(table[1][2][i]==0||table[1][2][i]==2)&&(table[3][2][i]==0||table[3][2][i]==2))
				flag = 1;
		}
		if(flag!=0){}
		else if(table[2][2][i]==1||table[2][2][i]==2){
			if((table[2][0][i]==1||table[2][0][i]==2)&&(table[2][1][i]==1||table[2][1][i]==2)&&(table[2][3][i]==1||table[2][3][i]==2))
				flag = 2;
			else if((table[0][2][i]==1||table[0][2][i]==2)&&(table[1][2][i]==1||table[1][2][i]==2)&&(table[3][2][i]==1||table[3][2][i]==2))
				flag = 2;
		}
		//4
		if(flag!=0){}
		else if(table[3][3][i]==0||table[3][3][i]==2){
			if((table[3][0][i]==0||table[3][0][i]==2)&&(table[3][1][i]==0||table[3][1][i]==2)&&(table[3][2][i]==0||table[3][2][i]==2))
				flag = 1;
			else if((table[0][3][i]==0||table[0][3][i]==2)&&(table[1][3][i]==0||table[1][3][i]==2)&&(table[2][3][i]==0||table[2][3][i]==2))
				flag = 1;
		}
		
		if(flag!=0){}
		else if(table[3][3][i]==1||table[3][3][i]==2){
			if((table[3][0][i]==1||table[3][0][i]==2)&&(table[3][1][i]==1||table[3][1][i]==2)&&(table[3][2][i]==1||table[3][2][i]==2))
				flag = 2;
			else if((table[0][3][i]==1||table[0][3][i]==2)&&(table[1][3][i]==1||table[1][3][i]==2)&&(table[2][3][i]==1||table[2][3][i]==2))
				flag = 2;
		}
		//5
		if(flag!=0){}
		else if(table[0][3][i]==0||table[0][3][i]==2){
			if((table[3][0][i]==0||table[3][0][i]==2)&&(table[2][1][i]==0||table[2][1][i]==2)&&(table[1][2][i]==0||table[1][2][i]==2))
				flag = 1;
		}
		if(flag!=0){}
		else if(table[0][3][i]==1||table[0][3][i]==2){
			if((table[3][0][i]==1||table[3][0][i]==2)&&(table[2][1][i]==1||table[2][1][i]==2)&&(table[1][2][i]==1||table[1][2][i]==2))
				flag = 2;
		}

		if(flag == 0){
			for(j=0;j<4;j++){
				for(k=0;k<4;k++){
					if(table[j][k][i]==3)
						flag = 3;
					if(flag == 3)
						break;
				}
				if(flag == 3)
						break;
			}
		}

		//cout << "Case #" << (i+1) << ": ";
		ofs << "Case #" << (i+1) << ": ";
		if(flag==0)
			//cout << "Draw" << endl;
			ofs << "Draw" << endl;
		else if(flag==1)
			//cout << "O won" << endl;
			ofs << "O won" << endl;
		else if(flag==2)
			//cout << "X won" << endl;
			ofs << "X won" << endl;
		else if(flag==3)
			//cout << "Game has not completed" << endl;
			ofs << "Game has not completed" << endl;
	}
	
	return 0;
}