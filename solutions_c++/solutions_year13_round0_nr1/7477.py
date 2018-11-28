#include<iostream>
#include<string>
using namespace std;

void takeinput();
bool xwin(int);
bool owin(int);
bool draw(int);
bool incomplete(int);

int t;
string input[10][4];

int main()
{
takeinput();
for(int i=0;i<t;i++){
	if(xwin(i)){
		cout<<"Case #" <<i+1 <<": X won" <<endl;	
	}
	else if(owin(i)){
		cout<<"Case #" <<i+1 <<": O won" <<endl;	
	}
	else if(draw(i)){
		cout<<"Case #" <<i+1 <<": Draw" <<endl;	
	}
	else if(incomplete(i)){
		cout<<"Case #" <<i+1 <<": Game has not completed" <<endl;	
	}
}
return 0;	
}

bool incomplete(int cas)
{	
return true;	
}

bool draw(int cas)
{
	for(int i=0;i<4;i++){
		for(int j=0;j<4;j++){
			if(input[cas][i][j]=='.')
				return false;	
		}
	}
return true;	
}

bool owin(int cas)
{
	for(int i=0;i<4;i++){
		if((input[cas][i][0]=='O'||input[cas][i][0]=='T')&&(input[cas][i][1]=='O'||input[cas][i][1]=='T')&&(input[cas][i][2]=='O'||input[cas][i][2]=='T')&&(input[cas][i][3]=='O'||input[cas][i][3]=='T')){
			return true;
		}
		else if((input[cas][0][i]=='O'||input[cas][0][i]=='T')&&(input[cas][1][i]=='O'||input[cas][1][i]=='T')&&(input[cas][2][i]=='O'||input[cas][2][i]=='T')&&(input[cas][3][i]=='O'||input[cas][3][i]=='T')){
			return true;
		}
	}
	if((input[cas][0][0]=='O'||input[cas][0][0]=='T')&&(input[cas][1][1]=='O'||input[cas][1][1]=='T')&&(input[cas][2][2]=='O'||input[cas][2][2]=='T')&&(input[cas][3][3]=='O'||input[cas][3][3]=='T'))
		return true;
	if((input[cas][0][3]=='O'||input[cas][0][3]=='T')&&(input[cas][1][2]=='O'||input[cas][1][2]=='T')&&(input[cas][2][1]=='O'||input[cas][2][1]=='T')&&(input[cas][3][0]=='O'||input[cas][3][0]=='T'))
		return true;
return false;	
}

bool xwin(int cas)
{
	for(int i=0;i<4;i++){
		if((input[cas][i][0]=='X'||input[cas][i][0]=='T')&&(input[cas][i][1]=='X'||input[cas][i][1]=='T')&&(input[cas][i][2]=='X'||input[cas][i][2]=='T')&&(input[cas][i][3]=='X'||input[cas][i][3]=='T')){
			return true;
		}
		else if((input[cas][0][i]=='X'||input[cas][0][i]=='T')&&(input[cas][1][i]=='X'||input[cas][1][i]=='T')&&(input[cas][2][i]=='X'||input[cas][2][i]=='T')&&(input[cas][3][i]=='X'||input[cas][3][i]=='T')){
			return true;
		}
	}
	if((input[cas][0][0]=='X'||input[cas][0][0]=='T')&&(input[cas][1][1]=='X'||input[cas][1][1]=='T')&&(input[cas][2][2]=='X'||input[cas][2][2]=='T')&&(input[cas][3][3]=='X'||input[cas][3][3]=='T'))
		return true;
	if((input[cas][0][3]=='X'||input[cas][0][3]=='T')&&(input[cas][1][2]=='X'||input[cas][1][2]=='T')&&(input[cas][2][1]=='X'||input[cas][2][1]=='T')&&(input[cas][3][0]=='X'||input[cas][3][0]=='T'))	
		return true;
return false;
}

void takeinput()
{
	cin>>t;
	for(int i=0;i<t;i++){
		for(int j=0;j<4;j++){
			cin>>input[i][j];
		}
		//cout<<"\n";
	}	
}
