#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <utility> 
#include <queue>
#include <map>

#define Max_n 100

#define ll long long

using namespace std;

int r,t,i,k,j,n=6,m,maxh,minh,bres,tres,l,nx,ny,tek,nw,p,w,smax,res;

char c;

string x,y;

int s[31234],res2[31234];

bool cmp_sorth(int i, int j)
{
	return 1;//(h[i]>h[j]);
}


bool cmp_sorthw(int i, int j)
{
	return 1;// (h[i]-w[i]<h[j]-w[j]);
}

int main()
{
  if (1)
  {
	  freopen("input.txt","r",stdin);
	  freopen("output.txt","w",stdout);
  }
 cin >> t;
 for (int ti=0;ti<t;ti++)
 {
	  cin >> smax;
	  for (int i=0;i<=smax;i++)
	  {
		  cin >> c;
		  s[i]=c-'0';
	  }
      res=0;j=0;
	  for (i=0;i<=smax;i++)
	  {
		  if (j<i)
		  {
			  res+=i-j;
			  j=i;
		  }
		  j+=s[i];
	  }
	  cout << "Case #"<<ti+1<<": "<<res<<endl;
 }
 return 0;
}

