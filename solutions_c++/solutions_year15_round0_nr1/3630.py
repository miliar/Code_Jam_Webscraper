#include<cstdio>

int main()
{
    int i,j,k,m,n,t,T;
    char s[1005];
    
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%s",&m,s);
        k=0;i=0;j=0;
        while(i<=m)
            {
             if(j<i)   
                {
                k+= i-j;
                j=i;
                }
            j+=s[i]-'0';
            i++;
    //    printf("#%d: %d  %d\n",i,j,k);
            }
        printf("Case #%d: %d\n",t,k);
    }
    
    return 0;
}
