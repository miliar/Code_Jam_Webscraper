#include <iostream>
#include <fstream>

using namespace std;

int main()
{
ifstream in("A-large.in");
ofstream out("A-large.out");
int t;
in>>t;
for(int y=1;y<=t;y++)
{
int n;
in>>n;
int a[1009];char c;
for(int i=0;i<=n;i++)
{in>>c;a[i]=c-'0';}
int res=0,sum=0;
for(int i=0;i<=n;i++)
{
if((sum+res)<i)
res=res+i-(sum+res);
sum=sum+a[i];        
}
out<<"Case #"<<y<<": ";
out<<res<<"\n";
}
}
