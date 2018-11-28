#include <iostream>
#include <string>
#include <math.h>
#include <algorithm>
#include <fstream>
#include <stdlib.h>
using namespace std;
long long i,z,j,k,a,b,n,d[1000],dd[1000],p,t,u,g,y,az,bz,s,tt;
//------------------------------------------
long long nish(long long h)
{
z=0;
while (h>0)     
{z++; h=h/10;}
return z;
}
//------------------------------------------
long long vahh(long long o)
{
tt=0;
i=0;
while (o>0)     
{i++; dd[i]=o % 10; o=o/10;}
for (j=1; j<=i/2; j++)
if (dd[j]!=dd[i-j+1]) {tt=1; break;}
if (tt==1) return 0; else return 1;
}
long long kkkk(long long l)
{
p=0;
if (t % 2==0)
{
u=1;
p+=d[1];
for (i=2; i<=l; i++)
{u*=10;
p+= d[i]*u;
}
for (i=l; i>=1; i--)
{u*=10;
p+= d[i]*u;
}}
else
{
u=1;
p+=d[1];
for (i=2; i<=l; i++)
{u*=10;
p+= d[i]*u;
}
for (i=l-1; i>=1; i--)
{u*=10;
p+= d[i]*u;
}
}
g=(long long)sqrt(p);
if ((g*g==p) && (a<=p) && (b>=p) && (vahh(g)==1)) return 1; else return 0;
}
//--------------------------------------
long long numb(long long c)
{
y=0;
if (c % 2==1) c=c/2+1; else c=c/2;
for (i=0; i<=c; i++)
d[i]=0;
d[1]=1;
while (d[0]==0)
{
y+=kkkk(c);
d[c]++;
for (j=c; j>=1; j--)
if (d[j]>9) {d[j]=0; d[j-1]++;}
}
return y;
}
//---------------------------------------------
main()
{
freopen ("C-small-attempt0.in","r",stdin);
freopen ("jj.txt","w",stdout);
cin>>n;
for (k=1; k<=n; k++)
{
s=0;
cin>>a>>b;
az=nish(a);
bz=nish(b);
for (t=az; t<=bz; t++)
s+=numb(t);
cout<<"Case #"<<k<<": ";  
cout<<s<<endl;
}}
