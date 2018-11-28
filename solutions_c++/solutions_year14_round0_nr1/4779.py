#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>

using namespace std;
int main()
{

  char ch;

  int n,ro,rt,c[4],f[4],m,nu;
  string s;
  ifstream fin;
  ofstream fot;
  fin.open("h.in");
  fot.open("ans.out");
  getline(fin,s);
  stringstream(s) >> n;

for(int i=0;i<n;i++)
{
 fot<<"Case #"<<i+1<<": ";
 getline(fin,s);
  stringstream(s) >> ro;
 for(int j=1;j<ro;j++)
  getline(fin,s);
  getline(fin,s,' ');
  stringstream(s) >> c[0];
  getline(fin,s,' ');
  stringstream(s) >> c[1];
  getline(fin,s,' ');
  stringstream(s) >> c[2];
  getline(fin,s);
  stringstream(s) >> c[3];
  for(int j=ro;j<4;j++)
  getline(fin,s);
  getline(fin,s);
  stringstream(s) >> rt;
 for(int j=1;j<rt;j++)
  getline(fin,s);
  getline(fin,s,' ');
  stringstream(s) >> f[0];
  getline(fin,s,' ');
  stringstream(s) >> f[1];
  getline(fin,s,' ');
  stringstream(s) >> f[2];
  getline(fin,s);
  stringstream(s) >> f[3];
  for(int j=rt;j<4;j++)
  getline(fin,s);
  m=0;
  for(int j=0;j<4;j++)
  {
   for(int k=0;k<4;k++)
   {
      if(f[j]==c[k])
      {
        m++;
        nu=f[j];
      }
   }
  }
  if(m==0)
  fot<<"Volunteer cheated!";
  else if(m==1)
  fot<<nu;
  else
  fot<<"Bad magician!";
  fot<<endl;
}

  fin.close();
  fot.close();

}
