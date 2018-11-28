#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    
    int n,m,i,j,k,t;
    int r,c,w,ans;
    freopen("A-small-attempt1.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
    {
        scanf("%d%d%d",&r,&c,&w);
        ans = c/w;
        if(c%w!=0) ans++;
        ans+= w-1;
        
        printf("Case #%d: %d\n",k,ans*r);
    }
    
 scanf(" ");
 return 0;
}
