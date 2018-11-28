#include<stdio.h>
#include<fstream>

using namespace std;

double dowork(double c,double f,double x)
{
double time1,time2=x/2,time3=c/2;
double g=2+f;
if(time3>time2)
    return time2;
time1=time2;
while(time1>=time2)
{

time1=time2;
time2=time3+x/g;
time3=time3+(c/g);
g=g+f;
}
return time1;
}

int main()
{

    fstream A("input.in",ios::in);
    FILE *B;
    B=fopen("output.in","w+");
double c,f,x;
int t,i=1;
A>>t;
while(i<=t)
{
A>>c;
A>>f;
A>>x;

fprintf(B,"Case #%d: %.7lf\n",i,dowork(c,f,x));
i++;
}
A.close();
fclose(B);
return 0;
}
