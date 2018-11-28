#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int main(){
	
	int array[4][4], array2[4][4];
	int times, no=1;
	int row1,row2,temp;
	int flag1,flag2;
	
	
	
	
	
	ifstream infile("A-small-attempt3.in");
	ofstream outfile("output.txt");
	infile >> times;

do{

flag1=flag2=0;
	infile >> row1;
	
	for(int a=0; a<4; a++)
		for(int b=0; b<4; b++)
		infile >> array[a][b];
		
				
	infile >> row2;
	
	for(int a=0; a<4; a++)
		for(int b=0; b<4; b++)
		infile >> array2[a][b];	
		
		////////////////////////// input data ////////////////
		
	for(int a=0; a<4; a++)
		for(int b=0; b<4; b++)
		if(array[row1-1][a]==array2[row2-1][b] ){
		
		if(flag1==1){
		
		flag2=1;
		break;
		}
		else{
		
		flag1=1;
		temp=b;
	}
			
		}
		
	
		outfile <<"Case #" << no  <<": ";
		if (flag1==1 && flag2 ==0)
		outfile << array2[row2-1][temp];
		
		else if (flag1==1 && flag2 ==1)
		outfile << "Bad magician!";
		else if (flag1==0 && flag2==0)
		outfile << "Volunteer cheated!";
		
		times--;
		no++;
		
			outfile <<endl;
	
		
		
		}while(times!=0);
		
	
		
	
}
