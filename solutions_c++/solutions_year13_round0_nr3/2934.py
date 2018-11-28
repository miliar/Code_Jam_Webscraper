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
bool is_Pel(unsigned long long a)
{
string result="";
stringstream ss;
ss<<a;
string s=ss.str();
for(int i=0;i<s.size();i++)
result=s[i]+result;
if(s==result)
return 1;
else
return 0;
}
bool is_Perf(unsigned long long a)
{
double b=sqrt(a);
unsigned long long c=sqrt(a);
if((double)c==b)
return 1;
else return 0;
}
int main()
{
ifstream file;
ofstream file1;
file.open("inp.txt");
file1.open("out.txt");
int t;
string s;
getline(file,s);
istringstream instr(s);
instr>>t;
for(int k=0;k<t;k++)
{
unsigned long long a,b;
getline(file,s);
istringstream instr2(s);
instr2>>a>>b;
unsigned long long count=0;
for(unsigned long long i=a;i<=b;i++)
{
if(is_Pel(i))
{
if(is_Perf(i)&&is_Pel(sqrt(i)))
count++;
}
}
file1<<"Case #"<<k+1<<": "<<count<<"\n";
}
return 0;
}
