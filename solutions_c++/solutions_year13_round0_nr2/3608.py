#include <iostream>
#include <fstream>
using namespace std;
int p,i,j,d,k,m,n,y,x,a[1000][1000],h;
main()
{
freopen ("B-large.in","r",stdin);
freopen ("jj.txt","w",stdout);
cin>>d;
for (k=1; k<=d; k++)
{
cin>>n>>m;
for (i=1; i<=n; i++)
for (j=1; j<=m; j++)
cin>>a[i][j];
for (j=1; j<=m; j++)
a[n+1][j]=0;
for (i=1; i<=n; i++)
a[i][m+1]=0;
cout<<"Case #"<<k<<": "; 
p=0;
for (i=1; i<=n; i++)
{
for (j=1; j<=m; j++)  
{
x=0;
y=0;
for (h=1; h<i; h++)
if (a[h][j]>a[i][j]) {x++; break;}
for (h=i+1; h<=n; h++)
if (a[h][j]>a[i][j]) {x++; break;}
for (h=1; h<j; h++)
if (a[i][h]>a[i][j]) {y++; break;}
for (h=j+1; h<=m; h++)
if (a[i][h]>a[i][j]) {y++; break;}
if ((x>=1) && (y>=1)) {p=1; break;} 
}
if (p==1) break;
}
if (p==1) cout<<"NO"<<endl; else cout<<"YES"<<endl;
}}
