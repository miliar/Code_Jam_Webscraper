#include <iostream>
#include <fstream>

using namespace std;
char tab[4][4];
fstream file("A-large.in");
fstream out("out.txt");
bool isfull=true,reslt=false;
string result="Draw";
void switcher(int val){
	switch(val){
		case 316:
		case 321:
		result="O won";
		reslt=true;
		break;
		case 352:
		case 348:
		result="X won";
		reslt=true;
		}
}

void read(){
for(int i=0;i<4;i++)
	for(int j=0;j<4;j++){
	file>>tab[i][j];
	if(tab[i][j]=='.')
	isfull=false;
	}
}
void hori(){
int val;
for(int i=0;i<4&&!reslt;i++){
	val=0;
	for(int j=0;j<4;j++)
	val+=tab[i][j];
	switcher(val);
	}
}
void vert(){
int val;
for(int i=0;i<4&&!reslt;i++){
	val=0;
	for(int j=0;j<4;j++)
	val+=tab[j][i];
	switcher(val);
	}
}


void diag(){
int val=0;
for(int i=0;i<4;i++)
	val+=tab[i][i];
	switcher(val);
	val=0;
for(int i=0;i<4&&!reslt;i++)
	val+=tab[3-i][i];
	switcher(val);
	}

int main(){
int no;
file>>no;
for(int i=0;i<no;i++){
	isfull=true;
	reslt=false;
	result="Draw";
	read();
	hori();
	if(!reslt)
	vert();
	if(!reslt)
	diag();
	if(!reslt&&!isfull)
	result="Game has not completed";
	out<<"Case #"<<i+1<<": "<<result<<endl;
}
return 0;
}