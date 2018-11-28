#include <stdio.h>
#include <math.h>
int tcase,loop,n,m;
bool a[40];
void f(int p)
{
    int i,j;
    long long int num,digit,ans[11];
    bool flag;

    if(m<=0)
        return;
    
    if(p>n)
    {
        for(i=2;i<=10;i++)
        {
            num=0; digit=1;
            for(j=n;j>=1;j--)
            {
                if(a[j]==true)
                    num+=digit;
                digit*=(long long int)i;
            }
            
            flag=false;
            for(j=2;;j++)
            {
                if((long long int)j*(long long int)j>num)
                    break;
                
                if(num%j==0)
                {
                    flag=true;
                    break;
                }
            }
            if(flag==false)
                return;
            else
            {
                ans[i]=j;
            }
        }
        
        for(i=1;i<=n;i++)
        {
            if(a[i]==true)
                printf("1");
            else
                printf("0");
        }
        printf(" ");
        for(i=2;i<=10;i++)
            printf("%lld ",ans[i]);
        printf("\n");
        
        m--;
        return;
    }
    
    
    if(p!=1 && p!=n)
    {
        a[p]=false;
        f(p+1);
    }
    
    a[p]=true;
    f(p+1);
}
int main()
{
    
    freopen("C-small-attempt1.in.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    scanf("%d",&tcase);
    
    for(loop=1;loop<=tcase;loop++) {
        
        scanf("%d %d",&n,&m);
        printf("Case #%d:\n",loop);
        
        f(1);
    }
    return 0;
}