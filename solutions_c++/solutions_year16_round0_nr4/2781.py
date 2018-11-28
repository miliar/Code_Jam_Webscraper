#include<iostream>
#include<bits/stdc++.h> 
#include<fstream>
#include<set>
#include<map>
#define up(j,n,i) for(i=j;i<n;i++)
using namespace std;
typedef long long int lld;
lld binpow(lld base,lld pow)
{
if(pow>0)
{
if(pow%2==1)
{
pow--;
return(base*binpow(base,pow/2)*binpow(base,pow/2));
}
else
return(binpow(base,pow/2)*binpow(base,pow/2));
}
else
return 1;
}
int main()
{
lld t,tk=0;
fstream I,O;
I.open("in.in",ios::in);
O.open("out.txt",ios::out);
I>>t;
tk=1;
while(tk<=t)
{
O<<"Case #"<<tk<<": ";
lld k,c,s;
I>>k>>c>>s;
lld ki,i;
ki=binpow(k,c-1);
up(0,k,i)
O<<(i*ki+1)<<' ';
O<<endl;

tk++;
}
return 0;
}
