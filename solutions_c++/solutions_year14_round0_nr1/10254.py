#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char *argv[]){
	int rounds,i,j,c1,c2,tempnum,results,position;
	int answ1,answ2;
	int grid1[4],grid2[4];
	fstream myfile;
	ofstream  output;


	myfile.open("A-small-attempt0.in", ios::in | ios::binary);
	output.open("output");
	if(myfile.is_open()){
		myfile>>rounds;
		for(i=0;i<rounds;i++){
			myfile>>answ1;
			c1=c2=results=0;
			for(j=0;j<16;j++){
				myfile>>tempnum;
				if((j/4+1)==answ1){
					grid1[c1]=tempnum;
					c1++;
				}
			}
			myfile>>answ2;
			for(j=0;j<16;j++){
				myfile>>tempnum;
				if((j/4+1)==answ2){
					grid2[c2]=tempnum;
					c2++;
				}
			}
			for(c1=0;c1<4;c1++)
				for(c2=0;c2<4;c2++)
					if(grid1[c1]==grid2[c2]){
						results++;
						position=c1;
					}
			if(results==1)
				output<<"Case #"<<i+1<<": "<<grid1[position]<<endl;
			else if(results>1)
				output<<"Case #"<<i+1<<": Bad magician!"<<endl;
			else
				output<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}

