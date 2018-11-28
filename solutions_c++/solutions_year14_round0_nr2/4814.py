#include<iostream>
#include<string.h>
#include<fstream>
#include<sstream>
#include<stdlib.h>
using namespace std;
char ch;
double cal(double c,double f,double x,double t,double r)
{
     double ti,tf;
     tf=x/r;
     ti=c/r;
     r+=f;
     if(ti+x/r>tf)
        return t+tf;
     else
        return cal(c,f,x,ti+t,r);
}
int main()
{

  char ch;

  int n;
  double c,f,x;
  string s;
  ifstream fin;
  ofstream fot;
  fin.open("gg.in");
  fot.open("ans.out");
  getline(fin,s);
  stringstream(s) >> n;
  fot.precision(7);
for(int i=0;i<n;i++)
{
 fot<<"Case #"<<i+1<<": ";
 getline(fin,s,' ');
 stringstream(s) >> c;
 getline(fin,s,' ');
 stringstream(s) >> f;
 getline(fin,s);
 stringstream(s) >> x;

  fot<<fixed<<cal(c,f,x,0,2)<<endl;
 // cout<<c<<" c "<<f<<" f "<<x<<" x "<<endl;
}

  fin.close();
  fot.close();

}
