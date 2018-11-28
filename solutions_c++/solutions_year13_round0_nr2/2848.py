#include <iostream>
#include <cstdio>
using namespace std;
int a[128][128];
int n, m;
bool solve ()
{
   scanf ("%d%d", &n, &m);
   int i, j; 
   for (i = 0; i < n; i ++)
       for (j = 0; j < m; j ++)
           scanf ("%d", &a[i][j]);
       
   
   int k;
   
   for (i = 0; i < n; i ++)
       for (j = 0; j < m; j ++)
       {
            int colok = 1, rowok = 1;
            for (k = 0; k < n; k ++)
            {
                if (a[k][j] > a[i][j]) 
                {   
                    rowok = 0;
                    break;
                }
            }
            for (k = 0; k < m; k ++)
            {
                if (a[i][k] > a[i][j]) 
                {   
                    colok = 0;
                    break;
                }
            }
       if (!rowok && !colok)
           return false; 
           
    }
    
    
    return true;
}


int main ()
{
    int t; 
    scanf ("%d", &t);
    
    int i; 
    for (i = 1; i <=t; i ++)
    {
        printf ("Case #%d: %s\n",i,  solve()?"YES":"NO");
    }
    
    
}