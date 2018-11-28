#include <iostream>
#include <string>


using namespace std;

int solve(string *s){
	string x[] = {"XXXX","XXXT","XXTX","XTXX","TXXX"};
	string o[] = {"OOOO","OOOT","OOTO","OTOO","TOOO"};

	// check X won in rows
	for(int i = 0; i < 4; i ++){
		for ( int j = 0; j < 5; j++ ){
			if( string::npos != s[i].find(x[j]) )
				return 0;
		}
	}
	// chech O won in rows
	for(int i = 0; i < 4; i ++){
		for ( int j = 0; j < 5; j++ ){
			if( string::npos != s[i].find(o[j]) )
				return 1;
		}
	}

	//check X won in columns
	for ( int j = 0; j < 4; j++ ){
		char a[5] = {s[0][j],s[1][j],s[2][j],s[3][j],'\0'};
		string temp = string(a);
		for(int i = 0; i < 5; i ++)
		if( string::npos != temp.find(x[i]) )
			return 0;		
	}

	//check Y won in column
	for ( int j = 0; j < 4; j++ ){
		char a[5] = {s[0][j],s[1][j],s[2][j],s[3][j],'\0'};
		string temp = string(a);
		for(int i = 0; i < 5; i ++)
		if( string::npos != temp.find(o[i]) )
			return 1;		
	}
	//check main diagonal
	char a[5] = {s[0][0],s[1][1],s[2][2],s[3][3],'\0'};
	string main_diag = string(a);

	for(int i = 0; i < 5; i++)
	{
		if( string::npos != main_diag.find(x[i]) )
			return 0;
		else if( string::npos != main_diag.find(o[i]) )
			return 1;
	}
	//check sec diagonal
	char b[5] = {s[0][3],s[1][2],s[2][1],s[3][0],'\0'};
	string sec_diag = string(b);

	for(int i = 0; i < 5; i++)
	{
		if( string::npos != sec_diag.find(x[i]) )
			return 0;
		else if( string::npos != sec_diag.find(o[i]) )
			return 1;
	}

	//draw or game not completed
	for(int i = 0; i < 4; i ++){
		for ( int j = 0; j < 4; j++ ){
			if( s[i][j] == '.' )
				return 3;
		}
	}
	return 2;
}

int main(){
	int t;
	string s[4];
	cin >> t;
	for ( int i = 0; i < t; i ++ ){
		for ( int j = 0; j < 4; j ++ ){
			cin >> s[j];	
		} 
		int res = solve(s);
		cout << "Case #"<<i+1<<": ";
		switch(res){
			case 0: 
				cout<< "X won\n";
				break; 
			case 1: 
				cout<< "O won\n";
				break;
			case 2: 
				cout<< "Draw\n";
				break;
			case 3:
				cout<< "Game has not completed\n";
				break;
		}
	}
	return 0;
}