#include<bits/stdc++.h>
#include<iostream>
#include<cmath>
#include<cstring>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<stack>
#include<queue>
long double p[10000],q[10000],x[10000],y[10000];
int main()
{
int test,cs=0;
scanf("%d",&test);
while(test--)
{
cs++;
int n,i,j,cout=0;
scanf("%d",&n);

for(i=0;i<n;i++)
{
scanf("%Lf",&p[i]);
x[i]=p[i];
}
for(i=0;i<n;i++)
{
scanf("%Lf",&q[i]);
y[i]=q[i];
}
std::sort(p,p+n);
std::sort(q,q+n);
std::sort(x,x+n);
std::sort(y,y+n);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(((double)y[j]>(double)x[i]) && ((double)x[i]!=0.0) &&((double)y[j]!=0.0))
{
y[j]=0.0;
x[i]=0.0;
cout++;
break;
}
}
}
std::reverse(q,q+n);
int counter=0,xx=n-1;
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(p[i]>q[xx] &&p[i]!=0 &&q[xx]!=0)
{
p[i]=0;
q[xx]=0;
xx--;
counter++;
}
else if(p[i]<q[j] && p[i]!=0 && q[j]!=0)
{
p[i]=0;
q[j]=0;
}
}
}
printf("Case #%d: %d ",cs,counter);
if(cout==n)
printf("0\n");
else
printf("%d\n",n-cout);

}
return 0;
}
