#include<cstdio>
int main()
{
    int a[100][100],i,j,k,n,m,test,NO=0,l,g,row[100],col[100],maxrow,maxcol;
    scanf("%d",&test);
    g=1;
    while(test--)
    {
        scanf("%d %d",&n,&m);
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&a[i][j]);
            }
        }
    if(n>1&&m>1)
    {   maxrow=0;
     for(i=0;i<n;i++)
     {
         for(j=0;j<m;j++)
        {
            if(a[i][j]>maxrow)
         maxrow=a[i][j];
         
        }
         row[i]=maxrow;
         maxrow=0;
     }
        maxcol=0;
     for(j=0;j<m;j++)
     {
         for(i=0;i<n;i++)
        {
            if(a[i][j]>maxcol)
         maxcol=a[i][j];
         
        }
         col[j]=maxcol;
         maxcol=0;
     }
     
    for(i=0;i<n;i++)
    {
        for(j=0;j<m;j++)
        {
            if(a[i][j]<row[i]&&a[i][j]<col[j])
            NO=1;
            
        }
    }
        if(NO==1)
        {
            printf("Case #%d: ",g);
            printf("NO\n");
            
        }
        else
        {
          
            printf("Case #%d: ",g);
            printf("YES\n");  
        }
    NO=0;
    
    }
    else
    
            {
                printf("Case #%d: ",g);
            printf("YES\n");}
        g++;
        NO=0;
    }
    return 0;
}
