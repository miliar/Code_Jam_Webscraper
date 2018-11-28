#include<stdio.h>
#include<algorithm>
using namespace std;
struct node
{
   int w,e,s,d;
   bool operator < (const node &o)const
   {
        return d < o.d;
   }
}table[1000],sd[1000];
int wall[10000];
int main(){
    
    int n,m,i,j,k,a,b,t,last,ds,dp,dd,w,e,s,d,check,ans,ll,cur,cc;
    
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    for(k=1;k<=t;k++)
       {
        last = 0;
        scanf("%d",&n);
        for(i=0;i<n;i++)
           {
            scanf("%d%d%d%d%d",&d,&a,&w,&e,&s);
            scanf("%d%d%d",&dd,&dp,&ds);
            
            w+= 500;
            e+= 500;
            w *= 2;
            e *= 2;
            dp *= 2;
            for(j=0;j<a;j++)
               {
                table[last].w = w;
                table[last].e = e;
                table[last].s = s;
                table[last].d = d;
                
                d += dd;
                w += dp;
                e += dp;
                s += ds;
                last++;
                
               }
           }
        sort(table,table+last);
        /*for(i=0;i<last;i++)
           {
            printf("%d %d\n",table[i].d,table[i].s);
           }*/
        
        for(i=0;i<3000;i++)
           wall[i] = 0;
        ans = 0;
        
        for(i=0;i<last;i++)
           {
            ll = 0;
            for(j=table[i].w;j<=table[i].e;j++)
               {
                if(wall[j] < table[i].s)
                   {ans++;
                    //printf("%d\n",i);
                    break;
                   }
               }
            cc = i;
            if(table[cc].d != table[cc+1].d)
               {
                while(table[cc].d == table[i].d)
                   {
                    for(j=table[cc].w;j<=table[cc].e;j++)
                       wall[j] = max(wall[j],table[cc].s);
                    cc--;
                   }
               }
            
           }
        
        printf("Case #%d: %d\n",k,ans);
       }
    
    
    
 scanf(" ");
 return 0;
}
