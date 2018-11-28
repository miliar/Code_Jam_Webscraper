#include<fstream.h>
#include<conio.h>
#include<stdio.h>
void main()
{
clrscr();
int T,x,i,j,k,N,M,n,m,a[150][150];
char ch;
ifstream fin;
ofstream fout;
fin.open("lawn2.in");
fout.open("lawn2.txt");
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
fin>>N;
fin.get(ch);
fin>>M;
fin.get(ch);
for(i=0;i<N;i++)
{
for(j=0;j<M;j++)
{
fin>>a[i][j];
fin.get(ch);
}
}

for(i=0;i<N;i++)
{
for(j=0;j<M;j++)
{
m=1;
n=1;
for(k=0;k<M;k++)
if(a[i][k]>a[i][j])
m=0;
for(k=0;k<N;k++)
if(a[k][j]>a[i][j])
n=0;
if((m==0)&&(n==0))
{
fout<<"Case #"<<x<<": NO\n";
goto end;
}
}
}
fout<<"Case #"<<x<<": YES\n";
end:
}
getch();
}
