#include<fstream.h>
#include<conio.h>
#include<stdio.h>
void main()
{
clrscr();

ifstream fin;
fin.open("in.in");
ofstream fout;
fout.open("out.txt");

long int x,T,m[15000],N,i,y,gap,z;
char ch;
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{


y=0;
z=0;
gap=0;

fin>>N;
fin.get(ch);
fin>>m[0];
fin.get(ch);
for(i=1;i<N;i++)
{
fin>>m[i];
fin.get(ch);
if(m[i]<m[i-1])
y+=m[i-1]-m[i];
if(m[i-1]-m[i]>gap)
gap=m[i-1]-m[i];

}
for(i=0;i<N-1;i++)
{
if(m[i]<gap)
z+=m[i];
else
z+=gap;
}
fout<<"Case #"<<x<<": "<<y<<" "<<z<<"\n";


}
getch();

}
