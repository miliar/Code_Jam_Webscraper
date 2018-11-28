#include <iostream>
#include <fstream>
#include <cmath>
#include <math.h>

using namespace std;
int palindrome(int);
int main()
{
     ofstream file1("output.txt");
    ifstream file("C-small-attempt0.in");
    int a,b,n;
    file>>n;
    for(int s=1;s<=n;s++)
    {file>>a;
    file>>b;
    int c,d;
    int q=0;
    c=sqrt(a);
    double c1=sqrt(a)-c;
    d=sqrt(b);
    if(c1>0)
    {c=c+1;}
    for(int i=c;i<=d;i++)
    {if(palindrome(i)==1&&palindrome(i*i)==1)
      {q++;cout<<"I"<<i<<"\n";
      }}
      file1<<"Case #"<<s<<": "<<q<<"\n";
    }
}
int palindrome(int m)
{int g,h;
g=h=m;
int s=0;
while(g!=0)
{g=g/10;
s++;}
g=0;
while(s!=0)
{g=g+((m%10)*pow(10.0,s-1));
m=m/10;
s--;}
if(g==h)
 {return 1;}
 else{return 0;}   }
