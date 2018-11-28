#include<iostream>
#include<fstream>
#include<vector>
#include<string.h>
#include<algorithm>
#include<iomanip>
using namespace std;
int main()
{

ifstream in("test");
ofstream out("opt");
int n;
in>>n;
for(int i=0;i<n;i++)
{out<<"Case #"<<i+1<<": ";
double c,f,x;
in>>c>>f>>x;
if(x<=c)
out<<(x/2)<<endl;
else
{
double f1=2;
double pt=0,ct=0;
pt=x/2;
double lapse=c/2;
f1=f1+f;
ct=lapse+(x/f1);
while(pt>ct)
{
pt=ct;
lapse=lapse+(c/f1);
f1=f1+f;
ct=lapse+(x/f1);
}
out<<fixed<<setprecision(7)<<pt<<endl;
}  
}
return 1;
}
