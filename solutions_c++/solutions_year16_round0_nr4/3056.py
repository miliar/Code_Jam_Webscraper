#include<bits/stdc++.h>
unsigned long long int power(int k,int c)
{
    if(c==0)
        return 1;
    if(c==1)
        return k;
    unsigned long long int temp=power(k,c/2);
    temp=temp*temp;
    if(c%2!=0)
        temp=temp*k;
    return temp;
}
int main()
{
    freopen("D-small-attempt0 (1).in","r",stdin) ;
    freopen("Dsmall.out","w",stdout) ;
    int t,coun=1;
    scanf("%d",&t);
    while(t--)
    {
        int k,c,s;
        scanf("%d %d %d",&k,&c,&s);
        if(k==s)
        {
            printf("Case #%d:",coun);
            coun++;
            unsigned long long int mm=power(k,c-1);
            for(int i=0;i<k;i++)
            {
                printf(" %llu",1+(i)*mm);
            }
            printf("\n");
        }
    }
return 0;
}
