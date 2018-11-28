#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>
#include<math.h>

using namespace std;
int  *a;
int palin(int n)
{

    int r,rev=0,b=n;
   while(n!=0)
     {
      r=n%10;
      n=n/10;
      rev=rev*10+r;
     }

     if (b==rev)
     return 1;
     else
        return 0;
}
int main()
{

  char ch;
    int n,i,q,t,ne,ns;
  string s;
  ifstream fin;
  ofstream fot,fct;
  fin.open("gg.in");
  fot.open("ans.out");
 // fct.open("wtf.out");
 getline(fin,s);
  stringstream(s) >> n;

for(int i=0;i<n;i++)
{
    q=0;
    fot<<"Case #"<<i+1<<": ";
    getline(fin,s,' ');
  stringstream(s) >>ns;
  getline(fin,s);
  stringstream(s) >>ne;
for (int j=ns;j<ne+1;j++)
  {

     if(palin(j))
     {

         t=sqrt(j);
         if(t*t==j)
         {

     if(palin(t))
     {
         q++;
     }
         }
     }

  }
  fot<<q<<endl;
}

  fin.close();
  fot.close();

}
