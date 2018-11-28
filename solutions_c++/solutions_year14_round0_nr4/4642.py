#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>
using namespace std;
char ch;

int main()
{

  char ch;

  int t,n,ind,tempi,y,ys,z,zs;
  double l,tempd,a[2][2005];
  string s;
  ifstream fin;
  ofstream fot;
  fin.open("gg.in");
  fot.open("ans.out");
  getline(fin,s);
  stringstream(s) >> t;
  fot.precision(7);
for(int i=0;i<t;i++)
{
 fot<<"Case #"<<i+1<<": ";

 getline(fin,s);
 stringstream(s) >> n;
 for(int j=1;j<n;j++)
 {
  getline(fin,s,' ');
  stringstream(s) >> a[0][j-1];
  a[1][j-1]=1;
 }
 getline(fin,s);
 stringstream(s) >> a[0][n-1];
 a[1][n-1]=1;
 for(int j=1;j<n;j++)
 {
  getline(fin,s,' ');
  stringstream(s) >> a[0][n+j-1];
  a[1][n+j-1]=0;
 }
 getline(fin,s);
 stringstream(s) >> a[0][2*n-1];
 a[1][2*n-1]=0;
    for(int j=0;j<2*n;j++)
    {
        l=a[0][j];
        ind=j;
      for(int v=j+1;v<2*n;v++)
     {
        if(a[0][v]>l)
        {
         l=a[0][v];
         ind=v;
        }
     }
     tempd=a[0][ind];
     a[0][ind]=a[0][j];
     a[0][j]=tempd;

     tempi=a[1][ind];
     a[1][ind]=a[1][j];
     a[1][j]=tempi;

    }
   y=0,ys=0;
   for(int j=0;j<2*n;j++)
   {
      if(ys>0)
          if(a[1][j]==0)
            {
                ys--;
                y++;
            }
      if(a[1][j]==1)
        ys++;
   }
   z=0,zs=0;
   for(int j=0;j<2*n;j++)
   {
      if(zs>0)
          if(a[1][j]==1)
            {
                zs--;
                z++;
            }
      if(a[1][j]==0)
        zs++;
   }

   fot<<y<<" "<<n-z<<endl;

}

  fin.close();
  fot.close();

}
