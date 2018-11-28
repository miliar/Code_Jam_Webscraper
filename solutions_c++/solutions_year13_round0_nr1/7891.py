#include<iostream>
#include<conio.h>//comment in the last
#include<fstream>
using namespace std;



class Square{
public:
	char box[4][4];
	Square(){
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++){
				box[i][j]='.';
			}
		}
	}
	void input(){
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++){
				box[i][j]=_getche();
			}
		}
		char p=_getche();//for enter
	}

	bool checkX(char c){
		char check[]={ c , 'T'};
		bool checker,checker2;
		for(int i=0 ; i<4 ; i++){
			checker=checker2=true;
			for(int j=0 ; j<4 ; j++){
				if(box[i][j]!=check[0] && box[i][j]!=check[1]){
					checker=false;
				}
				if(box[j][i]!=check[0] && box[j][i]!=check[1]){
					checker2=false;
				}
			}
			if(checker  || checker2){
				return true;
			}
		}
			checker=checker2=true;
		for(int i=0 ; i<4 ; i++){
			if(box[i][i]!=check[0] && box[i][i]!=check[1])
				checker=false;
			if(box[i][3-i]!=check[0]  && box[i][3-i]!=check[1])
				checker2=false;
		}
		if(checker  || checker2){
			return true;
		}
		return false;
	}
	bool draw(){
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++){
				if(box[i][j]=='.'){
					return false;
				}
			}
		}
		return true;
	}

};

int main(){
	char xx[]="X won";
	char oo[]="O won";
	char dd[]="Draw";
	char uu[]="Game has not completed";
	Square obj;
	char boxo[][5]={
		"XXXO","..O.",".O..","T..."
	};
	char c;
	
	ofstream file("output3.txt");
	ifstream filein("a.txt");
	//ifstream filein("A-small-attempt.in");
	filein>>c>>c;
	filein>>c>>c;
		//obj.input();
		//for(int i= 0 ; i<4 ; i++){
		//	for(int j=0 ; j<4 ; j++){
		//		obj.box[i][j]=boxo[i][j];
		//	}
		//}
	int i=1;
	for(int i=1 ;i <1001 ; i++){
		file<<"Case #"<<i<<":"<<" ";
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++){
				filein>>obj.box[i][j];
			}
		}
		if(obj.checkX('X'))
			file<<xx;
		else if(obj.checkX('O'))
			file<<oo;
		else if(obj.draw())
			file<<dd;
		else
			file<<uu;
		file<<"\n";
	}
	return 0;
}