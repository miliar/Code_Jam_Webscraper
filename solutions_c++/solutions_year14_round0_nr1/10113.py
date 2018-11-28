#include<iostream>
#include<fstream>
using namespace std;

int main(){
	ifstream infile;
	infile.open("A-small-attempt3.in");
		ofstream out;
		out.open("output.out");
	int cases;
	infile>>cases;
	int index=0;
	
	while(index<cases)
	{
		int cards[4][4];
		int cards2[4][4];
		int counter=0;
		int value1;
		infile>>value1;
		infile>>cards[0][0]>>cards[0][1]>>cards[0][2]>>cards[0][3]>>cards[1][0]>>cards[1][1]>>
			cards[1][2]>>cards[1][3]>>cards[2][0]>>cards[2][1]>>cards[2][2]>>cards[2][3]>>
			cards[3][0]>>cards[3][1]>>cards[3][2]>>cards[3][3];
		
		int value2;
		infile>>value2;
		infile>>cards2[0][0]>>cards2[0][1]>>cards2[0][2]>>cards2[0][3]>>cards2[1][0]>>cards2[1][1]>>
			cards2[1][2]>>cards2[1][3]>>cards2[2][0]>>cards2[2][1]>>cards2[2][2]>>cards2[2][3]>>
			cards2[3][0]>>cards2[3][1]>>cards2[3][2]>>cards2[3][3];
		
		int row,col;
		for( int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(cards[value1-1][i]==cards2[value2-1][j]){
					row=value1-1;
					col=i;
					counter++;
				}
				
			}	
		}

		out<<"case #"<<index+1<<": ";
		if(counter>1)
			out<<"Bad magician!"<<endl;
		if(counter<1)
			out<<"Volunteer cheated!"<<endl;
		if(counter==1)
			out<<cards[row][col]<<endl;
		index++;
	}
	
	
	
	
	
	return 0;
}