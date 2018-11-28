#include<iostream.h>
#include<conio.h>
#include<fstream.h>

main()
{ ifstream in;
ofstream o;
o.open("A-small-out.txt");
int n,r1,r2,m1[4][4],m2[4][4],i,k,y,ct,j;
in.open("A-small-attempt0.in");

in>>n;

for(i=0;i<n;i++)
{in>>r1;
r1--;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
in>>m1[j][k];

in>>r2;
r2--;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
in>>m2[j][k];
ct=0;
for(j=0;j<4;j++)
for(k=0;k<4;k++)
if(m1[r1][j]==m2[r2][k])
{ct++;y=m1[r1][j];}

if(ct==1)
o<<"Case #"<<i+1<<": "<<y<<"\n";
else if(ct==0)
o<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
else 
o<<"Case #"<<i+1<<": Bad magician!"<<"\n";

                }
      
      
}
