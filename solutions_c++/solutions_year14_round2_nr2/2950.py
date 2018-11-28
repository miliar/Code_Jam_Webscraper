     #include<stdio.h>
    int main()
    {
     
    int a,b,k,test,ans,l,m,n,i;
    scanf("%d",&test);
    for(i=1;i<=test;i++)
    {ans=0;
    scanf("%d%d%d",&a,&b,&k);
    for(l=0;l<a;l++)
    {
    for(m=0;m<b;m++)
    {
    n=l&m;
    if(n<k)
    ans++;
    }
    }
    printf("Case #%d: %d\n",i,ans);
    }
    return 0;
    }
