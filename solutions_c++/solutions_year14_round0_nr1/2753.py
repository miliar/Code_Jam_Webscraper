#include "math.h"
#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <conio.h>
#include <iomanip>
using namespace std;



int main()
{
	
	int a=0,i=0;
	ifstream in("Input.txt");	
    if (!in) {
    cout << "Cannot open file.\n";
    return 0;
     }
	ofstream out("Output.txt");
    in>>a;
	
	for(i=1;i<=a;i++)
	{
		int c=0,b=0,j=0,k=0,s1[4][4],s2[4][4],d=0,w=0;

		in>>b;

		for(k=0;k<4;k++)
			for(j=0;j<4;j++)
				in>>s1[k][j];
		in>>c;

		for(k=0;k<4;k++)
			for(j=0;j<4;j++)
				in>>s2[k][j];

		for(k=0;k<4;k++)
			for(j=0;j<4;j++)
			  if(s1[b-1][k]==s2[c-1][j])
			  {
				  d=s1[b-1][k];
				  w=w+1;
			  }
        if(w==0)		
			out<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		
		if(w==1)
		    out<<"Case #"<<i<<": "<<d<<endl;
		
		if(w>1)
		    out<<"Case #"<<i<<": Bad magician!"<<endl;


	}
    out.close();
	in.close();

 return 0;
}