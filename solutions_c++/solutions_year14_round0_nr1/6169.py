#include <cstdio>
#include <cstdlib>
#include <cstdarg>
#include <cstring>
#include<iostream>
//#define debug
using namespace std;
#define rr
int  flag[1003]={0},cnt[1003]={0},i,j,arr[3][5][5];

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

    pFile = fopen ("A.in","r");
    fscanf (pFile, "%d", &t);

    #endif // rr
    while(t--)
    {
        cc++;
        int a,b;
        fscanf (pFile, "%d", &a);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                fscanf (pFile, "%d", &arr[1][i][j]);
            }
        }
        fscanf (pFile, "%d", &b);
        for(i=1;i<=4;i++)
        {
            for(j=1;j<=4;j++)
            {
                fscanf (pFile, "%d", &arr[2][i][j]);
            }
        }
        for(int k=1;k<=4;k++)
        {
            for(i=1;i<=4;i++)
           {
            if(arr[1][a][k]==arr[2][b][i])
            {
                flag[cc]++;
                j=arr[1][a][k];
                if(flag[cc]>1)
                    break;

            }
          }
        }
        #ifdef debug
        cout<<flag[cc]<<"\n";
        #endif // debug
        if(!flag[cc])flag[cc]=-1;
        else if(flag[cc]==1)flag[cc]=j;
        else flag[cc]=0;
    }
    #define ww
#ifdef ww

    isOutFile=true;
    oFile = fopen ("C.txt","w+");
//fprintf (pFile, "%s"
    for( i=1;i<=cc;i++){
    write("Case #%d: ",i);//<<": ";
       if(flag[i]>0)
        write("%d",flag[i]);
        else if(flag[i]==0)write("Bad magician!");
        else write("Volunteer cheated!");


   write("\n");
    }
    fclose(oFile);
    #endif
    fclose(pFile);


    }
