#include<bits/stdc++.h>
long double a1[100000],b1[100000],anew[100000],bnew[100000];
int main()
{
int t,pp=0;
scanf("%d",&t);
while(t--)
{
pp++;
int n,i,j,c=0;
scanf("%d",&n);

for(i=0;i<n;i++)
{
scanf("%Lf",&a1[i]);
anew[i]=a1[i];
}
for(i=0;i<n;i++)
{
scanf("%Lf",&b1[i]);
bnew[i]=b1[i];
}
std::sort(a1,a1+n);
std::sort(b1,b1+n);
std::sort(anew,anew+n);
std::sort(bnew,bnew+n);
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(((double)bnew[j]>(double)anew[i]) && ((double)anew[i]!=0.0) &&((double)bnew[j]!=0.0))
{
bnew[j]=0.0;
anew[i]=0.0;
c++;
break;
}
}
}
std::reverse(b1,b1+n);
int pos,cc=0,k=n-1;
for(i=0;i<n;i++)
{
for(j=0;j<n;j++)
{
if(a1[i]>b1[k] &&a1[i]!=0 &&b1[k]!=0)
{
a1[i]=0;
b1[k]=0;
k--;
cc++;
}
else if(a1[i]<b1[j] && a1[i]!=0 && b1[j]!=0)
{
a1[i]=0;
b1[j]=0;
}
}
}
printf("Case #%d: %d ",pp,cc);
if(c==n)
printf("0\n");
else
printf("%d\n",n-c);

}
return 0;
}
