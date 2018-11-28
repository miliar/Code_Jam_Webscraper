#include<fstream.h>
#include<conio.h>
#include<math.h>

ifstream fin("A.txt");
ofstream fout("Out.txt");

int pallin(double x)
{
 double rev,copy,y,loop;

 rev=0;
 copy=x;

 while(copy>0)
 {
  y=copy;

  while(y-10>0)
  y=y-10;

  rev=rev*10+y;
  copy=(int) (copy/10);
 }

 if(rev==x)
 return 1;
 else
 return 0;
}
void main()
{
 clrscr();
 double n1,n2,sq,i,temp;
 int count,flag1,flag2,test,l;

 fin>>test;

 for(l=1;l<=test;l++)
 {
  fin>>n1;
  fin>>n2;
  count=0;

  for(i=n1;i<=n2;i++)
  {
   flag1=pallin(i);

   if(flag1==1)
   {
    sq=sqrt(i);
    temp=(int)(sq);

    if(sq-temp==0.0000000000000)
    flag2=pallin(sq);
    else
    flag2=0;
   }

   if(flag1==1 && flag2==1)
   count++;
  }

  fout<<"Case #"<<l<<":"<<" "<<count<<'\n';
 }

 getch();
}