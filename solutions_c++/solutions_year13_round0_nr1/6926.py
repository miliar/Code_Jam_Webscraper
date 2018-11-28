#include <iostream>
using namespace std;
int main()
{
int s,a[4][4],j,i,j1,j2,n,k,xwin,ywin;
char c;
cin>>n;
for (j=0;j<n;j++)
{
s=0;
for (j1=0;j1<4;j1++)
for (j2=0;j2<4;j2++)
{
cin>>c;
if (c=='.') a[j1][j2]=-100; else if (c=='X') a[j1][j2]=1; 
else if (c=='O') a[j1][j2]=3; else a[j1][j2]=2;
s+=a[j1][j2];
}
xwin=0;
for (i=0;i<4;i++)
{
k=a[i][0]+a[i][1]+a[i][2]+a[i][3];
if (k==4||k==5) xwin=1;
k=a[0][i]+a[1][i]+a[2][i]+a[3][i];
if (k==4||k==5) xwin=1;
}
k=a[0][0]+a[1][1]+a[2][2]+a[3][3];
if (k==4||k==5) xwin=1;
k=a[0][3]+a[1][2]+a[2][1]+a[3][0];
if (k==4||k==5) xwin=1;
if (xwin==1) cout<<"Case #"<<j+1<<": X won"<<endl;

ywin=0;
for (i=0;i<4;i++)
{
k=a[i][0]+a[i][1]+a[i][2]+a[i][3];
if (k==12||k==11) ywin=1;
k=a[0][i]+a[1][i]+a[2][i]+a[3][i];
if (k==12||k==11) ywin=1;
}
k=a[0][0]+a[1][1]+a[2][2]+a[3][3];
if (k==12||k==11) ywin=1;
k=a[0][3]+a[1][2]+a[2][1]+a[3][0];
if (k==12||k==11) ywin=1;
if (ywin==1) cout<<"Case #"<<j+1<<": O won"<<endl;
if (xwin==0&&ywin==0) 
if (s>0) cout<<"Case #"<<j+1<<": Draw"<<endl;
else cout<<"Case #"<<j+1<<": Game has not completed"<<endl;
}
return 0;
}
