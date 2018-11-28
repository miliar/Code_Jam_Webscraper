#include<iostream>
#include<stdio.h>
#include<conio.h>

using namespace std;
int main()
{
    freopen("A-small-attempt1.in","r",stdin);
    freopen("magic-small.out","w",stdout);
int n,a,b,c[5][5],d[5],e=1,i,j;
cin>>n;
while(e<=n)
{b=0;
cin>>a;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{
cin>>c[i][j];
}
}
for(i=1;i<=4;i++)
{
d[i]=c[a][i];
}
cin>>a;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{
cin>>c[i][j];
}
}
int m;
for(i=1;i<=4;i++)
{

for(j=1;j<=4;j++)
{
if(c[a][i]==d[j])
{
m=d[j];
b++;
}
}
}
if(b>1)
{
cout<<"Case #"<<e<<": Bad magician!\n";
}
else if(b==0)
{
cout<<"Case #"<<e<<": Volunteer cheated!\n";
}
else if(b==1)
{
cout<<"Case #"<<e<<": "<<m<<endl;
}

e++;
}
getch();
return 0;
}
