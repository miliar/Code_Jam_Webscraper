#include<fstream>
#include<string>
//#include<math.h>
//#include<iostream>
//#include <conio>
//#include<stdio.h>
//#define INPUTFILENAME "test.txt"
#define INPUTFILENAME "A-large.in"
#define OUTPUTFILENAME "OutputA.txt"
using namespace std;


int main(){

register int t,n,j,k,i;
	ifstream input;
  	ofstream output;
  	input.open(INPUTFILENAME);
  	output.open(OUTPUTFILENAME);
  	input>>t;
  	
  	string buf;
  	getline(input,buf);
	int *Y=new int[10];
    int *A=new int[26];
    
  	for(j=0;j<25;j++)
		A[j]=0;
  	
	for(k=0;k<10;k++)
  		Y[k]=0;
    

  	
	  for(i=0;i<t;i++){
		string line;//=new char[2000];
		getline( input, line );
		
    	for ( k=0; k < line.length(); k++){
 			A[line[k]-'A']++;
		}

		while(A['Z'-'A']!=0){
		  Y[0]++;
		  A['Z'-'A']--;
		  A['E'-'A']--;
		  A['R'-'A']--;
		  A['O'-'A']--;
		}
		while(A['W'-'A']!=0){
		  Y[2]++;
		  A['T'-'A']--;
		  A['W'-'A']--;
		  A['O'-'A']--;
		}
		while(A['U'-'A']!=0){
		  Y[4]++;
		  A['F'-'A']--;
		  A['O'-'A']--;
		  A['U'-'A']--;
		  A['R'-'A']--;
		}
		while(A['X'-'A']!=0){
		  Y[6]++;
		  A['S'-'A']--;
		  A['I'-'A']--;
		  A['X'-'A']--;
		}
		
		while(A['G'-'A']!=0){
		  Y[8]++;
		  A['E'-'A']--;
		  A['I'-'A']--;
		  A['G'-'A']--;
		  A['H'-'A']--;
		  A['T'-'A']--;
		}
		
		
		while(A['O'-'A']!=0){
		  Y[1]++;
		  A['O'-'A']--;
		  A['N'-'A']--;
		  A['E'-'A']--;
		}
		
		while(A['F'-'A']!=0){
		  Y[5]++;
		  A['F'-'A']--;
		  A['I'-'A']--;
		  A['V'-'A']--;
		  A['E'-'A']--;
		}
		
		while(A['T'-'A']!=0){
		  Y[3]++;
		  A['T'-'A']--;
		  A['H'-'A']--;
		  A['R'-'A']--;
		  A['E'-'A']-=2;
		}
		
		while(A['I'-'A']!=0){
		  Y[9]++;
		  A['N'-'A']-=2;
		  A['I'-'A']--;
		  A['E'-'A']--;
		}
		while(A['S'-'A']!=0){
		  Y[7]++;
		  A['S'-'A']--;
		  A['E'-'A']-=2;
		  A['V'-'A']--;
		  A['N'-'A']--;
		}

		output<<"Case #"<<i+1<<": ";
		for(register int k=0;k<10;k++)
		   for(;Y[k]>0;Y[k]--){		   
		     output<<k;
		 }
		output<<endl;
		  
}
 	
  	input.close();
  	output.close();
	  return 0;
  	
}
  
