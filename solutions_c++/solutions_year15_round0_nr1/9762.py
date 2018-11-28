#include<iostream>
using namespace std;
int main()
{
int i,j,t,smax,frnd,total;
string ary;
cin>>t;
for(i=0; i<t; i++)
{
frnd=0;
total=0;
cin>>smax;
cin>>ary;
for(j=0; ary[j]!='\0'; j++)
{
if(total<j && ary[j]!=48)
{
frnd=frnd+(j-total);
total=total+frnd;
}
total=total+(ary[j]-48);
}
cout<<"Case #"<<i+1<<": "<<frnd<<endl;
}
return 0;
}
