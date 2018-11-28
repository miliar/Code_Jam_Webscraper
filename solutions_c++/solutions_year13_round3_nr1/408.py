#include<stdio.h>
#include<algorithm>
using namespace std;
int table[1000005];
char in[1000005];
int main(){
    
    int n,m,i,j,k,t,a,b,r,l,s,cur;
    long long ans;
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    /*ans = 1000000;
    ans *= 1000001;
    ans *=10;
    ans *=20;
    printf("%lld",ans);*/
    
    scanf("%d",&t);
    
    for(k=1;k<=t;k++)
       {
        ans = 0;
        scanf("%s",in);
        scanf("%d",&m);
        
        for(i=0;in[i]!='\0';i++)
           {
            if(in[i] == 'a' || in[i] == 'e' || in[i] == 'i' || in[i] == 'o' || in[i] == 'u')
               table[i] = 0;
            else table[i] = 1;
           }
        n = i;
        l = 0;
        r = -1;
        cur = 0;
        
        while(l < n)
           {
            //printf("l = %d  r = %d  \n",l,r);
            if(cur < m)
               {
                if(r == n-1) break;
                
                r++;
                if(table[r] == 1)
                   {
                    if(cur == 0)
                       s = r;
                    cur++;
                    
                    //if(cur >= m) ans++;
                   }
                else
                   {
                    cur = 0;
                   }
               }
            else
               {
                //ans += n-r-1;
                if(s == l)
                   {
                    s++;
                    cur--;
                   }
                l++;
               }
            if(cur >= m)
               ans+= n-r;
            
            
           }
        
        
        printf("Case #%d: %lld\n",k,ans);
        
       }
    
    
    
 scanf(" ");
 return 0;
}
