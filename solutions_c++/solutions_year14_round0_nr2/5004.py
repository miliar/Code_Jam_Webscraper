#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main()
{
 int cas,t;
 double c,x,f,total,current,t1,t2,temp;
 ifstream input;
 ofstream output;
 output.open("output.txt");
 input.open("B-large.in");
 input>>cas;
 for (int i=0;i<cas;i++)
 {
  input>>c;
  input>>f;
  input>>x;
  t=0;
  current=2.0;
  total=0.0;
  do
  {
    t2=c/current;
    t1=x/current;
    if(t2>t1)
    {
     t=1;
     total+=t1;
    }
    else
    {
     temp=current+f;
     if(total+t1>(total+t2+x/temp))
      {
       total+=t2;
       current+=f;
      }
      else
      {
       total+=t1;
       t=1;
      }
    }
  }while(t==0);
  output<<"Case #"<<i+1<<": "<<total<<"\n";
 }
}
