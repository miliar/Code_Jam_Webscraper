#include <ctype.h>

#include <stdio.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <fstream>
#include <iostream>

#define D 101
#define S "C-small-attempt0.in"
#define L "C-large-attempt0.in"

using namespace std;

typedef struct
{
    int lwr, upr;
}no;
no A;
int isPal(long a);
int isSqr(long a);

int main(int argc, char* argv[])
{
   //sprintf(s, "%d",a); 
     char tmp[16], buffer[100];
    int i, j, k, a, b, var = 0, c = 0;
    ifstream file;
    ofstream fil;
    file.open(S, ios::in);
    fil.open("C.out", ios::out);
    //if(!file.is_open())                       file.open(L, ios::in);
    file>>var;
    
    for (int loop = 0; loop < var; loop++)
    {
        c=0;
        file>>a>>b;
        A.lwr = a;
        A.upr = b;
        for(i=A.lwr; i <= A.upr; i++)
                       if(isPal(i))
                                   if (isSqr(i))
                                      if (isPal((long)sqrt((double)i)))
                                         c++;
        //cout<<"\n"<<a<<' '<<b;
        sprintf (buffer, "Case #%d: %d\n", loop+1, c);
        printf("%s",buffer);
        fil<<buffer;
    }
    system("pause");
    file.close();
    return 0;
}
int isSqr(long a)
{
    long xp=(long)sqrt((double)a);
    if(a==(xp*xp))
        return 1;
    else
        return 0;
} 
int isPal(long a)
{
    int ary[D], i, j, k;
    for(i=0; a != 0; i++)
    {
             ary[i]=a%10;
             a = a/10;
    }
    for(j=0, k = i-1; j<i/2; j++, k--)
    {
             //cout<<ary[j]<<' '<<ary[k];
             if(ary[j] != ary[k])
                 return 0;
    }
    return 1;
}  
