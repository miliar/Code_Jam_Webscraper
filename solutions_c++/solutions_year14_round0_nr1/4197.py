#include<iostream>
#include<fstream>
#include<string.h>
#include<stdlib.h>

using namespace std;

int main()
{

  int T,a[2],sq1[4][4],sq2[4][4];

  int i,j,k,c,sol;

  ifstream fin;
  ofstream fout;
  fin.open("A-small-attempt1.in");
  fout.open("output1");

  fin>>T;


  for(i=0;i<T;i++)
    {

      fin>>a[0];
      for(j=0;j<4;j++)
	{
	  for(k=0;k<4;k++)
	    {
	      fin>>sq1[j][k];
	    }
	}

      fin>>a[1];
      for(j=0;j<4;j++)
	{
	  for(k=0;k<4;k++)
	    {
	      fin>>sq2[j][k];
	    }
	}

      a[0]--;
      a[1]--;

      c=0;

      for(j=0;j<4;j++)
	{
	  for(k=0;k<4;k++)
	    {
	      if(sq1[a[0]][j]==sq2[a[1]][k])
		{
		  c++;
		  sol=sq1[a[0]][j];
		}
	    }
	}
      switch(c)
	{
	case 0:fout<<"Case #"<<i+1<<": Volunteer cheated!\n";break;
	case 1:fout<<"Case #"<<i+1<<": "<<sol<<"\n";break;
	case 2:fout<<"Case #"<<i+1<<": Bad magician!\n";break;
	case 3:fout<<"Case #"<<i+1<<": Bad magician!\n";break;
	case 4:fout<<"Case #"<<i+1<<": Bad magician!\n";break;
	default:fout<<"Case #"<<i+1<<": Bad magician!\n";break;
	}
    }


}
