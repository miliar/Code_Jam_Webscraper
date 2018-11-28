#include<fstream.h>
#include<conio.h>
#include<math.h>

void main()
{
 clrscr();
 int r,t,count,test,i;
 double req,r1,r2;

 ifstream fin("circle.txt");
 ofstream fout("result.txt");

 fin>>test;

 for(i=1;i<=test;i++)
 {
  count=0;
  fin>>r;
  fin>>t;

  r1=r;
  r2=r1+1;

  req=pow(r2,2)-pow(r1,2);

  while(req<=t)
  {
   count++;
   t=t-req;

   r2=r2+2;
   r1=r1+2;

   req=pow(r2,2)-pow(r1,2);
  }

  fout<<"Case #"<<i<<": "<<count<<"\n";
 }
 getch();
}