#include<stdio.h>
void main()
{
 FILE *f1, *f2;
 f1 = fopen("B.in","r");
 f2 = fopen("Boutput.txt","w");
 int t;
 long float r,c,f,x;
 long float t1,t2,time;
 fscanf(f1,"%d",&t);
 for(int i=0;i<t;i++)
 {
  time=0;
  fscanf(f1,"%lf %lf %lf",&c,&f,&x);
  r=2;
  do
  {
  t1=time+c/r+x/(r+f);
  t2=time+x/r;
  time=time+c/r;
  r=r+f;
  }while(t1<t2);
  fprintf(f2,"Case #%d: %.7lf\n",i+1,t2);
 }
 fclose(f1);
 fclose(f2);
}