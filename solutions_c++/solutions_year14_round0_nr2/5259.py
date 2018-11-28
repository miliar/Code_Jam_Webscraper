#include <cstdio>
#include <iomanip>
using namespace std;
int main()
{
    int testcase,p,i=0;;
    scanf("%d",&testcase);
    float C,F,X;
    double ch=2;
    double sec1,sec,totalsec,final,final1[100];
    for(p=0;p<testcase;p++)
    {
    scanf("%f %f %f",&C,&F,&X);
    ch=2;
    sec1=C/ch;
    final=X/ch;
sec=0;
totalsec=0;
i=0;
    while(i!=1)
    {
        ch=ch+F;
        sec=C/ch;
        totalsec=(X/ch);
        totalsec+=sec1;
        sec1=sec+sec1;
        if(final<totalsec)
        {    final1[p]=final;

        i=1;
        }
        final=totalsec;
    }
    }
    for(p=0;p<testcase;p++)
    {
     printf("Case #%d: ",p+1);
     printf("%.7lf \n",final1[p]);
    }
    return 0;
}
