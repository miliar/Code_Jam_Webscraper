#include <iostream>
#include <algorithm>
#include <cmath>
#include <fstream>

using namespace std;

int winner(int X,int R,int C);
int main(){
	ofstream outfile;
	outfile.open("output.txt");
	ifstream infile;
	infile.open("input.txt");
	int K;
	infile>>K;
	int X,R,C;

	for (int numcase=1;numcase<=K;numcase++){
		
		int result;
		infile>>X;
		infile>>R;
		infile>>C;

		result=winner(X,R,C);
		
		if(result==1){
		 	outfile<<"Case #" <<numcase <<": "<< "RICHARD"<<endl; 
		
		 }else{
		 	outfile<<"Case #" <<numcase <<": "<< "GABRIEL" <<endl; 
			
		 }
	}


	outfile.close();
	infile.close();
	return 0;

}

int winner(int X,int R,int C){
	if(R>C){
		int temp=C;
		C=R;
		R=temp;
	}
	if(R*C%X!=0)
		return 1;
	if(X<3)
		return 2;
	bool winner=false;
	winner |=(X==3)&&(R==2)&&(C==3);
	winner |=(X==3)&&(R==3)&&(C==3);
	winner |=(X==3)&&(R==3)&&(C==4);
	winner |=(X==4)&&(R==3)&&(C==4);
	winner |=(X==4)&&(R==4)&&(C==4);
	if(winner==false)
	{
		return 1;
	}
	if(winner==true)
	{
		return 2;
	}

}