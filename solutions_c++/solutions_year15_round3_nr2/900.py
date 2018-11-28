#include<stdio.h>
#include<algorithm>
using namespace std;
double cha[30],maxx,ex,temp,all,sum,have;
char in[100],want[100],cur[100];
int a,l,s,check,yes[100];
void cal(int idx)
{
    if(idx == s)
    {
        double count = 0;
        for(int i=0;i<s-l+1;i++)
        {
            check = 1;
            for(int j=0;j<l;j++)
            {
                if(cur[i+j] != want[j]) 
                {   check = 0;break;
                }
            }
            if(check == 1)
            {
                count++;
                //for(int j=0;j<l;j++)
                //    yes[i+j]=1;
            }
        }
        /* for(int i=0;i<s;i++)
        {
            if(yes[i]==1) count++;
            yes[i]=0;
        }*/
        have+=count;
        all++;
        if(count > maxx) maxx=count;
        return ;
    }
    
    for(int i=0;i<a;i++)
    {
        cur[idx] = in[i];
        cal(idx+1);
    }
    
    
}
int main(){
    
    int n,m,i,j,k,t,x;
    
    
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    
    scanf("%d",&t);
    
    for(x=1;x<=t;x++)
    {
        for(i=0;i<30;i++) cha[i]=0;
        
        scanf("%d%d%d",&a,&l,&s);
        scanf("%s",in);
        scanf("%s",want);
        
        for(i=0;i<a;i++)
        {
            cha[in[i]-'A']+=1;
        }
        
        all = 0;
        maxx = 0;
        sum=0;
        have = 0;
        cal(0);
        
        ex = have/all;
        //printf("maxx = %lf have = %lf all = %lf\n",maxx,have,all);
        printf("Case #%d: %lf\n",x,maxx-ex);
    }
    
    
 scanf(" ");
 return 0;
}
