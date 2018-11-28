#include <iostream>
#include <cstdlib>
#include <fstream>
using namespace std;
int main()
{
    ifstream in("input.txt");
    ofstream of("output.txt");
    int qwe;
    in>>qwe;
    int num;
    for(int qwerty=0;qwerty<qwe;qwerty++)
    {
      int X;
      int R;
      int C;
      in>>X;
      in>>R;
      in>>C;
      if(X==1)
      of<<"Case #"<<qwerty+1<<": "<<"GABRIEL"<<"\n";
      if(X==2)
         {
         	if((R*C)%2==0)
         	  of<<"Case #"<<qwerty+1<<": "<<"GABRIEL"<<"\n";
         	else
         	  of<<"Case #"<<qwerty+1<<": "<<"RICHARD"<<"\n";
		 }
	  if(X==3)
	    {
	  		if(R==1 or C==1)
	  		  of<<"Case #"<<qwerty+1<<": "<<"RICHARD"<<"\n";
	  		else
			  if((R*C)%3!=0)
	  		   of<<"Case #"<<qwerty+1<<": "<<"RICHARD"<<"\n";
	  	      else
	  	       of<<"Case #"<<qwerty+1<<": "<<"GABRIEL"<<"\n";
	  		 
		}
	
		if(X==4)
		  {
		  	 if(R==4 and C==4)
		  	   of<<"Case #"<<qwerty+1<<": "<<"GABRIEL"<<"\n";
		  	else 
		  	   if(R*C==12)
		  	     of<<"Case #"<<qwerty+1<<": "<<"GABRIEL"<<"\n";
		  	else
			   of<<"Case #"<<qwerty+1<<": "<<"RICHARD"<<"\n"; 
		  }
    } 
}
