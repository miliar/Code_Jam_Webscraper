#include <cstdio>
int arr[1050],a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z;
int main()
{
    scanf(" %d",&t);
    for(l=1;l<=t;l++)
    {
        printf("Case #%d: ",l);
        scanf(" %d",&a);
        s=0,z=0;
        for(i=0;i<=a;i++)
        {
            char tp;
            scanf(" %c",&tp);
            if(s<i)z+=(i-s),s=i;
            if(s>=i)s+=tp-'0';
        }
        printf("%d\n",z);
    }
    return 0;
}
