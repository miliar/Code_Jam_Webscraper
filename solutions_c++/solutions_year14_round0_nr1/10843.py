
#include <string>
#include "stdlib.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include "main.h"

#define FILENAME "A-small-attempt2.txt"

using namespace std;
int main(){
	int num_cases;
	int i;
	FILE* inputs;
	FILE* output;
	inputs=fopen(FILENAME,"r");
	output=fopen("output.txt","w");
	if(inputs==NULL) cout << "ERROR";

	fseek (inputs , 0 , SEEK_END);
	int fSize = ftell (inputs);
	rewind (inputs);


	fscanf(inputs,"%d",&num_cases);
	for(i=0;i<num_cases;i++){
	process(inputs,i+1,output);
	}
	fclose(inputs);
	fclose(output);
	system("pause");

}

int compare(int *cards){

	int i,j;
	int count=0;
	int result;
	
	for(i=0;i<4;i++){
		for(j=0;j<4;j++){
		if(cards[i]==cards[j+4]){
			count++;
			result=cards[i];
		}
		}
	}
	if(count>1) result=-1;
	if(count==0) result=0;
	return result;
}

void process(FILE* inputs,int currcase,FILE* output){
	int row1,row2;
	int cards1[8];
	int dummy[4];
	int i;
	int result;
	char Case[]="Case #";
	char A[]="Volunteer cheated!\n";
	char B[]="Bad magician!\n";
fscanf(inputs,"%d",&row1);
	for(i=1;i<5;i++){
	if(row1==i)
	fscanf(inputs,"%d %d %d %d",&cards1[0],&cards1[1],&cards1[2],&cards1[3]);
	else
	fscanf(inputs,"%d %d %d %d",&dummy[0],&dummy[1],&dummy[2],&dummy[3]);
	}
	
	fscanf(inputs,"%d",&row2);
	for(i=1;i<5;i++){
	if(row2==i)
	fscanf(inputs,"%d %d %d %d",&cards1[4],&cards1[5],&cards1[6],&cards1[7]);
	else
	fscanf(inputs,"%d %d %d %d",&dummy[0],&dummy[1],&dummy[2],&dummy[3]);
	}
	
	result=compare(cards1);
	
	cout << "Case #"<<currcase<<": ";	
	switch (result){
		case 0:
			cout<< "Volunteer cheated!"<<"\n";
			fprintf(output,Case);
			fprintf(output,"%d: ",currcase);
			fprintf(output,A);
			break;
		case -1:
			cout<< "Bad Magician!"<<"\n";
			fprintf(output,Case);
			fprintf(output,"%d: ",currcase);
			fprintf(output,B);
			break;
		default:
			cout << result<<"\n";
			fprintf(output,Case);
			fprintf(output,"%d: ",currcase);
			fprintf(output,"%d\n",result);
	}
}