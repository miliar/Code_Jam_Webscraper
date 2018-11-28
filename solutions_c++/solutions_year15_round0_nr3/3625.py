#include<stdio.h>
int main()
{
    int t,m,i,flag,d,z,l,x,j,k;
    scanf("%d",&t);
    int a[5][5]={0,0,0,0,0,0,1,2,3,4,0,2,-1,4,-3,0,3,-4,-1,2,0,4,3,-2,-1};
    /*for(i=0;i<5;++i)
    {
        for(j=0;j<5;++j) printf("%d ",a[i][j]);
        printf("\n");
    }*/
    for(i=1;i<=t;++i)
    {
        scanf("%d%d",&l,&x);
        char c[l];
        scanf("%s",c);
        m=2;
        d=1;
        flag=0;
        for(j=1;j<=x;++j)
        {
            for(k=0;k<l;++k)
            {
                z=c[k]-'g';
                if(d>=0) d=a[d][z];
                else d=-1*a[-1*d][z];
                if(d==m&&m<=3) {m++;d=1;}
                //printf("%c %d %d\n",c[k],d,m);
            }
        }
        if(d==4&&m==4) flag=1;
        if(flag==1) printf("Case #%d: YES\n",i);
        else printf("Case #%d: NO\n",i);
    }
    return 0;
}
