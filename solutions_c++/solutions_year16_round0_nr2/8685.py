#include<cstdio>


int main()
{
int m,n,t,T,ans,i,f;
char a[102];
scanf("%d",&T);

for(t=1;t<=T;t++)
    {
    scanf("%s",a);
    for(n=0;a[n];n++);
    f=(a[0]=='+'?0:1);
    ans=0;
    for(i=1;i<n;i++)
        {
        if((!f && a[i]=='-')||(f&& a[i]=='+'))
            {
            ans++;
            f=!f;    
            }
        }
    if(a[n-1]=='-') ans++;
    printf("Case #%d: %d\n",t,ans);    
    }
    
return 0;    
}
