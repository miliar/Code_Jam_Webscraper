#include <cstdio>
#include <cstring>
#include <cstdlib>

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    
    int cases, s, total, i, ans;
    char str[1005];

    gets(str);
    cases = atoi(str);
    for(int c = 1 ; c <= cases ; c++)
    {
        total=ans=s=i=0;

        gets(str);
        //puts(str);
                
        
        while(str[i]!=' ')
        {
            i++;
        }

        i+=2;
        total = str[i-1]-'0';
        int nth = 0;
        
        while(str[i])
        {
         int thislevel = str[i]-'0';
         nth++;
         i++;
         
         if(thislevel)
         {         
          if(nth > total)
          {
           ans += (nth-total);
           total += (nth-total) ;
          } 
          total += thislevel;            
         }
        
        }

        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
