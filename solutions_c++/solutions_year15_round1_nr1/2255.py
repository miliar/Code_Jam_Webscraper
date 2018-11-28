#include <fstream>
#include <iostream>

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
int a[1000];
for(int i=0;i<n;i++)
in>>a[i];
int res1=0,res2=0;
int r=0;
for(int i=1;i<n;i++)
{
if(a[i-1]-a[i]>0)
{
res1+=a[i-1]-a[i];
r=max(r,a[i-1]-a[i]);
}
}
for(int i=0;i<n-1;i++)
res2+=min(a[i],r);
out<<"Case #"<<y<<": ";
out<<res1<<" "<<res2<<"\n";
}
}
