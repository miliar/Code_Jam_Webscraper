/*
 *  A.cpp
 *  
 *
 *  Created by Sushruth Muralidharan on 12/04/14.
 *  All rights reserved.
 *
 */
#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{    
	int ts,k;
	double c,f,x,f1,x1,t;
	fstream fin,fout;
	fin.open("./B-large.in",ios::in);
	fout.open("./Ao.txt",ios::out);
	fin>>ts;
	for(k=0;k<ts;k++)
	{ fin>>c>>f>>x;
		t=0;x1=0;f1=2;
		while(1)
		{   if(x1>=x){t+= ((x-x1)/f1);break;}
			if(x1>=c)
			{if((x-x1)/f1 >((x-(x1-c))/(f1+f)))
			{f1+=f;x1-=c;}
			 else 
			 {t+=(x-x1)/f1;x1=x;
			 }
			}
			
			else 
			{t +=(c-x1)/f1;
				x1+=c;
			}
					}
		
		fout<<"Case #"<<k+1<<": "<<setprecision(10)<<t<<endl;
	
	}
	
}


