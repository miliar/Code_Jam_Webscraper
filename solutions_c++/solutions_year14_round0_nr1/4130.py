#include <stdio.h>
//#include <iostream>
#include <fstream>
using namespace std;

int main(){
	ifstream in ("A-small-attempt1.in");
	ofstream out ("output.txt");
	int caso,coso;
	in>>caso;
	
	for(coso=0;coso<caso;coso++){
		
		int r,s,i,j,probabili=0,numeroh;
		int buffer1[4][10],buffer2[4][10];
		
		in>>r;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				in>>buffer1[i][j];
			}
		}

		in>>s;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				in>>buffer2[i][j];
		}}
		//cout<<probabili<<"\n\n";
		for(i=0;i<4;i++){
			for (j=0;j<4;j++){
				if (buffer1[r-1][i]!=' ' && buffer1[r-1][i]==buffer2[s-1][j]) {probabili++; numeroh =buffer1[r-1][i];
			}
		}
	}
	
	    out<<"case #"<<coso+1<<": ";
		if(probabili==1) out<<numeroh<<"\n";
		else if (probabili==0) out<<"Volunteer cheated!"<<"\n";
		else out<<"Bad magician!"<<"\n";
}
}
