#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    
    int t, n, i;
    int c[10];
    char d[10];
    int b = 0;
    int r = 0;
    scanf("%d", &t);
    int t1 = t;
    if((t>=1) && (t<=100))
    {
    while ( t-- )
    {
       for(i=0;i<10;i++)
        c[i] = 0;
        r = 0;
        b = 0;
        scanf("%d %s",&n,&d);
        if((n>=0) && (n<=6))
            {
             int len = strlen(d) ;
             for(i=0;i<len;i++)
             c[i] = ( d[i] - '0' );
            
             for(i=0;i<=n;i++)
                {
                 if(i == 0)
                    r = r+c[i];
             
                 else
                    {
                    if((r>=i) || (c[i] == 0) )
                        {
                         r = r + c[i];
                     
                        }
                    else
                        {
                         b = b+(i-r);
                         r = r + c[i]+b;
                        }
                     }
            
                 }
             printf("Case #%d: %d\n",(t1-t),b);
            }
       
        
    }
    }    
    
        
   return 0;
}
