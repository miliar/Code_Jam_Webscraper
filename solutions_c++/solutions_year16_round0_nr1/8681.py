#include<iostream>
using namespace std;
int main()
{
int test,c=1;
cin>>test;
while(test--)
{
int z,x,i=2,array0[10]={10,10,10,10,10,10,10,10,10,10},q,array1[10]={0,1,2,3,4,5,6,7,8,9},a,w=0;
{
cin>>a;
if (a==0)
{
 cout<<"Case #"<<c<<": "<<"Insomnia"<<endl;
}
else{
z=a;
while(w!=10)
 {if(array0[0]!=array1[0]|| array0[1]!=array1[1]|| array0[2]!=array1[2]|| array0[3]!=array1[3]|| array0[4]!=array1[4]|| array0[5]!=array1[5]|| array0[6]!=array1[6]|| array0[7]!=array1[7]|| array0[8]!=array1[8]|| array0[9]!=array1[9])
{
x=z;
while(x!=0)
{
q=x%10;
array0[q]=q;
x/=10;
}
z=i*a;
i++;
}
else
{
 w=10;
}
}
cout<<"Case #"<<c<<": "<<z-a<<endl;
}
c++;
}
}
}

