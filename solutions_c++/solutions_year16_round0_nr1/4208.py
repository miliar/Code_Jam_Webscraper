#include <stdio.h>
#include <string.h>
int tcase,n;
int main()
{
    int loop,i,j;
    bool check[10];
    char str[300];
    
    freopen("A-large.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&tcase);
    
    for(loop=1;loop<=tcase;loop++) {
        
        scanf("%d",&n);
        
        printf("Case #%d: ",loop);
        
        if(n==0) {
            printf("INSOMNIA\n");
            continue;
        }
        
        for(i=0;i<10;i++)
            check[i] = false;
        
        for(i=1;;i++) {
            
            sprintf(str,"%lld",(long long int)n*(long long int)i);
            
            for(j=0;j<strlen(str);j++) {
                check[str[j]-'0'] = true;
            }
            
            for(j=0;j<10;j++) {
                if(check[j] == false)
                    break;
            }
            
            if(j==10)
            {
                printf("%d\n",n*i);
                break;
            }
        }
    }
    return 0;
}