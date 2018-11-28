#include<fstream.h>
#include<conio.h>
#include<stdio.h>
void main()
{
clrscr();
int x,T,f=0,sm,i,st=0;
char n,ch;
ifstream fin;
ofstream fout;
fin.open("in.in");
fout.open("out.txt");
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
f=0;
st=0;
fin>>sm;
fin.get(ch);
for(i=0;i<=sm;i++)
{
fin.get(n);
if(st>=i)
st+=((int)n)-48;
else
{
f+=i-st;
st+=i-st+((int)n)-48;

}

}
fin.get(ch);
fout<<"Case #"<<x<<": "<<f<<"\n";
}
fin.close();
fout.close();
getch();
}

