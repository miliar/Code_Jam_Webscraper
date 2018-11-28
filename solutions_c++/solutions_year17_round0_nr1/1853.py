#include <iostream>
#include <stdio.h>
using namespace std;
int main() 
{
    int t,i,j,p,r,b,k,n,ans;
    cin >> t;
    for (i=1; i<=t; i++)
    {   
        char a[1000];
        p=0; r=0;
        scanf("%s", a);
        scanf("%d", &k);

        for (j=0; a[j] != '\0'; j++)
        p = p+1;
        
        
        for ( j=0; a[j] != '\0'; j++)
        {    
            if ( a[j] == '-')
            {  if ( j <= p-k ) 
                {  r = r+1;
                   for (n=1,b=j; n<=k ;n++,b++)
                   {   if (a[b]== '-')
                          a[b] = '+';
                       else 
                          a[b] = '-';                   
                    }
                }
                else
                 {   r= -1; break;  }
            }
            
         }
        
         
        
        if (r == -1)
        { cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl; }
        else 
        { cout << "Case #" << i << ": " << r << endl; }
     }
}






