#include<stdio.h>
#include<algorithm>
using namespace std;
int in[35],DP[100][600],check[50];
int main(){
    
    int n,m,i,j,k,t,c,d,v,a,b,x;
    int re,temp,ans;
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    
    
    
    
    for(x=1;x<=t;x++)
    {
        for(i=0;i<40;i++)
        {   for(j=0;j<40;j++)
            {DP[i][j] = 0;
            }
         check[i]=0;
        }
        scanf("%d%d%d",&c,&d,&v);
        m = 1<<d;
       // printf("%d\n",m);
        for(i=0;i<d;i++)
        {
            scanf("%d",&in[i]);
            temp = 1<<i;
            DP[in[i]][temp] = 1;
        }
        
        for(i=1;i<v;i++)
        {
            for(j=1;j<m;j++)
            {
             if(DP[i][j] == 0) continue;
             a = j;
             for(k=0;k<d;k++)
             {
                if(a%2==0)
                {
                    DP[i+in[k]][j|(1<<k)] = 1;
                }
                a/=2;
             }
             
            }
        }
        re = v;
        for(i=1;i<=v;i++)
        {
            for(j=1;j<m;j++)
            {
                if(DP[i][j] == 1) 
                {
                    check[i] = 1;
                }
            }
        }
        for(i=1;i<=v;i++)
        {
            if(check[i] == 0) {}//printf("%d ",i);
            else re--;
        }
        ans=0;
        for(i=1;i<=v;i++)
        {
            if(check[i] == 0)
            {
                //printf("add %d \n",i);
                ans++;re--;
                
                for(j=v;j>i;j--)
                {
                    if(check[j-i] == 1) 
                    {
                        if(check[j] == 0) re--;
                        check[j] = 1;
                    }
                }
                check[i] = 1;
            }
        }
        //printf("re = %d\n",re);
        printf("Case #%d: %d\n",x,ans);
       // printf("--------break -------\n");
    }
    
    
 scanf(" ");
 return 0;
}
