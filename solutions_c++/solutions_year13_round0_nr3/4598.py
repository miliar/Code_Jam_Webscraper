#include<fstream.h>
#include<conio.h>
#include<math.h>
#include<stdio.h>
int check(long x)
{
long j,m=x,n=0;
for(j=10;x/j!=0;j*=10);
for(j/=10;j>=1;j/=10,m/=10)
n+=(m%10)*j;
if(x==n)
return 1;
return 0;
}
int rt(long r,long x)
{
if(r*r==x)
return r;
return 12;
}
void main()
{
clrscr();
long no,i,M,N,T,x;
char ch;
ifstream fin;
ofstream fout;
fin.open("fsquare.in");
fout.open("fsquare.txt");
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
no=0;
fin>>M;
fin.get(ch);
fin>>N;
fin.get(ch);
for(i=M;i<=N;i++)
{
if(check(i)==1)
{
if(check(rt(sqrt(i),i))==1)
no++;
}
}
fout<<"Case #"<<x<<": "<<no<<"\n";
}
getch();
}