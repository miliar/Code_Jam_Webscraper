#include <cstdio>
#include <cstdlib>
#include <cstdarg>
#include <cstring>
#include<iostream>
//#define debug
using namespace std;
#define rr
//#define debug

double  flag[1003];

bool isOutFile;
FILE * oFile, * pFile;
void write(const char *fmt, ...) {
    va_list ap;
    va_start(ap, fmt);
    vprintf(fmt, ap);
    if (isOutFile)
        vfprintf(oFile, fmt, ap);
    va_end(ap);
}
int main()
{
    int t,cc=0;
    #ifdef rr
    //FILE * pFile;

    pFile = fopen ("B.in","r");
    fscanf (pFile, "%d", &t);

    #endif // rr
    while(t--)
    {
        cc++;
     double c,f,x,time=0.0f,c2,rate=2.0f;
      fscanf (pFile, "%lf %lf %lf", &c, &f, &x);
      //time=c/2;
      while(1)
      {
         double t1=x/rate,t2=c/rate + x/(rate+f);
         /*t1=x/rate;
         t2=c/rate + x/(rate+f);*/
         #ifdef debug
         cout<<t1<<" "<<t2<<"\n";
         #endif // debug
         if(t1<t2)
                break;
         time+=c/rate;
         rate+=f;

      }
      #ifdef debug
      cout<<time<<"\n";
      #endif // debug
      flag[cc]=time+x/rate;

    }
    #define ww
#ifdef ww

    isOutFile=true;
    oFile = fopen ("C.txt","w+");
//fprintf (pFile, "%s"
    for(int i=1;i<=cc;i++){
    write("Case #%d: ",i);//<<": ";
     write("%lf",flag[i]);

   write("\n");
    }
    fclose(oFile);
    #endif
    fclose(pFile);


    }
