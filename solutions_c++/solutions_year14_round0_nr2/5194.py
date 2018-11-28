#include<stdio.h>
#include<malloc.h>
#include<fstream>
#include<iomanip>
using namespace std;

int main()
{
int test,test_no=1;
double c,f,x;
double starts;
double time;
//ofstream myfile;
//myfile.open ("example.txt");
FILE * pFile;
pFile = fopen ("myfile.txt","w");
scanf("%d",&test);
while(test>=test_no)
{
time=0;
scanf("%lf %lf %lf",&c,&f,&x);
if(c>=x)
{
time = x/2;
}
else
{
starts = x/2;
double no_farms=0;
double div=2+no_farms*f;
while(1)
{
if(starts>((c/div)+x/(f+div)))
{
time+=c/div;
div+=f;
no_farms++;
starts = x/div;
}
else
{
time+=x/div;
break;
}
}
}
//myfile<<"Case #"<<test_no<<": "<<setprecision(8)<<time<<"\n";
fprintf (pFile, "Case #%d: %.7lf\n",test_no,time);
test_no++;
}
float val = 10000010/10000000;
//myfile<<setprecision(10)<<val<<"\n";
//myfile.close();
fclose(pFile);
return 0;
}
