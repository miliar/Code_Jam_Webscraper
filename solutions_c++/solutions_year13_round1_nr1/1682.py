#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>
#define MAXSIZE 100002
#define MODVALUE 1000000007
#define MAX(a,b) \
({ __typeof__ (a) _a = (a); \
__typeof__ (b) _b = (b); \
_a > _b ? _a : _b; })
 
#define MIN(a,b) \
({ __typeof__ (a) _a = (a); \
__typeof__ (b) _b = (b); \
_a < _b ? _a : _b; })
 
#define FOR(a,b,c) for(long a=b;a<c;a++)
int main()
{
    int T,r,V;
    scanf("%d",&T);
    FOR(i,0,T)
    {
        scanf("%d %d",&r,&V);
        int tempV=0;
        long long int ringcount=0;
        while(1)
        {
        
            tempV+=(r+2*ringcount+1)*(r+2*ringcount+1)-(r+2*ringcount)*(r+2*ringcount);
            if(tempV<=V)
                ringcount++;
                else break;
        }
        printf("Case #%ld: %lld\n",(i+1),ringcount);
    
    }
}
