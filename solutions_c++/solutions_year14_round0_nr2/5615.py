#include<iostream>
#include<stdio.h>
#include<conio.h>
#include<iomanip.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("cookies-large.out","w",stdout);
double n,c,f,x=2,X,e=1,i,j,t=0;
cin>>n;
while(e<=n)
{
t=0;
x=2;
cin>>c;
cin>>f;
cin>>X;
while(t+(X/x)>t+(c/x)+(X/(x+f)))
{
   t=t+c/x;
   x=x+f;
}                             
t=t+X/x;
cout<<"case #"<<e<<": ";
cout<<fixed<<setprecision(7)<<t<<endl;
cout<<resetiosflags(ios::fixed);

e++;
}
getch();
return 0;
}
