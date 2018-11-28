#include <iostream>
#include <string.h>
using namespace std;

class Trick{
	int gridI[4][4],gridF[4][4];
	int i1,i2;
	char out[30];
	int check;
public:
	static int index;

	void init(){
		check = 0;
		strcpy(out,"\0");
	}

	void getGridI(){
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++)
				cin>>gridI[i][j];
		}
	}

	void getGridF(){
		for(int i=0 ; i<4 ; i++){
			for(int j=0 ; j<4 ; j++)
				cin>>gridF[i][j];
		}
	}

	void getI1(){
		cin>>i1;
	}

	void getI2(){
		cin>>i2;
	}

	void calOut(){
		int tempOut=0;
		
		for(int i=0 ; i<4 ; i++){
			int a = gridI[i1-1][i];
			for(int j=0 ; j<4 ; j++){
				int b = gridF[i2-1][j];
				if(a == b){
					tempOut = a;
					check++;
				}
			}
		}

		if(check == 0)
			strcpy(out,"Volunteer cheated!");
		else if(check > 1){
			strcpy(out,"Bad magician!");
		}
		else{
			char c[5];
			if(tempOut > 9){
				c[1] = (tempOut % 10) + 48;
				tempOut = tempOut / 10;
			}
			c[0] = tempOut + 48;
			strcpy(out,c);
		}
	}

	void showOut(){
		cout<<"Case #"<<index<<": "<<out<<endl;
		index++;
	}

};

int Trick::index = 1;

int main(){
	int testCases;
	cin>>testCases;
	Trick obj[testCases];

	for(int i=0 ; i<testCases ; i++){
		obj[i].init();
		obj[i].getI1();
		obj[i].getGridI();
		obj[i].getI2();
		obj[i].getGridF();
		obj[i].calOut();
	}

	for(int i=0 ; i<testCases ; i++){
		obj[i].showOut();
	}
	return 0;
}