//in the name of GOD
#include<fstream.h>
#include<stdlib.h>
#include<stdio.h>
void main()
{
double cases,x,c,f,time,done=0.0,flag=1.0,r=2.0;
fstream ifile("b1.in",ios::in);
fstream ofile("b1.out",ios::out);
ifile>>cases;
while(done<cases)
{
 ifile>>c;
 ifile>>f;
 ifile>>x;
 time=0.0;
 flag=1.0;
 r=2.0;
 while(flag)
 {

  if((x/r)<(c/r+x/(r+f)))
  {
  time=time+x/r;
  flag=0.0;
  }
  else
  {
  time=time+c/r;
  r=r+f;
  }
 }
 done=done+1;
 ofile<<"Case #"<<done<<": "<<time<<"\n";
}


}