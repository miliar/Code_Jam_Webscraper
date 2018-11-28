#include<iostream>
#include<cstdio>
#include<iomanip>
using namespace std;
void cookie(double c, double f, double x,double k,int q)
{
 double z=0.0;
 double a,b;
 a=x/k;
 b=c/k+x/(k+f);
 while( a > b )
 {
  //cout<<"z="<<z<<" k="<<k<<" a="<<a<<" b="<<b<<"\n";
  z=z+c/k;
  k=k+f;
  a=x/k;
  b=c/k+x/(k+f);
  //cout<<"z="<<z<<" k="<<k<<" a="<<a<<" b="<<b<<"\n"<<"\n";
 }
 z=z+a;
 cout<<"Case #"<<q<<": ";
 cout<<std::fixed << std::setprecision(7)<<z<<"\n";
}
int main()
{
 freopen("ab.txt","r",stdin);
 freopen("cd1.txt","w",stdout);
 int t;
 double c,f,x;
 cin>>t;
 for(int i=1;i<=t;i++)
 {
  cin>>c;
  cin>>f;
  cin>>x;
  cookie(c,f,x,2.0,i);
 }
}
