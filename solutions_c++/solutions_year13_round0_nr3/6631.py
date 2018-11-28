#include<fstream>
#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{

ifstream in,sq;
ofstream ou;
int n,m=1,k,a,b,i=0,j=0;
int arr[21];
/*
    {1,4,9,121,484,10201,12321,14641,40804,
    44944,1002001,1234321,4008004,100020001,
    102030201,104060401,121242121,123454321,
    125686521,400080004,404090404};
*/
in.open("A.in",ios::in);
if(!in)
{
cout<<"input File error";
return 0;
}
sq.open("square1.in",ios::in);
if(!sq)
{
cout<<"sq File error";
return 0;
}

ou.open("A.out",ios::out);
if(!ou)
{
cout<<"ouput File error";
return 0;
}
while(i<21)
{
    sq>>arr[i];
    i++;
}

in>>n;
cout<<n;
while(m<=n)
{
ou<<"Case #"<<m<<": ";
m++;

in>>a;
in>>b;
j=0;
while(a>arr[j])
{
    j++;
}
k=j;
while(b>=arr[k])
{
    k++;
}
ou<<(k-j)<<'\n';

}
sq.close();
in.close();
ou.close();
return 0;
}
