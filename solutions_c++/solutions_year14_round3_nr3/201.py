#include <iostream>
#include <vector>
#include <string>
#include <algorithm>



using namespace std;

const int MAXn = 25;
bool jadval[MAXn][MAXn];
int chap[MAXn];
int rast[MAXn];
int bala[MAXn];
int payin[MAXn];



void clr()
{
  for(int i=0;i<MAXn;i++)
    for(int j=0;j<MAXn;j++)
      jadval[i][j] = 0;
}


int t(int n,int m)
{
  int tedad = 0;
  for(int i=0;i<n;i++)
    {
      for(int j=0;j<m;j++)
	{
	  if(jadval[i][j] == 1)
	    tedad++;
	  else
	    {
	      if(bala[j]<=i && payin[j]>=i && rast[i]>=j && chap[i]<=j && bala[j]!= -1 && payin[j]!= -1 && chap[i]!= -1 && rast[i]!= -1)
		tedad++;
	    }
	}
    }
  return tedad;
}

void make(int n,int m)
{
  for(int i=0;i<n;i++)
    {
      chap[i] = -1;
      for(int j=0;j<m;j++)
	if(jadval[i][j] == 1)
	  {
	    chap[i] = j;
	    break;
	  }
    
      rast[i] = -1;
      for(int j=m-1;j>=0;j--)
	if(jadval[i][j] == 1)
	  {
	    rast[i] = j;
	    break;
	  }
    }
  for(int j=0;j<m;j++)
    {
      bala[j] = -1;
      for(int i=0;i<n;i++)
	{
	  if(jadval[i][j] == 1)
	    {
	      bala[j] = i;
	      break;
	    }
	}
      payin[j] = -1;
      for(int i=n-1;i>=0;i--)
	{
	  if(jadval[i][j] == 1)
	    {
	      payin[j] = i;
	      break;
	    }
	}
    }
}


int f(int n,int m,int k)
{
  int minimum = n*m;
  for(int i=0;i<(1<<(n*m));i++)
    {
      int  l=0;
      int tmp = i;
      for(int j=0;j<n;j++)
	{
	  for(int g=0;g<m;g++)
	    {
	      if(tmp%2)
		{
		  jadval[j][g] = 1;
		  l++;
		}
	      else
		jadval[j][g] = 0;
	      tmp/=2;
	    }
	}
      /*
      for(int j=0;j<n;j++)
	{
	  for(int g=0;g<m;g++)
	    cerr<<jadval[j][g];
	  cerr<<endl;
	}*/
      make(n,m);
      // cerr<<endl<<t(n,m)<<endl;
      //make(n,m);
      if(t(n,m)>=k && l<minimum)
	{
	  minimum = l;/*
	  for(int j=0;j<n;j++)
	    {
	      for(int g=0;g<m;g++)
		cerr<<jadval[j][g];
	      cerr<<endl;
	      }*/
	  // cerr<<l<<endl;
	}
      //  cerr<<i<<endl;
      // cerr<<"hre"<<endl;
    }
  return minimum ;
}

int main()
{
  ios::sync_with_stdio(false);
  int T;
  cin>>T;
  for(int I=1;I<=T;I++)
    {
      clr();
      int n,m,k;
      cin>>n>>m>>k;
      cout<<"Case #"<<I<<": "<<f(n,m,k)<<endl;
    }
  return 0;
}
