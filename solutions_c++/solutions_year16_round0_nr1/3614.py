#include<iostream>
#include<fstream>
#include<cstdio>
using namespace std;


int main()
{

fstream myfile;
int T,N[200],r[10],i,j,s,t,q,o;

freopen("temp.in", "r", stdin);

freopen("temp.out", "w", stdout);

cin>>T;
for(i=1;i<=T;i++)
cin>>N[i];

for(i=1;i<=T;i++)
{cout<<"Case #"<<i<<":"<<" ";
q=N[i];
for(s=0;s<=9;s++)
r[s]=0;

for(j=1;j<2147483647;j++)
{

t=q*j;
while(t>0)
{
s=t%10;
r[s]+=1;
t=t/10;
}


if(r[0]>0 && r[1]>0 && r[2]>0 && r[3]>0 && r[4]>0 && r[5]>0 && r[6]>0 && r[7]>0 && r[8]>0 && r[9]>0)
break;
}


if(j==2147483647)
cout<<"INSOMNIA"<<endl;
else
cout<<q*j<<endl;

/*
for(s=0;s<=9;s++)
r[s]=0;
*/
}
return 0;
}
