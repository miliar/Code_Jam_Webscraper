#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
long int sum1, sum2;
int T,n,m[10001],i,j,min,min1;
scanf("%d",&T);
//freopen ("best3.txt","w",stdout);

for(i=1;i<=T;i++)
{
cin >> n;
sum1=0;
sum2=0;
min1=-1;
for(j=0;j<n;j++)
{
cin >> m[j];
if(min1==-1 || m[j]<min1)
min1=m[j];
}
min=-1;
for(j=0;j<n-1;j++)
{
if( m[j]>=m[j+1] && (min==-1 || m[j]-m[j+1]>min))
min=m[j]-m[j+1];
}
if(min==-1)
min=min1;
for(j=0;j<n-1;j++)
{
if(m[j]-m[j+1]>0)
{
sum1+=m[j]-m[j+1];
}
if(m[j]>min)
sum2+=min;
else
sum2+=m[j];
}
cout << "Case #" << i<<": "<<sum1<<" " << sum2<<"\n";
}
//fclose(stdout);
return 0;
}
