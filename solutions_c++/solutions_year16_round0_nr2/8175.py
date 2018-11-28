#include <iostream>
#include <stdio.h>
#include <cstring>
using namespace std;
bool all_is(char ar[], char l)
{
    int t_size = (int)strlen(ar);
    for(int i=0;i<t_size;i++)
    {
        if(ar[i] != l)
            return false;
    }
    return true;
}
int main()
{
    int t, flips;
    FILE * pFile;
    FILE * rFile;
    char a[101];
    int t_size;
    pFile = fopen ("B-large.in","r");
    rFile = fopen ("A-small-practice.out","w+");
    fscanf(pFile, "%d", &t);
    for(int i = 0; i<t;i++)
    {
        fscanf(pFile, "%s", a);
        t_size = (int)strlen(a);
        if(all_is(a, '+'))
            fprintf(rFile, "Case #%d: 0\n", i+1);
        else if(all_is(a, '-'))
            fprintf(rFile, "Case #%d: 1\n", i+1);
        else
        {
            flips = 0;
            for(int j=1;j<t_size;j++)
            {
                if(a[j]!=a[0])
                {
                    for(int k=0;k<j;k++)
                        a[k]=a[j];
                    flips++;
                }
            }
            if(all_is(a, '+'))
                fprintf(rFile, "Case #%d: %d\n", i+1, flips);
            else if(all_is(a, '-'))
                fprintf(rFile, "Case #%d: %d\n", i+1, flips+1);

        }
    }
    return 0;
}
