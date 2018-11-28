#include <iostream.h>
#include <fstream.h>
#include <conio.h>
void main()
{
ifstream fin("input.txt", ios::in);
ofstream fout("output.txt",ios::out);
int cases;
fin>>cases;
int x,r,c;
for (int i=0;i<cases;++i)
{
fin>>x>>r>>c;
if (x==1) fout<<"Case #"<<i+1<<": Gabriel";
else if (x==2)
{
if ((r*c)%2==0) fout<<"Case #"<<i+1<<": Gabriel";
else fout<<"Case #"<<i+1<<": Richard";
}
else if (x==3)
{
if ((r==3 && c>1) || (c==3 && r>1)) fout<<"Case #"<<i+1<<": Gabriel";
else fout<<"Case #"<<i+1<<": Richard";
}
else if (x==4)
{
if ((r==4 && c>2) || (c==4 && r>2)) fout<<"Case #"<<i+1<<": Gabriel";
else fout<<"Case #"<<i+1<<": Richard";
}
fout<<endl;
}
}
