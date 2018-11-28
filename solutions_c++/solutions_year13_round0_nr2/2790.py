#include<stdio.h>
int main()
{
int t,i,j,k,l,m,n,x,col;
freopen("input.in","r",stdin);
freopen("output.txt","w",stdout);
scanf("%d\n",&t);
for(i=0;i<t;i++)
{x=0;
                scanf("%d %d\n",&m,&n);
                int a[m][n];
                for(j=0;j<m;j++)
                {for(k=0;k<n;k++)
                scanf("%d ",&a[j][k]);
                scanf("\n");
                }
int row;
for(j=0;j<m;j++)
{row=0;
                for(k=0;k<n;k++)
                {if(a[j][k]==1)
                row++;
                }
  for(k=0;k<n;k++)
  {if(a[j][k]==1)
  { col=0;
            for(l=0;l<m;l++)
            {if(a[l][k]==1)col++;}
                if(col!=m && row!=n)
                {x=1;goto result;}
  }
       
 }
 }
result:
if(x==1)
printf("Case #%d: NO\n",i+1);
else
printf("Case #%d: YES\n",i+1);

}

return 0;
}//end main
