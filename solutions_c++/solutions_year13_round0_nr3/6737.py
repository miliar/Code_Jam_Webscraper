#include<stdio.h>
#include<math.h>
int ispal(int n)
{
    int i,a[105];
    for(i=1;n!=0;i++)
    {a[i]=n%10;n=n/10;}
    int f=1,l=i-1,num=0;
    int x=f,y=l;
    if(l==1) return 1;
    if(l%2)
    {
        while(f<=l)
        {
            if(a[f]==a[l])
            {f++;l--;
            num+=2;}
            else break;
        }
        if(num-1==y) return 1;
        else return 0;
    }
    else
    {
        while(f<=l)
        {
            if(a[f]==a[l])
            {num+=2;
            f++;l--;}
            else break;
        }
        if(num==y) return 1;
        else return 0;
    }
}
int issqu(double n)
{
    if(sqrt(n)==(int)(sqrt(n)))
    return 1;
    else return 0;
}
main()
{
    freopen("A1.in","r",stdin);
    freopen("A11.txt","w",stdout);
    int n,k=1;
    scanf("%d",&n);
    while(n--)
    {
        int i,l,r,num=0;
        scanf("%d%d",&l,&r);
        for(i=l;i<=r;i++)
        {
            if(ispal(i)&&issqu(i)&&ispal(sqrt(i)))
            num++;
        }
        printf("Case #%d: %d\n",k++,num);
    }
}
