#include<iostream>
#include <fstream>
using namespace std;

int main(){
	// Declarations
	// InputFile in;
	ifstream in;
	
	// OutputFile o;
	ofstream o;
	
	// declarations
	int T,row1,row2,i,j,raw,found=0,d=0,k=0;
	int data1[16],data2[16];
	int flag=0,count=0,rl1=1,rl2=1;
	
	
	// open in file "A-small-attempt0.in"
	in.open("A-small-attempt1.in");

	// open output file "A-small-attempt0.out"
	o.open("A-small-attempt1.out");
	in>>T;
	
	// while ( in not EOF )
	while(!in.eof()){
		// read number from in file
		in>>row1;
		if(in.eof()) break;
		for(i=0;i<16;i++)
			in>>data1[i];
		
		in>>row2;
		
		for(i=0;i<16;i++)
			in>>data2[i];
				
		rl1= ((row1 * 4) - 4);
		count=0;
		flag=0;
		for(i=0;i<4;i++){
			rl2= ((row2 * 4) - 4);
			for(j=0;j<4;j++){
				if(data1[rl1] == data2[rl2]){
					flag=1;
					found=data1[rl1];
					count++;
				}
				rl2++;
			}
			rl1++;
		}
		d++;
		if(flag==0)
			o<<"Case #"<<d<<": Volunteer cheated!"<<endl;
		else{
			if(count>1)
				o<<"Case #"<<d<<": Bad magician!"<<endl;
			else
				o<<"Case #"<<d<<": "<<found<<endl;
		}		
		in.ignore(80, '\n');
	}
	
	
	// close inp
	in.close();
	
	// close outt
	o.close();
	
	// Stop
	return 0;
}
