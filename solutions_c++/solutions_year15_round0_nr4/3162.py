#include<fstream>
#include<iostream>
using namespace std;
//#define fin cin
//#define fout cout
int main()
{
 ifstream fin("D-small-attempt0.in");
 ofstream fout("out.out");

 int t;
 int x,r,c;
 int ans;
 fin>>t;
 for(int z=0;z<t;z++)
 {
  fout<<"Case #"<<z+1<<": ";
  fin>>x>>r>>c;
  ans=x*(x-1);
  if((r*c)%x==0&&(r*c)>=ans)
   fout<<"GABRIEL"<<endl;
  else 
   fout<<"RICHARD"<<endl;
 }
}

 
 

