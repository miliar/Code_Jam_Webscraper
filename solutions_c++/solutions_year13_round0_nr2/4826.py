#include<stdio.h>
#include<conio.h>
#include<iostream.h>
#include<math.h>


int compute(int a[100][100],int n,int m)
{
    int i,j, b[n][m],row[n],col[m],max;
    for(i=0;i<n;i++)
    {
                    max=a[i][0];
                    for(j=0;j<m;j++)
                    {
                           if(a[i][j]>max)
                           max=a[i][j];         
                    }
                    row[i]=max;
    }
    for(i=0;i<m;i++)
    {
                    max=a[0][i];
                    for(j=0;j<n;j++)
                    {
                           if(a[j][i]>max)
                           max=a[j][i];         
                    }
                    col[i]=max;
    }
    
    for(i=0;i<n;i++)
    {
                    for(j=0;j<m;j++)
                    {
                                    b[i][j]=row[i];
                    }
    }
    for(i=0;i<m;i++)
    {
                    for(j=0;j<n;j++)
                    {
                                    if(b[j][i]>col[i])
                                    b[j][i]=col[i];
                    }
    }
                    
    for(i=0;i<n;i++)
    {
                  for(j=0;j<m;j++)
                   {
                                  if(a[i][j]!=b[i][j])
                                  return 0;
                   }
    }
                    
                    return 1;
}


main()
{
      int a[100][100],n,m,num,b,i,j,ans;
      char s1[]="Case #";
      char s2[]=": ";
      
      FILE *fp,*fw;
      fw=fopen("out_large.txt","w");
      fp=fopen("B-large.in","r");
      
      fscanf(fp,"%d",&num);
      
      for(b=1;b<=num;b++)
      {
                         fscanf(fp,"%d",&n);
                         fscanf(fp,"%d",&m);
                         
                         for(i=0;i<n;i++)
                         {
                                         for(j=0;j<m;j++)
                                         {
                                                         fscanf(fp,"%d",&a[i][j]);
                                         }
                         }
                        
                         
                         ans=compute(a,n,m);
      fputs(s1,fw);
      fprintf(fw,"%d",b);
      fputs(s2,fw);
      
      if(ans==1)
      fputs("YES",fw);
      else
      fputs("NO",fw);
       
      fputs("\n",fw);
      }
      
      
      
}
