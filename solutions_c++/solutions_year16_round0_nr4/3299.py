#include <stdio.h>
int tcase,loop;
int k,c,s;
int main()
{
    
    freopen("D-small-attempt0.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int i;
    long long int p;
    
    scanf("%d",&tcase);
    
    for(loop=1;loop<=tcase;loop++) {
        
        scanf("%d %d %d",&k,&c,&s);
        
        p=1;
        for(i=1;i<c;i++)
            p*=k;
        
        printf("Case #%d: ",loop);
        
        for(i=0;i<s;i++)
            printf("%lld ",p*(long long int)i+1);
        printf("\n");
        
    }
    return 0;
}