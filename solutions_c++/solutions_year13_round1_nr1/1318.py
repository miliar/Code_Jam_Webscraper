#include<iostream>

using namespace std;


long area(long r)
{
return (2*r+1);
}

int main()
{
int T;
cin>>T;
for(int k=1;k<=T;k++)
{
long r,t;

cin>>r>>t;
cout<<"Case #"<<k<<": ";

int i=0;

long a=area(r);
while(t-a>=0)
{
t=t-a;
//cout<<"t is "<<t<<endl;
i++;
a=a+4;
}

cout<<i<<endl;
}

}