#include <iostream>
using namespace std;
#include<string.h>
#include<stdio.h>

int main() {
    int T,i,j;
    char st[1002],p[1002],q[1002];
    scanf("%d",&T);
    for(i=1;i<=T;i++)
    {
        j=1;
        scanf("%s",st);
        p[0]=st[0];
        p[1]='\0';
        while(st[j]!='\0')
        {
            
            q[0]=st[j];
            q[1]='\0';
            if(q[0]>=p[0])
            {
                strcat(q,p);
                strcpy(p,q);
                
            }
            else
            {
                strcat(p,q);
                
            }
            
            j++;
        }
        printf("Case #%d: %s\n",i,p);
        
        
    }
    
    
    
    
    return 0;
}
