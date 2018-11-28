
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <math.h>
#include <cmath>
#include <algorithm>


using namespace std;


int main(int argc, char **argv)
{
	
	int T;
	int X,R,C;
	ifstream infile;
	ofstream outfile;
	infile.open("D-small-attempt0.in",ios::in);
	outfile.open("d.out",ios::out);
	
	if(!infile.is_open()) {cout<<"File not found"; cin>>T;return 0;}
	infile>>T;
for (int t=1;t<=T;t++){
	infile>>X>>R>>C;
	if(X==1) outfile<<"Case #"<<t<< ": GABRIEL\n";
	if(X==2) 
		{
			if((R%2==0) || (C%2==0))
			outfile<<"Case #"<<t<< ": GABRIEL\n";
			else
			outfile<<"Case #"<<t<< ": RICHARD\n";
		}
		if(X==3) 
		{
			if((R==2)&(C==3) ||(R==3)&(C==3) ||(R==3)&(C==2) ||(R==4)&(C==3)||(R==3)&(C==4))
			outfile<<"Case #"<<t<< ": GABRIEL\n";
			else
			outfile<<"Case #"<<t<< ": RICHARD\n";
		}
			if(X==4) 
		{
			if((R==3)&(C==4) ||(R==4)&(C==3) ||(R==4)&(C==4))
			outfile<<"Case #"<<t<< ": GABRIEL\n";
			else
			outfile<<"Case #"<<t<< ": RICHARD\n";
		}
	
		
		
	

	
}
	infile.close();
	outfile.close();
	
}


