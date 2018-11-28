#include<iostream>
#include<iomanip>
#include<fstream>
#include<string.h>
#include<stdlib.h>
#include<math.h>

using namespace std;

double naomi[2000],ken[2000];
double naomi2[2000],ken2[2000];
int N;

double move_k_n(double n_move)
{
  double smallest=1;
  int i,p,c=0;

  for(i=0;i<N;i++)
    {
      if((ken[i]<smallest)&&(ken[i]>n_move))
	{
	  smallest=ken[i];
	  p=i;
	  c++;
	}
    }

  if(c==0)
    {
      for(i=0;i<N;i++)
	{
	  if(ken[i]<smallest)
	    {
	      smallest=ken[i];
	      p=i;
	    }
	}
    }
  ken[p]=1;
  return smallest;
}

double move_k_d(double n_move)
{
  double smallest=1;
  int i,p,c=0;

  for(i=0;i<N;i++)
    {
      if((ken2[i]<smallest)&&(ken2[i]>n_move))
	{
	  smallest=ken2[i];
	  p=i;
	  c++;
	}
    }

  if(c==0)
    {
      for(i=0;i<N;i++)
	{
	  if(ken2[i]<smallest)
	    {
	      smallest=ken2[i];
	      p=i;
	    }
	}
    }
  ken2[p]=1;
  return smallest;

}

double move_n_n()
{
  double smallest=1;
  int i,p;

  for(i=0;i<N;i++)
    {
      if(naomi[i]<smallest)
	{
	  smallest=naomi[i];
	  p=i;
	}
    }

  naomi[p]=1;
  return smallest;

}

double move_n_d()
{

  double n_smallest=1,k_smallest=1,k_largest=0;
  double t=0.00000001;
  int i,p=0;

  for(i=0;i<N;i++)
    {
      if(naomi2[i]<n_smallest)
	{
	  n_smallest=naomi2[i];
	  p=i;
	}
    }

  for(i=0;i<N;i++)
    {
      if(ken2[i]<k_smallest)
	{
	  k_smallest=ken2[i];
	}
    }

  for(i=0;i<N;i++)
    {
      if((ken2[i]>k_largest)&&(ken2[i]!=1))
	{
	  k_largest=ken2[i];
	}
    }

  if(n_smallest>k_smallest)
    {
      naomi2[p]=1;
      return k_largest+t;
    }

  if(n_smallest<k_smallest)
    {
      naomi2[p]=1;
      return k_largest-t;
    }

}



int match(double n,double k)
{
  if(n>k)
    return 1;
  else if(n<k)
    return 0;
  else if(n==k)
    return 2;

}

int main()
{

  ifstream fin;
  ofstream fout;
  fin.open("D-large.in");
  fout.open("output3");

  int T;
  int i,j,k;
  int dWin,nWin;
 
  double t1,t2;

  fin>>T;

  for(i=0;i<T;i++)
    {

      fin>>N;

      for(j=0;j<N;j++)
	{
	  fin>>naomi[j];
	  naomi2[j]=naomi[j];
	}

      for(j=0;j<N;j++)
	{
	  fin>>ken[j];
	  ken2[j]=ken[j];
	}

      dWin=0;
      nWin=0;

      for(j=0;j<N;j++)
	{
	  t1=move_n_d();
	  t2=move_k_d(t1);
	  dWin+=match(t1,t2);

	  t1=move_n_n();
	  t2=move_k_n(t1);
	  nWin+=match(t1,t2);
	}

      fout<<"Case #"<<i+1<<": "<<dWin<<" "<<nWin<<"\n";

    }

}
