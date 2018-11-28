#include<iostream>
#include<fstream>

using namespace std;
char whoWon(char line[4][4]);
int main() {
	ofstream myfile;
  myfile.open ("a.out");
  
 ifstream myReadFile;
 myReadFile.open("a.in");
 int T;
 char line[4][4];
 myReadFile >> T;
 for(int x= 1; x<=T;x++){

	 for(int j = 0;j<4;j++)
		 for(int k = 0;k<4;k++)
			myReadFile >> line[j][k];
	switch(whoWon(line)){
	case 'x':
		myfile<<"Case #"<<x<<": X won"<<endl;
		break;
	case 'o':
		myfile<<"Case #"<<x<<": O won"<<endl;
		break;
	case 'e':
		myfile<<"Case #"<<x<<": Draw"<<endl;
		break;
	default:
		myfile<<"Case #"<<x<<": Game has not completed"<<endl;
		break;
	}
 }
myfile.close();
myReadFile.close();
return 0;
}
char whoWon(char line[4][4]){
bool x;
bool o;
bool t;
bool p;
char won ='n';
int j,k;
	for( j=0;j<4;j++){
		x = true;
		o = true;
		t = false;
		p=false;
		for( k=0;k<4;k++){
			if(line[j][k]=='X')
				o = false;
			else if(line[j][k]=='O')
				x=false;
			else if(line[j][k]=='T')
				t = true;
			else{
				x =false;
				o = false;
				p=true;
			}
		}
		if(!p){
			if(x || x && t){
				return 'x';
				break;
			}else if(o || o && t){
				return 'o';
				break;
			}
		}
	}
	for(j=0;j<4;j++){
		x = true;
		o = true;
		t = false;
		p=false;
		for(k=0;k<4;k++){
			if(line[k][j]=='X')
				o = false;
			else if(line[k][j]=='O')
				x=false;
			else if(line[k][j]=='T')
				t = true;
			else{
				x =false;
				o = false;
				p=true;
			}
		}
		if(!p){
			if(x || x && t){
				return 'x';
				break;
			}else if(o || o && t){
				return 'o';
				break;
			}
		}
	}
	j=0;
		x = true;
		o = true;
		t = false;
		p=false;
		for(k=0;k<4;k++){
			if(line[j][k]=='X')
				o = false;
			else if(line[j][k]=='O')
				x=false;
			else if(line[j][k]=='T')
				t = true;
			else{
				x =false;
				o = false;
				p=true;
			}
			j++;
		}
		if(!p){
			if(x || x && t){
				return 'x';
			}else if(o || o && t){
				return 'o';
			}
		}
	
	j=3;
		x = true;
		o = true;
		t = false;
		p=false;
		for(k=0;k<4;k++){
			if(line[j][k]=='X')
				o = false;
			else if(line[j][k]=='O')
				x=false;
			else if(line[j][k]=='T')
				t = true;
			else{
				x =false;
				o = false;
				p=true;
			}
			j--;
		}
		if(!p){
			if(x || x && t){
				return 'x';
			}else if(o || o && t){
				return 'o';
			}
		}
	for(j=0;j<4;j++){
		p=false;
		for(k=0;k<4;k++){
			if(line[k][j]=='.')
				p = true;
		}
		if(p){
			return 'n';
		}
	}
	return 'e';
}