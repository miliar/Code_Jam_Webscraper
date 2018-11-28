#include<iostream.h>
#include<conio.h>
void print(int c[4][4],int d[4][4],int x1,int x2);
int main()
{
clrscr();
int a[4][4],b[4][4];
int t,z1,z2,z,i,j,k,l;
cin>>t;
for(z=1;z<=t;z++)
{
cin>>z1;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
cin>>a[i][j];
cin>>z2;
for(k=0;k<4;k++)
for(l=0;l<4;l++)
cin>>b[k][l];
cout<<"Case #"<<z<<": ";
print(a,b,z1,z2);cout<<"\n";
}
getch();
return 0;
}

void print(int c[4][4],int d[4][4],int x1,int x2)
{
int flag=0,k,i,j,f=0;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(c[x1-1][i]==d[x2-1][j])
{
f++;
if(flag==0)
{
k=c[x1-1][i];
flag=1;
}
}
}
}
if(f==0)
cout<<"Volunteer cheated!";
else if(f==1)
cout<<k;
else
cout<<"Bad magician!";
}

