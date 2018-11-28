#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;
int main()
{
 ifstream fin("b1.txt");
 ofstream fout("output.txt");
 int n,k=0;
 double i=0,t1=0,t2=0,j=0,s=2,g=0,t=0,m=0;
 double c,f,x;
 fin>>n;
for(k=0;k<n;k++)
{fin>>c;
fin>>f;
fin>>x;
s=2;
t=0;
while(m!=x)
{
 if(m==x)
 break;
 i=x/s;
 t1=i;
 j=c/s;
 s+=f;
 g=x/s;
 t2=j+g;
 if(t1<t2)
 {
    t+=t1;
    break;
 }
 else
 {t+=j;
  }
}
 fout<<"Case #"<<k+1<<": "<<setprecision(12)<<t<<"\n";
}
return  0;
}
