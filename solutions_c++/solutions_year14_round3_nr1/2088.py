# include <stdio.h>
    # include <math.h>
    int main()
    {
freopen("A-small-attempt2.in.txt", "r", stdin);
freopen("output.txt", "w", stdout);
    int t,i,k;
    char c[100000];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
    int flag=0,count=0;
    double a=0,b=0;
    scanf("%s",&c);
    for(k=0;c[k]!='\0';k++)
    {
    if(c[k]=='/')
    {
    flag=1;
    continue;
    }
    if(flag==0)
    a=a*10+((int)c[k]-48);
    else
    b=b*10+((int)c[k]-48);
    }
    while(b>1)
    {
    if(a<b)
    count++;
    if(a==b)
    break;
    b=b/2;
    if(floor(b)!=ceil(b))
    {
    printf("Case #%d: impossible\n",i);
    flag=0;
    break;
    }

    }
    if(flag==1)
    printf("Case #%d: %d\n",i,count);
    }
    return 0;
    }
