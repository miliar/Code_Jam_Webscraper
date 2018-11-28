#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<stdio.h>
void main()
{
 int t,pos,count;
 int a1[4][4],a2[4][4];
 int r1,r2;
 int i,j,k;
 clrscr();
 ifstream fin("input.in");
 ofstream fout("output.out");
 if(!fin)
 {
   cout<<"file not found";
   getch();
   return;
 }
 fin>>t;
 for(int x=1;x<=t;x++)
 {
  fin>>r1;
  for(i=0;i<4;i++)
   for(j=0;j<4;j++)
     fin>>a1[i][j];
  fin>>r2;
  for(i=0;i<4;i++)
   for(j=0;j<4;j++)
     fin>>a2[i][j];
  r1=r1-1;
  r2=r2-1;
  for(i=0,count=0,pos=-1;i<4;i++)
  {
   for(j=0;j<4;j++)
   {
    if(a1[r1][i]==a2[r2][j])
    {
     count++;
     pos=i;
    }
   }
  }
 if(count==0)
 {
  fout<<"Case #"<<x<<": Volunteer cheated!\n";
 }
 else if(count==1)
 {
 fout<<"Case #"<<x<<": "<<a1[r1][pos]<<"\n";
 }
 else
 {
 fout<<"Case #"<<x<<": Bad magician!\n";
 }
}
fin.close();
fout.close();

getch();
 }