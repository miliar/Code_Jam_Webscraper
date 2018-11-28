#include<iostream>
#include<cmath>
using namespace std;

bool ispal(int n)
{int th,h,t,o;
o = n%10;
t = (n%100)   /10;
h = (n%1000)  /100;
th=(n%10000) /1000;
if(th==0) {if(h==0) {if(t==0) return true;
			else if(t==o) return true;}
	   else if(h==o) return true;}
else if(th==o&&h==t) return true;
return false;
}

bool issqrt(int n)
{if(!ispal(n)) return false;
float orsq;
int sq;
orsq=sqrt(n);
sq=(int) orsq;
if(sq==orsq) if (ispal(sq)) return true;
return false;}

int gcint()
{int A,B,count=0;
cin>>A>>B;
for(A;A<=B;A++)
if(issqrt(A)) count++;
return count;}

int main()
{
int T;
cin>>T;
for(int mainc=1;mainc<=T;mainc++)
{cout<<"Case #"<<mainc<<": "<<gcint()<<'\n';}}
