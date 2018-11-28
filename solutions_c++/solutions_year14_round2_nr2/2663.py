#include <cstdio>
#include <cstdlib>
#include <cstdarg>
#include <cstring>

using namespace std;
#define rr
char str[16007];
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
    int t,cc=0,counter[103]={0},i,j;
    #ifdef rr
    //FILE * pFile;

    pFile = fopen ("A.in","r");
    fscanf (pFile, "%d", &t);

    #endif // rr
    while(t--)
    {
    cc++;
    int a,b,c;
    fscanf(pFile,"%d%d%d",&a,&b,&c);
    for(int i=0;i<a;i++)
      for(int j=0;j<b;j++)
        if((i&j)<c)
          counter[cc]++;

    }

    //cin>>t;
//    cout<<str<<"\n";

#define ww
#ifdef ww

    isOutFile=true;
    oFile = fopen ("A.txt","w");
//fprintf (pFile, "%s"
   for(int i=1;i<=cc;i++)
   {

     write("Case #%d: %d\n",i,counter[i]);
   }
    #endif
    fclose(pFile);
}
