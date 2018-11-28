#include<iostream>
#include<iomanip>


using namespace std;

int main()
{
int T=0;
double eps=1e-7;
cin>>T;
cout.precision(10);
for(int i=0;i<T;i++)
{
double y=0,t1=0,t2=0;
double C=0,X=0,F=0; 
double lim=2;
cin>>C>>F>>X;
while(1)
{
t1=X/lim;
t2=C/lim+X/(F+lim);
if(t1<t2)
{
y+=t1;
break;
}
else
{
y+=(C/lim);
}
lim+=F;
}
cout<<"Case #"<<i+1<<": "<<y<<endl;
}
return 0;
}

