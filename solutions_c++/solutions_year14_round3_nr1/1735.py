#include<stdio.h>
#include<malloc.h>
#include<fstream>
#include<math.h>
#include<string.h>
using namespace std;
int test;
double  p,q;

int ispower()
{
double s = log2(q);
if(fmod(s,1)==0)
return 1;
return 0;
}
int main()
{
ofstream myfile;
  myfile.open ("example.txt");
scanf("%d",&test);
int i,j;
for(i=0;i<test;i++)
{
scanf("%lf/%lf",&p,&q);
if(ispower()==0)
myfile<<"Case #"<<i+1<<": impossible\n";
else
{
int generation =1;
while(1)
{
if((p/q)>=.5)
{
myfile<<"Case #"<<i+1<<": "<<generation<<"\n";
break;
}
else
{
q=q/2;
generation++;
}
}
}
}
myfile.close();
return 0;
}
