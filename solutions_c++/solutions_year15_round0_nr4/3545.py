#include <iostream>
#include <stdio.h>
#include <assert.h>
#include <vector>
#include <math.h>
using namespace std;
int main(){
int t=1;
cin>>t;
assert(t>=1 && t<=64);
int l=1;
while(t!=0)
{
t--;
int X=1,R=1,C=1;
cin>>X>>R>>C;
assert(X>=1 && X<=4);
assert(R>=1 && R<=4);
assert(C>=1 && C<=4);
if (X==1)
cout<<"Case #"<<l<<": GABRIEL\n";

if(X==4 && (R+C)>=7)
{cout<<"Case #"<<l<<": GABRIEL\n";}
else
if(X==4)
{cout<<"Case #"<<l<<": RICHARD\n";}

if(X==2 && (R*C)%2!=0)
{cout<<"Case #"<<l<<": RICHARD\n";}
else
if (X==2)
{cout<<"Case #"<<l<<": GABRIEL\n";}

if(X==3 && (R*C)%3==0 && R*C!=3)
{cout<<"Case #"<<l<<": GABRIEL\n";}
else if(X==3)
{cout<<"Case #"<<l<<": RICHARD\n";}
l++;
}
return 0;
}
