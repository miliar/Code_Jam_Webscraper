#include<iostream>
#include<iomanip>
#include<fstream>
#include<string.h>
#include<stdlib.h>
#include<math.h>

using namespace std;

int main()
{

  ifstream fin;
  ofstream fout;
  fin.open("D-small-attempt0.in");
  fout.open("output2");

  fout.precision(7);

  int T,i,x,r,c,sol;

  fin>>T;

  for(i=0;i<T;i++)
    {

      fin>>x>>r>>c;
 
      //1 For picker
      //2 For placer

      if(x==0)
	{sol=1;}

      else if(x==1)
	{
	  if(r==1&&c==1)
	    {sol=2;}
	  else if(r==1&&c==2)
	    {sol=2;}
	  else if(r==1&&c==3)
	    {sol=2;}
	  else if(r==1&&c==4)
	    {sol=2;}
	    //////////
	  else if(r==2&&c==1)
	    {sol=2;}
	  else if(r==2&&c==2)
	    {sol=2;}
	  else if(r==2&&c==3)
	    {sol=2;}
	  else if(r==2&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==3&&c==1)
	    {sol=2;}
	  else if(r==3&&c==2)
	    {sol=2;}
	  else if(r==3&&c==3)
	    {sol=2;}
	  else if(r==3&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==4&&c==1)
	    {sol=2;}
	  else if(r==4&&c==2)
	    {sol=2;}
	  else if(r==4&&c==3)
	    {sol=2;}
	  else if(r==4&&c==4)
	    {sol=2;}
	  //////////
	  else
	    {sol=0;}
	}

      else if(x==2)
	{
	  if(r==1&&c==1)
	    {sol=1;}
	  else if(r==1&&c==2)
	    {sol=2;}
	  else if(r==1&&c==3)
	    {sol=1;}
	  else if(r==1&&c==4)
	    {sol=2;}
	    //////////
	  else if(r==2&&c==1)
	    {sol=2;}
	  else if(r==2&&c==2)
	    {sol=2;}
	  else if(r==2&&c==3)
	    {sol=2;}
	  else if(r==2&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==3&&c==1)
	    {sol=1;}
	  else if(r==3&&c==2)
	    {sol=2;}
	  else if(r==3&&c==3)
	    {sol=1;}
	  else if(r==3&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==4&&c==1)
	    {sol=2;}
	  else if(r==4&&c==2)
	    {sol=2;}
	  else if(r==4&&c==3)
	    {sol=2;}
	  else if(r==4&&c==4)
	    {sol=2;}
	  //////////
	  else
	    {sol=0;}
	}


      else if(x==3)
	{
	  if(r==1&&c==1)
	    {sol=1;}
	  else if(r==1&&c==2)
	    {sol=1;}
	  else if(r==1&&c==3)
	    {sol=1;}
	  else if(r==1&&c==4)
	    {sol=1;}
	    //////////
	  else if(r==2&&c==1)
	    {sol=1;}
	  else if(r==2&&c==2)
	    {sol=1;}
	  else if(r==2&&c==3)
	    {sol=2;}
	  else if(r==2&&c==4)
	    {sol=1;}
	  //////////
	  else if(r==3&&c==1)
	    {sol=1;}
	  else if(r==3&&c==2)
	    {sol=2;}
	  else if(r==3&&c==3)
	    {sol=2;}
	  else if(r==3&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==4&&c==1)
	    {sol=1;}
	  else if(r==4&&c==2)
	    {sol=1;}
	  else if(r==4&&c==3)
	    {sol=2;}
	  else if(r==4&&c==4)
	    {sol=1;}
	  //////////
	  else
	    {sol=0;}
	}

      else if(x==4)
	{
	  if(r==1&&c==1)
	    {sol=1;}
	  else if(r==1&&c==2)
	    {sol=1;}
	  else if(r==1&&c==3)
	    {sol=1;}
	  else if(r==1&&c==4)
	    {sol=1;}
	    //////////
	  else if(r==2&&c==1)
	    {sol=1;}
	  else if(r==2&&c==2)
	    {sol=1;}
	  else if(r==2&&c==3)
	    {sol=1;}
	  else if(r==2&&c==4)
	    {sol=1;}
	  //////////
	  else if(r==3&&c==1)
	    {sol=1;}
	  else if(r==3&&c==2)
	    {sol=1;}
	  else if(r==3&&c==3)
	    {sol=1;}
	  else if(r==3&&c==4)
	    {sol=2;}
	  //////////
	  else if(r==4&&c==1)
	    {sol=1;}
	  else if(r==4&&c==2)
	    {sol=1;}
	  else if(r==4&&c==3)
	    {sol=2;}
	  else if(r==4&&c==4)
	    {sol=2;}
	  //////////
	  else
	    {sol=0;}
	}
      else
	{sol=0;}


      if(sol==1)
	{
	  fout<<"Case #"<<i+1<<": RICHARD\n";
	}
      else if(sol==2)
	{
	  fout<<"Case #"<<i+1<<": GABRIEL\n";
	}
    }
  
}
