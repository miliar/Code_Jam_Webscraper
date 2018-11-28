#include<iostream>
#include<fstream>
using namespace std;
int main(){
	int i,j,result=0,complete=0,notc=0,caseno,dotfound,a;
	char ch[4][4];
	ifstream inp("input.txt");
	ofstream out("out.txt");
	inp>>notc;	
	for(caseno=1;caseno<=notc;caseno++){
		result=0;
		dotfound=0;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				inp>>ch[i][j];
			}
		}
		for(i=0;i<4;i++){
			if(((ch[i][0]=='X'|| ch[i][0]=='T') && (ch[i][1]=='X'|| ch[i][1]=='T') && (ch[i][2]=='X'|| ch[i][2]=='T') && (ch[i][3]=='X'|| ch[i][3]=='T')) ||\
			   ((ch[0][i]=='X'|| ch[0][i]=='T') && (ch[1][i]=='X'|| ch[1][i]=='T') && (ch[2][i]=='X'|| ch[2][i]=='T') && (ch[3][i]=='X'|| ch[3][i]=='T'))){
				out<<"Case #"<<caseno<<": X won"<<endl;
				result=1;
				break;
			}
			if(((ch[i][0]=='O'|| ch[i][0]=='T') && (ch[i][1]=='O'|| ch[i][1]=='T') && (ch[i][2]=='O'|| ch[i][2]=='T') && (ch[i][3]=='O'|| ch[i][3]=='T')) ||\
			   ((ch[0][i]=='O'|| ch[0][i]=='T') && (ch[1][i]=='O'|| ch[1][i]=='T') && (ch[2][i]=='O'|| ch[2][i]=='T') && (ch[3][i]=='O'|| ch[3][i]=='T'))){
				out<<"Case #"<<caseno<<": O won"<<endl;
				result=1;
				break;
			}
		}
		if(result==1)
			continue;
		if(((ch[0][0]=='X'|| ch[0][0]=='T') && (ch[1][1]=='X'|| ch[1][1]=='T') && (ch[2][2]=='X'|| ch[2][2]=='T') && (ch[3][3]=='X'|| ch[3][3]=='T')) ||\
		   ((ch[0][3]=='X'|| ch[0][3]=='T') && (ch[1][2]=='X'|| ch[1][2]=='T') && (ch[2][1]=='X'|| ch[2][1]=='T') && (ch[3][0]=='X'|| ch[3][0]=='T'))){
		   	out<<"Case #"<<caseno<<": X won"<<endl;
			result=1;
		}
		else if(((ch[0][0]=='O'|| ch[0][0]=='T') && (ch[1][1]=='O'|| ch[1][1]=='T') && (ch[2][2]=='O'|| ch[2][2]=='T') && (ch[3][3]=='O'|| ch[3][3]=='T')) ||\
		        ((ch[0][3]=='O'|| ch[0][3]=='T') && (ch[1][2]=='O'|| ch[1][2]=='T') && (ch[2][1]=='O'|| ch[2][1]=='T') && (ch[3][0]=='O'|| ch[3][0]=='T'))){
			out<<"Case #"<<caseno<<": O won"<<endl;
			result=1;
		}
		if(result==0){
			for(i=0;i<4;i++){
				for(j=0;j<4;j++){
					if(ch[i][j]=='.'){
						dotfound=1;
						break;
					}
				}
				if(dotfound==1){
					out<<"Case #"<<caseno<<": Game has not completed"<<endl;
					break;
				}
			}
		}
		if(dotfound==0 && result==0)
			out<<"Case #"<<caseno<<": Draw"<<endl;
	}
	inp.close();
	return 0;
}
