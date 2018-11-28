#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<sstream>
#include<complex.h>
#include<fstream>
#include<stdlib.h>
#include<math.h>
#include<algorithm>
using namespace std;
int main()
{
string s;
unsigned long long t;
unsigned long long r;
unsigned long long p;
getline(cin,s);
istringstream instr(s);
instr>>t;
for(unsigned long long i=0;i<t;i++)
{
getline(cin,s);
istringstream instr1(s);
instr1>>r>>p;
unsigned long long sum=0;
unsigned long long sum1=1+(2*r);
unsigned long long rng=0;
unsigned long long g=1;
while(1)
{
//cout<<sum<<"\n";
if(p<sum1)
break;
rng++;
p-=sum1;
//cout<<sum<<"\n";
sum1+=4;
}
cout<<"Case #"<<i+1<<": "<<rng<<"\n";
}
return 0;
}

