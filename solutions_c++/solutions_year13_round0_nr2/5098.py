#include<cstdio>
int ch(int ar[][102],int i,int j, int m, int n)
{
    int h,x1=0;
    for(h=0;h<m;h++)
    {
		if(ar[h][j]>ar[i][j])
        {
            x1=1;
            
            break;
        }
    }
    if(x1==1)
   {
       for(h=0;h<n;h++)
        {
            if(ar[i][h]>ar[i][j])
            
            return 1;
        }
   }
    return 0;
}
int main()
{
    int tes , t=0;
    scanf("%d",&tes);
    while(tes > t++)
    {
        int n,m,i,j,ar[102][102],fl=0;
        scanf("%d%d",&m,&n);
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            scanf("%d",&ar[i][j]);
        }
        for(i=0;i<m;i++)
        {
            for(j=0;j<n;j++)
            {
                if(ch(ar,i,j,m,n)==1)
                {
                    fl=1;
                    break;
                }
            }
            if(fl==1)
            break;
        }
        if(fl!=1)
        printf("Case #%d: YES\n",t);
        else
        printf("Case #%d: NO\n",t);
        
    }
    return 0;
}
