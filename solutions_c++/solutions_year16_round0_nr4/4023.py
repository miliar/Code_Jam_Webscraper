#include<iostream>
#include<fstream>
#include<math.h>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
  int i,j,T,s;
  double m,k,c,temp;

  fin.open("input.in");
  fout.open("output-fin.txt");

  fin>>T;

  for(i=0;i<T;i++)
    {
      fin>>k>>c>>s;
      m=k/c;

      /*
      if( (k/2)!=floor(k/2) )
	{m=floor(m);}
      else
	{m=ceil(m);}

      //cout<<m<<"\n";

      fout<<"Case #"<<i+1<<":";

      if(m>s)
	{
	  fout<<" IMPOSSIBLE\n";
	  continue;
	}

      if(k==1)
	{
	  fout<<" 1";
	}
      else if(k!=1&&c==1)
	{
	  for(j=0;j<k;j++)
	    {fout<<" "<<j+1;}
	}
      else
	{
	  for(j=0;j<m;j++)
	    {
	      temp=pow(k,(c-1))*j*c;
	      //cout<<temp<<"\n";
	      temp+=2*(j+1);
	      //cout<<temp<<"\n";
	      fout<<" "<<temp;
	    }
	  if( (k/2)!=floor(k/2) )
	    {
	      temp=pow(k,(c-1))*j*c;
	      temp+=(k-1);
	      fout<<" "<<temp;
	    }
	}
      */
      fout<<"Case #"<<i+1<<":";
      for(j=1;j<=k;j++)
	{fout<<" "<<j;}

      fout<<"\n";
    }

return 0;
}
