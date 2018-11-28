#include<iostream>
#include<fstream>
using namespace std;
int main()
{ifstream n("lp.txt");
ofstream j("ot.txt");
int t,k;
n>>t;
for(int l=1;l<=t;l++)
{
{long p=0;
long w=0;
n>>k;
char a[k+1];
n>>a;
for(int i=0;i<=k;i++)
{
if(p<i)
{
w=i-p+w;
p=i;
}
p=p+a[i]-48;
}
j<<"Case #"<<l<<": "<<w<<endl;
}
}
return 0;
}
