#include <bits/stdc++.h>

using namespace std;

int main()
{
    
    int casos;
    scanf("%d\n",&casos);
    char buffer[500];
    for(int caso=1;caso<=casos;caso++)
    {
        gets(buffer);
       
        int len = strlen(buffer);
        bool state=true;
        int flips=0;
     
        for(int i=len-1;i>=0;i--)
        {
            bool current_state=buffer[i]=='+';
             
            if(state!=current_state)
            {
                flips++;
                state=current_state;
            }
             
        }
        
        printf("Case #%d: %d\n",caso,flips);
         
    }
    
    return 0;
}