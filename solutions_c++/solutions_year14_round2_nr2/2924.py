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
  fin.open("B-small-attempt1.in");
  fout.open("output2");

  int T;
  int a,b,k,ci;
  float count;
  int ac,bc;

  int ab[50],bb[50],cb[50],la,lb,lc;

  fin>>T;

  int i,j,m,al,bl;


  for(i=0;i<T;i++)
    {

      fin>>a>>b>>k;
      ac=a;
      bc=b;

      //cout<<ac<<" "<<bc<<"\n";


      count=0;

      for(al=0;al<ac;al++)
	{

	  for(bl=0;bl<bc;bl++)
	    {

	      la=0;
	      lb=0;
	      lc=0;
	      ci=0;
	      m=1;

	      a=al;
	      b=bl;

	      for(j=0;j<10;j++) //NOT VALID FOR LARGE
		{
		  ab[j]=0;
		  bb[j]=0;
		  cb[j]=0;
		}
	      
	      for(j=0;a!=0;j++)
		{
		  ab[j]=a%2;
		  a/=2;
		  la++;
		}
	      ab[la]=0;	      

	      for(j=0;b!=0;j++)
		{
		  bb[j]=b%2;
		  b/=2;
		  lb++;
		}
	      bb[lb]=0;	      

	      lc=(la>lb)?la:lb;
	  
	      //cout<<la<<" "<<lb<<" "<<lc<<"\n";
    
	      for(j=0;j<lc;j++)
		{
		  if((ab[j]==1)&&(bb[j]==1))
		    {cb[j]=1;}
		  else
		    {cb[j]=0;}
		  //cout<<cb[j];
		}
	      //cout<<"\n";	 
     
	      for(j=0;j<lc;j++)
		{
		  ci+=(cb[j]*m);
		  m*=2;
		}
	      //cout<<ci<<" ";
	      
	      if(ci<k)
		{count++;}
	    }
	}


      fout<<"Case #"<<i+1<<": "<<count<<"\n";
      
    }

}
