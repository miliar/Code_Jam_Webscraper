#include<iostream>
#include<fstream>
#include<math.h>
#include<conio.h>
#include<stdio.h>

using namespace std;

double Num, Denom, waste, temp;
int testcases, count;

bool check(double number){
	waste=log2(number);
	if(waste==int(waste)){return 1;}
	else{return 0;}
}

int main(){
	ifstream infile("A-small-attempt0 (1).in");
	ofstream outfile;
	outfile.open("2.txt");
	FILE * fin;
	fin = fopen ("A-small-attempt0 (1).in","r");
	
infile>>testcases;
fscanf(fin, "%lf", &temp);
for(int t=1; t<=testcases; t++){
	fscanf(fin,"%lf/%lf",&Num,&Denom);
	if(check(Denom)==false){outfile<<"Case #"<<t<<": "<<"impossible"<<endl;}
	else if(check(Denom)==true){
		count=0;
		while(Num<Denom){Num=Num*2; count++;}
		outfile<<"Case #"<<t<<": "<<count<<endl;	
	}
}
outfile.close();
return 0;
}
