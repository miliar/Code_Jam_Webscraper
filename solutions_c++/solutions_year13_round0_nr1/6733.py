#include<iostream>
#include<string>
#include<stdio.h>
using namespace std;
char arr[4][4];
int check_row(){
	bool x_win=false;
	bool o_win=false;
	int res=0;
	for(int x=0;x<4;x++){
		for(int y=0;y<4;y++){
			if(arr[x][y]=='X'||arr[x][y]=='T')
				res++;
		}
		if(res==4)
			x_win=true;
		res=0;
	}
	res =0;
	for(int x=0;x<4;x++){
		for(int y=0;y<4;y++){
			if(arr[x][y]=='O'||arr[x][y]=='T')
				res++;
		}
		if(res==4)
			o_win=true;
		res=0;
	}
	if(x_win&&o_win)
		return 3;
	else if(x_win&&!o_win)
		return 1;
	else if(!x_win&&o_win)
		return 2;
	else
		return 0;
}
int check_diagonal(){
	bool x_win=false;
	bool o_win=false;
	if((arr[3][3]=='X'||arr[3][3]=='T')&&
	   (arr[2][2]=='X'||arr[2][2]=='T')&&
	   (arr[1][1]=='X'||arr[1][1]=='T')&&
	   (arr[0][0]=='X'||arr[0][0]=='T'))
	   x_win=true;
	if((arr[3][3]=='O'||arr[3][3]=='T')&&
	   (arr[2][2]=='O'||arr[2][2]=='T')&&
	   (arr[1][1]=='O'||arr[1][1]=='T')&&
	   (arr[0][0]=='O'||arr[0][0]=='T'))
	   o_win=true;
	if((arr[0][3]=='X'||arr[0][3]=='T')&&
	   (arr[1][2]=='X'||arr[1][2]=='T')&&
	   (arr[2][1]=='X'||arr[2][1]=='T')&&
	   (arr[3][0]=='X'||arr[3][0]=='T'))
	   x_win=true;
	if((arr[0][3]=='O'||arr[0][3]=='T')&&
	   (arr[1][2]=='O'||arr[1][2]=='T')&&
	   (arr[2][1]=='O'||arr[2][1]=='T')&&
	   (arr[3][0]=='O'||arr[3][0]=='T'))
	   o_win=true;
	if(x_win&&o_win)
		return 3;
	else if(x_win&&!o_win)
		return 1;
	else if(!x_win&&o_win)
		return 2;
	else
		return 0;
}
int check_col(){
	bool x_win=false;
	bool o_win=false;
	int res=0;
	for(int x=0;x<4;x++){
		for(int y=0;y<4;y++){
			if(arr[y][x]=='X'||arr[y][x]=='T')
				res++;
		}
		if(res==4)
			x_win=true;
		res=0;
	}
	res =0;
	for(int x=0;x<4;x++){
		for(int y=0;y<4;y++){
			if(arr[y][x]=='O'||arr[y][x]=='T')
				res++;
		}
		if(res==4)
			o_win=true;
		res=0;
	}
	if(x_win&&o_win)
		return 3;
	else if(x_win&&!o_win)
		return 1;
	else if(!x_win&&o_win)
		return 2;
	else
		return 0;
}
int main(){
	freopen("A-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t=0;
	int count=0;
	cin>>t;
	cin.ignore();
	while(t--){
		count++;
		bool full=true;
		for(int x=0;x<4;x++)
			for(int y=0;y<4;y++){
				cin>>arr[x][y];
				if(arr[x][y] == '.')
					full=false;
			}
		int col = check_col();
		int row =check_row();
		int dia = check_diagonal();
		cout<<"Case #"<<count<<": ";
		if(col==1){
			cout<<"X won"<<endl;
			continue;
		}
		if(col==2){
			cout<<"O won"<<endl;
			continue;
		}
		if(row==1){
			cout<<"X won"<<endl;
			continue;
		}
		if(row==2){
			cout<<"O won"<<endl;
			continue;
		}
		if(dia==1){
			cout<<"X won"<<endl;
			continue;
		}
		if(dia==2){
			cout<<"O won"<<endl;
			continue;
		}
		if(!full){
			cout<<"Game has not completed"<<endl;
			continue;
		}
		cout<<"Draw"<<endl;


	}
	return 0;
}