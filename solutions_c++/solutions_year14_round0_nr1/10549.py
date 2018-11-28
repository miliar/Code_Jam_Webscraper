#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<string.h>
void main()
{
clrscr();
ifstream fin;
ofstream fout;
fin.open("in.in");
fout.open("out.txt");
int ans,in,a[4],j,i,k,num,rep,T,x;
char ch;
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
rep=0;
fin>>ans;
fin.get(ch);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
fin>>in;
fin.get(ch);
if(i==ans-1)
{
a[j]=in;
}
}
fin>>ans;
fin.get(ch);
for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
fin>>in;
fin.get(ch);
if(i==ans-1)
{
for(k=0;k<4;k++)
{
if(in==a[k])
{
rep++;
num=a[k];
break;
}
}
}
}
if(rep==1)
fout<<"Case #"<<x<<": "<<num<<"\n";
else if(rep==0)
fout<<"Case #"<<x<<": "<<"Volunteer cheated!\n";
else
fout<<"Case #"<<x<<": "<<"Bad magician!\n";
}
getch();


}