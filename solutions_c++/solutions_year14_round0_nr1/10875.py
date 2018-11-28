#include<iostream>
#include<vector>
#include<algorithm>
#include<sstream>
#include<fstream>
using namespace std;

class magictrick{
public:
	void fileread(char*);
	void readInput(int,int,int,int arrange1[4][4],int arrange2[4][4]);
	void giveOutput(int,int,int);
};
void magictrick::fileread(char* name){
	int limit,row1,row2,arrange1[4][4],arrange2[4][4];
	FILE *f = fopen(name,"r");
	int counter=0;
	int casenum=0;
	int i,j,one,two,three,four;
	fscanf(f,"%d",&limit);
	for(i=0;i<limit;i++){
		casenum+=1;
		fscanf(f,"%d",&row1);
		for(j=0;j<4;j++){
			fscanf(f,"%d %d %d %d",&one,&two,&three,&four);
			arrange1[j][0]=one;
			arrange1[j][1]=two;
			arrange1[j][2]=three;
			arrange1[j][3]=four;
		}
		fscanf(f,"%d",&row2);
		for(j=0;j<4;j++){
			fscanf(f,"%d %d %d %d",&one,&two,&three,&four);
			arrange2[j][0]=one;
			arrange2[j][1]=two;
			arrange2[j][2]=three;
			arrange2[j][3]=four;
		}
		readInput(casenum,row1,row2,arrange1,arrange2);
	}
}
void magictrick::readInput(int casenum,int row1, int row2,int arrange1[4][4],int arrange2[4][4]){
	int i;
	//int arrange1[4][4]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
	//int arrange2[4][4]={{1,2,5,4},{3,11,6,15},{9,10,7,12},{13,14,8,16}};
	int rows1[4];
	int rows2[4];
	vector<int> v(8);
	vector<int>::iterator it;
	for(i=0;i<4;i++){
		rows1[i]=arrange1[row1-1][i];
		rows2[i]=arrange2[row2-1][i];
	}
	int count=0;
	sort(rows2,rows2+4);
	sort(rows1,rows1+4);
	it=set_intersection(rows1,rows1+4,rows2,rows2+4,v.begin());
	v.resize(it-v.begin());
	int size=v.size();
	int num=0;
	if(size>1){
		size=2;
	}
	if(!v.empty()){
		num = v.front();
	}
	switch(size){
		case 1:
			giveOutput(1,num,casenum);
			break;
		case 2:
			giveOutput(2,1,casenum);
			break;
		case 0:
			giveOutput(3,1,casenum);
		default:
			break;
	}
}

void magictrick::giveOutput(int option,int num,int casenum){
	ofstream checkfile;
	checkfile.open("output.txt",ios::app);
	switch(option){
		case 1:
			checkfile<<"Case #"<<casenum<<": "<<num<<"\n";
			break;
		case 2:
			checkfile<<"Case #"<<casenum<<": Bad magician!\n";
			break;
		case 3:
			checkfile<<"Case #"<<casenum<<": Volunteer cheated!\n";
	}
	checkfile.close();
}

int main(int argc,char** argv){
	ofstream checkfile;
	checkfile.open("output.txt");
	checkfile.close();
	int option;
	char *file;
	file = argv[1];
	magictrick magic;
	magic.fileread(file);
	//magic.readInput();
}