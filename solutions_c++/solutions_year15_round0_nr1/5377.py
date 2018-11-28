#include<stdio.h>
#include<algorithm>
using namespace std;
int main(){
    
    char in[1005];
    int n,m,i,j,k,t;
    int ans,sum;
    
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
       {
        ans = 0;
        sum = 0;
        scanf("%d",&n);
        scanf("%s",in);
        
        for(i=0;i<=n;i++)
        {
            if(sum >= i || in[i] == '0')
            {
                sum+= in[i]-'0';
                //printf("%d sum = %d\n",i,sum);
            }
            else
            {
                ans += i-sum;
                sum = i + in[i]-'0';
            }
        }
        
        printf("Case #%d: %d\n",k,ans);
       }
    
    
    
    
 scanf(" ");
 return 0;
}
