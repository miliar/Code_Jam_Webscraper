#include <iostream>
#include <conio.h>
#include <fstream>

using namespace std;

int main(){
	
	int count, no=1, amount;
	int wken=0, wnaomi=0;
	double temp;	
	ifstream infile("D-large.in");
	
	ofstream outfile("output.txt");
	
	infile >> count;
	
	do 
	{
	
	infile >> amount;
	
	
	double naomi[amount], ken[amount];
	double c_naomi[amount], c_ken[amount];
	
	for(int a=0; a<amount; a++)
	infile >> naomi[a];
	
	for(int a=0; a<amount; a++)
	infile >> ken[a];
	
	
	for (int a=0; a<amount; a++){
		
		c_naomi[a]=naomi[a];
		c_ken[a]=ken[a];	
	}
	
	
	
	
	for (int a=0; a<amount-1; a++){
		
		if(ken[a] > ken[a+1])	{
		
		temp=ken[a];
		ken[a]=ken[a+1];
		ken[a+1]=temp;
		a=-1;
		}
	}
	
	
	for (int a=0; a<amount; a++){
		
		if (naomi[a]==0)
		continue;
		
		for (int b=0; b<amount; b++)
		{
			if(ken[b]==0)
			continue;
			else if (ken[b]>naomi[a]){
				ken[b]=naomi[a]=0;
				wken++;
				a=0;
				break;
				
			}
		}
		
		
	}
	wken= amount-wken;	
	
	for (int a=0; a<amount-1; a++){
		
		if(c_ken[a] < c_ken[a+1])	{
		
		temp=c_ken[a];
		c_ken[a]=c_ken[a+1];
		c_ken[a+1]=temp;
		a=-1;
		}
		
		
	}
	for (int a=0; a<amount-1; a++){
		
		if(c_naomi[a] > c_naomi[a+1])	{
		
		temp=c_naomi[a];
		c_naomi[a]=c_naomi[a+1];
		c_naomi[a+1]=temp;
		a=-1;
		}
		
		
	}
	
	
	for (int a=0; a<amount; a++){
		
		if (c_ken[a]==0)
		continue;
		
		for (int b=0; b<amount; b++)
		{
			if(c_naomi[b]==0)
			continue;
			else if (c_naomi[b]>c_ken[a]){
				c_naomi[b]=c_ken[a]=0;
				wnaomi++;
				a=0;
				break;
				
			}
		}
		
		
	}
	
		outfile <<"Case #" << no  <<": " <<wnaomi <<" " << wken << endl;
		count--;
		no++;
		wken=0;
		wnaomi=0;

}while(count!=0);

}
