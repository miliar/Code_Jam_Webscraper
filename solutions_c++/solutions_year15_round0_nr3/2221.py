#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int map(char c)
{
return (c-'1')?(c-'i'+2):1;
} 

int a[5][5];

void init()
{
a[1][1]=1;a[1][2]=2;a[1][3]=3;a[1][4]=4;
a[2][1]=2;a[2][2]=-1;a[2][3]=4;a[2][4]=-3;
a[3][1]=3;a[3][2]=-4;a[3][3]=-1;a[3][4]=2;
a[4][1]=4;a[4][2]=3;a[4][3]=-2;a[4][4]=-1;
}

int multiply(int x,char y)
{
if(x<0)
return -a[-x][map(y)];
else
return a[x][map(y)];
}

int multiply(char y,int x)
{
if(x<0)
return -a[map(y)][-x];
else
return a[map(y)][x];
}
    

int main()
{
init();
ifstream in("C-large.in");
ofstream out("C-large.out");
int t;
in>>t;
for(int y=1;y<=t;y++)
{
int l;long long x;
in>>l>>x;
string s;
in>>s;
int pr=1;
for(int i=0;i<l;i++)
pr=multiply(pr,s[i]);
int lim;
if(4LL<x)lim=4;
else
lim=(int)x;
string temp=s;
for(int i=1;i<lim;i++)
s+=temp;
int n=s.length();
out<<"Case #"<<y<<": ";
if(pr!=1 && ((pr==-1 && x&1) || (pr!=-1 && x%4==2)))
{
int i=0,prod=1;
while(i<n && prod!=2)
{
prod=multiply(prod,s[i]);
i++;          
}
int j=n-1;prod=1;
while(j>=0 && prod!=4)
{
prod=multiply(s[j],prod);
j--;
}
long long total=(long long)l*x;
long long sub=(long long)i+((long long)n-(long long)j-1LL);
if(total>sub && i!=n && j>=0)
out<<"YES\n";
else
out<<"NO\n";          
}
else
out<<"NO\n";
}
}
